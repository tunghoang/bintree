class BinaryTreeNode:
  def __init__(self, value, left=None, right=None, data=None):
    self.left = left
    self.right = right
    self.value = value
    self.data = data
  def isLeaf(self):
    return self.left is None and self.right is None

def dfsFunction(root, path, callback):
  if root is None:
    return
  callback(root, path)
  if root.isLeaf():
    return
  path.append(root.left.value)
  dfsFunction(root.left, path, callback)
  path.pop()
  path.append(root.right.value)
  dfsFunction(root.right, path, callback)
  path.pop()
    
class BinaryTree:
  '''
  Binary tree implementation
  '''
  def __init__(self):
    '''
    Constructor
    '''
    self.root = None
    self.current = self.root

  def goLeft(self):
    '''
    Visit left node of current node
    '''
    if self.current.left is not None:
      self.current = self.current.left

  def goRight(self):
    '''
    Visit left node of current node
    '''
    if self.current.right is not None:
      self.current = self.current.right

  def goRoot(self):
    '''
    Set current node back to root node
    '''
    self.current = self.root

  def insert(self, code, data):
    '''
    Insert a code and its associated data (symbol) into binary tree
    ---
    Parameters:
    - code: list. The code to be inserted. It is an array that holds 0 or 1
    - data: the source symbol for the code `code`
    '''
    if self.root is None:
      self.root = BinaryTreeNode(None)

    self.current = self.root
    while len(code) > 1:
      bit = code.pop(0)
      self.insertChild(bit)
    if len(code) == 1:
      bit = code.pop(0)
      self.insertChild(bit, data = data)

  def insertChild(self, bit, data = None, node = None):
    if bit == 0:
      if self.current.left is None:
        self.current.left = node if node is not None else BinaryTreeNode(0, data = data)
      self.current = self.current.left
    else:
      if self.current.right is None:
        self.current.right = node if node is not None else BinaryTreeNode(1, data = data)
      self.current = self.current.right


  def dfs(self, callback):
    '''
    Depth first search on the tree. It can be used for tree traversal
    ---
    Parameters:
    - callback: Function(node, path). This function will be called on every visited nodes. It takes two parameters:
      - node: BinaryTreeNode. The currently visited node
      - path: array of 0 or 1. This is the values of nodes on the path from root to the node `node`
    '''
    print('start depth first search')
    dfsFunction(self.root, [], callback)

  @staticmethod
  def merge(leftTree, rightTree):
    newTree = BinaryTree()
    newTree.left = leftTree.root
    newTree.right = rightTree.root
    return newTree
