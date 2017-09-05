"""
	Class definition for heaps min-heap max -heap
"""
"""Methods for getiing parent , left and right nodes""""
import math
def parent(i):
	i-=1
	return math.floor(i/2)
def left(i):
	i+=1
	return 2*i
def right(i):
	i+=1
	return 2*i+1
#min-heap in which root node value is smaller than that of its subtrees
class Min-Heap():
	"""initializer for min-heap wither with an array or empty one"""
	def __init__(self,array=None):
			self.heap=[]
			self.heapsize=0
			if(not array==None):
				create_Heap(self,array);

	"""method for making heap fro a subarray"""
	def min-heapify(self,i):
		key=self.heap[i]
		l=left(i)
		r=right(i)
		while(r<=self.heapsize):
			minsub=l
			if(self.heap[r]<self.heap[l]):
				minsub=r
			if(key>self.heap[minsub]):
				self.heap[i]=self.heap[minsub]
				i=minsub
				l=left(i)
				r=right(i)
			else:
				break
		self.heap[i]=key

	""""create-heap""""
	def create_Heap(self,array):
		self.heap=array
		self.heapsize=array.length
		for i in range(math.floor(self.heapsize()))

	""" insert method"""
	def insert(n):
		self.heapsize+=1
		self.heap.append(n)