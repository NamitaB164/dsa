	return(str(self.val))
def inorder(node):
    if node:
        inorder(node.left)
        print(node)
        inorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node)
def preorder(node):
    if node:
        print(node)
        preorder(node.left)
        preorder(node.right)
def invert(node):
    if node:
        node.left,node.right=node.right,node.left
        invert(node.left)
        invert(node.right)
        return(node)
root=Tree(5)
root.left=Tree(5)
root.right=Tree(15)
root.left.left=Tree(3)
root.left.right=Tree(4)
invert(root)
inorder(root)

#BST

class bst:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return bst(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=' ')
        inorder(node.right)


n = list(map(int, input("Enter numbers: ").split()))
root = None
for i in n:
    root = insert(root, i)

print("Inorder traversal of BST:")
inorder(root)