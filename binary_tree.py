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
	def delete(self,data):
		if self.root is None:
			return None
		if self.root.data==data:
			if self.root.left is None and self.root.right is None:
				self.root=None
			elif self.root.left and self.root.right is None:
				self.root=self.root.left
			elif self.root.right and self.root.left is None:
				self.root=self.root.right
			elif self.root.left and self.root.right:
				delparent=self.root
				delnode=self.root.right
				while delnode.left:
					delparent=delnode
					delnode=delnode.left
				self.root.data=delnode.data
				if delnode.right:
					if delnode.data<delparent.data:
						delparent.left=delnode.right
					else:
						delnode.right=delnode.right
				else:
					if delnode.data<delparent.data:
						delparent.left=delnode.right
					else:
						delparent.right=delnode.right		


		parent=None
		cur_node=self.root
		while cur_node and cur_node.data!=data:
			parent=cur_node
			if data<cur_node.data:
				cur_node=cur_node.left
			elif data>cur_node.data:
				cur_node=cur_node.right
		if cur_node is None or cur_node.data!=data:
			return None
		elif cur_node.right is None and cur_node.left is None:
			if data<parent.data:
				parent.left =None
			else:
				parent.right=None
		elif cur_node.left is None and cur_node.right:
			if data<parent.data: 
				parent.left=cur_node.right
			else:
				parent.right=cur_node.right
			return True	
		elif cur_node.left and cur_node.right is None:
			if data<parent.data:
				parent.left=cur_node.left
			else:
				parent.right=cur_node.left
			return True
		else:
			delparent=cur_node
			delnode=cur_node.right
			while delnode.left:
				delparent=delnode
				delnode=delnode.left
			cur_node.data=delnode.data
			if delnode.right:
				if delparent.data>delnode.data:
					delparent.left=delnode.right
				else:
					delparent.right=delnode.right
			else:
				if delnode.data<delparent.data:
					delparent.left=None
				else:
					delparent.right=None		
			


bst=BST()
bst.insert(8)
bst.insert(1)			
bst.insert(3)
bst.insert(5)
print(bst.find(1))



				
								
