"""
The TreeNode represents node in a Tree.
This module is perfect for Binary Tree but their implementation needs restructuring of the TreeNode
for other Tree types.
"""

class TreeNode(object):
	"""
		Node in a Tree has arguments
		data,link[0]-leftlink,link[0]-right link
		emptiness of a TreeNode is indicated by self.data==None
	"""
	### The Default Initializer
	def __init__(self,data=None,link0=None,link1=None):
		self.data=data
		self.link=[]
		self.link.append(link0)
		self.link.append(link1)
	
	### Data in the Tree Node is to be returned
	def getData(self):
		return self.data

	### Compare Method needs to compare only the data.
	###	Since comparing the subTree Nodes depends on the Tree implementation 
	###	B-Tree , B+ Tree , AVL, Binary Search Tree needs   modifications in their  compare method 
	###	This TreeNode just need to care about the data present in it
	###
	###	Compare Two Nodes
	### -1 if self.data is less than that of arguments
	### 0 if both are equal
	### 1 if self.data is greater than that of argument
	
	def compare(self,Node2):
		if(self.data==None and Node2.data==None):
			return True
		if((self.data!=None and Node2.data==None) or (self.data!=None and Node2.data==None) ):
			return False
		if(self.data==Node2.data):
			return True
		else:
			return False


NullNode=TreeNode()