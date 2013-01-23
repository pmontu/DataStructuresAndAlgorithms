import sys
class BSTNode:
    def __init__(self,x,parent):
        self.data = x
        self.left = None
        self.right = None
        self.count = 1
        self.parent = parent

def delete(x,T,parent=None):
    if T is None:
        print('Element Not Found')
    elif x<T.data:
        T.left = delete(x,T.left,T)
    elif x>T.data:
        T.right = delete(x,T.right,T)
    elif T.count==1:
        # 2 CHILDREN
        if T.left and T.right:
            TempNode = findMin(T.right)
            T.data = TempNode.data
            T.right = delete(TempNode.data,T.right,T)
        # 0 CHILDREN
        elif T.left is None and T.right is None:
            T = None
        # 1 CHILDREN
        elif T.right is not None:
            T = T.right
            T.parent = parent
        elif T.left is not None:
            T = T.left
            T.parent = parent
    else:
        T.count = T.count - 1
    return T

def findMin(T):
    if T.left:
        return findMin(T.left)
    else:
        return T

def insert(x,T,parent=None):
    if T is None:
        T = BSTNode(x,parent)
    elif x<T.data:
        T.left = insert(x,T.left,T)
    elif x>T.data:
        T.right = insert(x,T.right,T)
    else:
        T.count = T.count + 1
    return T

def inorder(T):
    if T is None:
        return
    else:
        inorder(T.left)
        b = back(T)
        if b:
            print("back:",b.data)
        sys.stdout.write(str(T.data)+" ")
        if T.parent:
            sys.stdout.write("("+str(T.parent.data)+")")
        print(" ")
        n = next(T)
        if n:
            print("next:",n.data)
        inorder(T.right)

def preorder(T,i=0):
    if T is None:
        return
    else:
        for j in range(i):
            sys.stdout.write("    ")
        print(T.data)
        preorder(T.left,i+1)
        preorder(T.right,i+1)

def next(node):
    if node is None:
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

def back(node):
    if node is None:
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

T = None
T = insert(7,T)
T = insert(4,T)
T = insert(2,T)
T = insert(1,T)

T = insert(13,T)
T = insert(15,T)
T = insert(16,T)
T = insert(6,T)

T = insert(5,T)
T = insert(3,T)
T = insert(11,T)
T = insert(14,T)

T = insert(12,T)
T = insert(9,T)
T = insert(8,T)
T = insert(10,T)

T = delete(11,T)
T = delete(12,T)
T = delete(13,T)
T = delete(8,T)
T = delete(6,T)
T = delete(7,T)
preorder(T)
inorder(T)