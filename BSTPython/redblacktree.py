# This code is adapted from a RBT module
# downloaded from http://newcenturycomputers.net/projects/rbtree.html
#
# Author: Manojkumar Purushothaman
#
# Date Created: July 23 2012
# Date Modified: July 23 2012

BLACK = 0
RED = 1

class RBNode(object):

    def __init__(self, key = None, color = RED):
        self.left = self.right = self.parent = None
        self.color = color
        self.key = key
        self.nonzero = 1

    def __nonzero__(self):
        return self.nonzero

class RBTree:
    def __init__(self):
        self.sentinel = RBNode()
        self.sentinel.left = self.sentinel.right = self.sentinel
        self.sentinel.color = BLACK
        self.sentinel.nonzero = 0
        self.root = self.sentinel
        self.elements = 0

    def rotateLeft(self, x):

        y = x.right

        # establish x.right link
        x.right = y.left
        if y.left != self.sentinel:
            y.left.parent = x

        # establish y.parent link
        if y != self.sentinel:
            y.parent = x.parent
        if x.parent:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        else:
            self.root = y

        # link x and y
        y.left = x
        if x != self.sentinel:
            x.parent = y

    def rotateRight(self, x):

        #***************************
        #  rotate node x to right
        #***************************

        y = x.left

        # establish x.left link
        x.left = y.right
        if y.right != self.sentinel:
            y.right.parent = x

        # establish y.parent link
        if y != self.sentinel:
            y.parent = x.parent
        if x.parent:
            if x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
        else:
            self.root = y

        # link x and y
        y.right = x
        if x != self.sentinel:
            x.parent = y

    def insertFixup(self, x):
        #************************************
        #  maintain Red-Black tree balance  *
        #  after inserting node x           *
        #************************************

        # check Red-Black properties

        while x != self.root and x.parent.color == RED:

            # we have a violation

            if x.parent == x.parent.parent.left:

                y = x.parent.parent.right

                if y.color == RED:
                    # uncle is RED
                    x.parent.color = BLACK
                    y.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent

                else:
                    # uncle is BLACK
                    if x == x.parent.right:
                        # make x a left child
                        x = x.parent
                        self.rotateLeft(x)

                    # recolor and rotate
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.rotateRight(x.parent.parent)
            else:

                # mirror image of above code

                y = x.parent.parent.left

                if y.color == RED:
                    # uncle is RED
                    x.parent.color = BLACK
                    y.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent

                else:
                    # uncle is BLACK
                    if x == x.parent.left:
                        x = x.parent
                        self.rotateRight(x)

                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.rotateLeft(x.parent.parent)

        self.root.color = BLACK

    def deleteFixup(self, x):
        #************************************
        #  maintain Red-Black tree balance  *
        #  after deleting node x            *
        #************************************

        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.rotateLeft(x.parent)
                    w = x.parent.right

                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.rotateRight(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.rotateLeft(x.parent)
                    x = self.root

            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.rotateRight(x.parent)
                    w = x.parent.left

                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.rotateLeft(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.rotateRight(x.parent)
                    x = self.root

        x.color = BLACK

    def insertNode(self, key):
        #**********************************************
        #  allocate node for data and insert in tree  *
        #**********************************************

        # find where node belongs
        current = self.root
        parent = None
        while current != self.sentinel:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        # setup new node
        x = RBNode(key)
        x.left = x.right = self.sentinel
        x.parent = parent

        self.elements = self.elements + 1

        # insert node in tree
        if parent:
            if key < parent.key:
                parent.left = x
            else:
                parent.right = x
        else:
            self.root = x

        self.insertFixup(x)
        return x

    def deleteNode(self, z):
        #****************************
        #  delete node z from tree  *
        #****************************

        if not z or z == self.sentinel:
            return

        if z.left == self.sentinel or z.right == self.sentinel:
            # y has a self.sentinel node as a child
            y = z
        else:
            # find tree successor with a self.sentinel node as a child
            y = z.right
            while y.left != self.sentinel:
                y = y.left

        # x is y's only child
        if y.left != self.sentinel:
            x = y.left
        else:
            x = y.right

        # remove y from the parent chain
        x.parent = y.parent
        if y.parent:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        else:
            self.root = x

        if y != z:
            z.key = y.key

        if y.color == BLACK:
            self.deleteFixup(x)

        del y
        self.elements = self.elements - 1

    def findNode(self, key):
        #******************************
        #  find node containing data
        #******************************

        current = self.root

        while current != self.sentinel:
            if key == current.key:
                return current
            else:
                if key < current.key:
                    current = current.left
                else:
                    current = current.right

        return None

    def successor(self,node):
        if not node:
            return
        if node.right:
            n = node.right
            while n.left:
                n = n.left
            return n
        else:
            n = node
            while n.parent and n.parent.right is n:
                n = n.parent
            if n.parent and n.parent.left is n:
                return n.parent
            else:
                return

    def predecessor(self,node):
        if not node:
            return
        if node.left:
            n = node.left
            while n.right:
                n = n.right
            return n
        else:
            n = node
            while n.parent and n.parent.left is n:
                n = n.parent
            if n.parent and n.parent.right is n:
                return n.parent
            else:
                return

import sys
def preorder(t,i=0):
    if t:
        for j in range(i):
            sys.stdout.write("    ")
        var = "B"
        if t.color==RED:
            var="R"
        print(str(t.key)+var)
        preorder(t.left,i+1)
        preorder(t.right,i+1)
    else:
        return

def inorder(t):
    if t:
        inorder(t.left)
        n = ""
        nex = Tree.successor(t)
        if nex:
            n = nex.key
        p = ""
        pre = Tree.predecessor(t)
        if pre:
            p = pre.key
        print p, t.key,n
        inorder(t.right)
    else:
        return

Tree = RBTree()

if __name__ == "__main__":

    Tree.insertNode(10)
    Tree.insertNode(7)
    Tree.insertNode(5)
    Tree.insertNode(3)
    Tree.insertNode(1)
    Tree.insertNode(2)
    Tree.insertNode(15)
    Tree.insertNode(20)
    Tree.insertNode(30)
    Tree.insertNode(18)
    Tree.insertNode(35)
    Tree.insertNode(19)
    Tree.insertNode(17)
    Tree.insertNode(25)

    preorder(Tree.root)

    Tree.deleteNode(Tree.findNode(7))
    Tree.deleteNode(Tree.findNode(5))
    Tree.deleteNode(Tree.findNode(1))
    Tree.deleteNode(Tree.findNode(20))

    preorder(Tree.root)

    inorder(Tree.root)
    print "No of elements: ", Tree.elements