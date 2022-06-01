# find min and max element in BST
class BST:
  def __init__(self,key):
    self.key = key
    self.lchild = None
    self.rchild = None
  # Insertion 
  def insert(self,data):
    if self.key is None:
      self.key = data
      return
    if self.key == data:
      return
    if self.key > data:
      if self.lchild:
        self.lchild.insert(data)
      else:
        self.lchild = BST(data)
    else:
      if self.rchild:
        self.rchild.insert(data)
      else:
        self.rchild = BST(data)
  # searching in tree
  def search(self,data):
    if self.key==data:
      print("node found")
      return 
    if self.key > data:
      if self.lchild:
        self.lchild.search(data)
      else:
        print("node is not present")
    else:
      if self.rchild:
        self.rchild.search(data)
      else:
        print("node is not present ")
  # minimum node value in BST
  def min_node(self):
    current = self
    while current.lchild:
      current = current.lchild
    print("node with minimum key is:",current.key)

  # maximum node value in BST
  def max_node(self):
    current = self
    while current.rchild:
      current = current.rchild
    print("\nnode with maximum  node is :",current.key)


root = BST(10)
list1 = [20,4,30,4,1,5,6]
for i in list1:
  root.insert(i)

root.min_node()
root.max_node()
      