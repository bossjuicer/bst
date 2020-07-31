class Node:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data

class BST:
	def __init__(self):
		self.root=None
	def insert(self,data):
		if self.root is None:
			self.root=Node(data)
		else:
			self._insert(data,self.root)
	def _insert(self,data,cur_node):
		if data<cur_node.data:
			if cur_node.left is None:
				cur_node.left=Node(data)
			else:
				self._insert(data,cur_node.left)
		elif data>cur_node.data:
			if cur_node.right is None:
				cur_node.right=Node(data)
			else:
				self._insert(data,cur_node.right)
		else:
			print("Value already present\n")
	def find(self,data):
		if self.root:
			is_found=self._find(data,self.root)
			if is_found:
				return True
			return False
		else:
			return None							
	def _find(self,data,cur_node):
		if data>cur_node.data and cur_node.right:
			return self._find(data,cur_node.right)
		elif data<cur_node.data and cur_node.left:
			return self._find(data,cur_node.left)
		if data==cur_node.data:
			return True
	#finding an element without recursion
	def findwr(self,data):
		cur_node=self.root
		while cur_node:
			if data==cur_node.data:
				return True
			if data>cur_node.data:
				cur_node=cur_node.right
			else:
				cur_node=cur_node.left
		return False		
		
 	#to find minimum element in binary search tree
        def find_min(self):
		cur_node=self.root
		self._find_min(cur_node.left)
	def _find_min(self,cur):
		if cur.left is None:
			print("minimum element is ",cur.data)
		else:
			self._find_min(cur.left)
			
			
	#to find maximum element in binary searh tree
	def find_max(self):
		cur_node=self.root
		self._find_max(cur_node.right)
	def _find_max(self,cur):
		if cur.right is None:
			print("maximium element is ",cur.data)
		else:
			self._find_max(cur.right)	
			


bst=BST()
bst.insert(8)
bst.insert(1)			
bst.insert(3)
bst.insert(5)
print(bst.find(1))



				
								
