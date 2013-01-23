import sys
class BSTNode:
    def __init__(self,x,parent):
        self.data = x
        self.left = None
        self.right = None
        self.count = 1
        self.parent = parent
        self.height = 0

def delete(x,T,parent=None):
    if T is None:
        print('Element Not Found')
    elif x<T.data:
        T.left = delete(x,T.left,T)
        if height(T.right) - height(T.left) ==2:
            if T.right.right:
                T = singleRotationWithRight(T)
            elif T.right.left:
                T = doubleRotationWithRight(T)
    elif x>T.data:
        T.right = delete(x,T.right,T)
        if height(T.left) - height(T.right) ==2:
            if T.left.left:
                T = singleRotationWithLeft(T)
            elif T.left.right:
                T = doubleRotationWithLeft(T)
    elif T.count==1:
        # 2 CHILDREN
        if T.left and T.right:
            TempNode = findMin(T.right)
            T.data = TempNode.data
            T.right = delete(TempNode.data,T.right,T)
            #No need to check for rotation here, taken care above
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
    if T:
        T.height = max(height(T.left),height(T.right)) + 1
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
        if height(T.left) - height(T.right) ==2:
            if x<T.left.data:
                T = singleRotationWithLeft(T)
            else:
                T = doubleRotationWithLeft(T)
    elif x>T.data:
        T.right = insert(x,T.right,T)
        if height(T.right) - height(T.left) ==2:
            if x>T.right.data:
                T = singleRotationWithRight(T)
            else:
                T = doubleRotationWithRight(T)
    else:
        T.count = T.count + 1
    T.height = max(height(T.left),height(T.right)) + 1
    return T

def height(P):
    if P is None:
        return -1
    else:
        return P.height

def singleRotationWithLeft(K2):
    K1 = K2.left
    K2.left = K1.right
    K1.right = K2

    K1.height = max(height(K1.left),height(K1.right)) + 1
    K2.height = max(height(K2.left),height(K2.right)) + 1
    return K1

def doubleRotationWithLeft(K3):
    K3.left = singleRotationWithRight(K3.left)
    return singleRotationWithLeft(K3)

def singleRotationWithRight(K1):
    K2 = K1.right
    K1.right = K2.left
    K2.left = K1

    K1.height = max(height(K1.left),height(K1.right)) + 1
    K2.height = max(height(K2.left),height(K2.right)) + 1
    return K2

def doubleRotationWithRight(K1):
    K1.right = singleRotationWithLeft(K1.right)
    return singleRotationWithRight(K1)
    return

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

T = insert(4,T)
T = insert(2,T)
T = insert(6,T)
T = insert(1,T)

T = insert(3,T)
T = insert(5,T)
T = insert(7,T)

T = insert(16,T)
T = insert(15,T)
T = insert(14,T)
T = insert(13,T)

T = insert(12,T)
T = insert(11,T)
T = insert(10,T)
T = insert(8,T)

""" """

T = delete(5,T)
T = delete(6,T)
T = delete(1,T)

preorder(T)

T = delete(14,T)
T = delete(16,T)
T = delete(15,T)

preorder(T)
inorder(T)

"""
13
    7
        3
            2
            4
        11
            10
                8
            12
    15
        14
        16
7
    3
        2
        4
    11
        10
            8
        13
            12
2 (4) 
('back:', 2)
3 (2) 
('next:', 4)
4  
('back:', 4)
7 (6) 
('next:', 8)
8 (10) 
('next:', 10)
('back:', 8)
10 (11) 
('next:', 11)
('back:', 10)
11 (12) 
('next:', 12)
12 (13) 
('next:', 13)
('back:', 12)
13 (14) 
"""