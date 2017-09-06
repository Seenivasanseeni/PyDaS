"""
	Class definition for heaps min-heap max -heap
"""
"""Methods for getiing parent , left and right nodes"""
import math
def parent(i):
	return math.floor((i-1)/2)
def left(i):
	return 2*i+1
def right(i):
	return 2*i+2
#max-heap in which root node value is higher than that of its subtrees
class MaxHeap():
	"""initializer for max-heap wither with an array"""
	def __init__(self,array=None):
			if(array==None):
				print("array Needs to passed as argument")
				return;
			self.heap=[]
			self.heapsize=0
			self.createHeap(array);

	"""method for making heap fro a subarray"""
	def maxHeapify(self,i):
		key=self.heap[i]
		l=left(i)
		r=right(i)
		while(i<self.heapsize/2):
			maxsub=l
			#right child going out of the heap
			if( r>(self.heapsize-1) ):
				if(l<self.heapsize and self.heap[l]>key):
					self.heap[i]=self.heap[l]
					i=l
				break;
			if(self.heap[r]>self.heap[l]):
				maxsub=r
			if(key<self.heap[maxsub]):
				self.heap[i]=self.heap[maxsub] 
				i=maxsub
				l=left(i)
				r=right(i)
			else:
				break
		self.heap[i]=key

	""""create-heap"""
	def createHeap(self,array):
		self.heap=array
		self.heapsize=len(array)
		for i in range(math.floor(self.heapsize/2),-1,-1):
			self.maxHeapify(i)

	""" insert method"""
	def insert(self,n):
		self.heapsize+=1
		self.heap.append(n)
		self.fixIt(self.heapsize-1)
	"""fixIt method fixes the max property of the heap as an element is just appended to the heap as last leaf node.
	So fixing it up requires visiting parent's nodes and maintaning max property"""
	def fixIt(self,i):
		key=self.heap[i]
		j=parent(i)
		while(j>=0): #parents cannot exist behind 0
			if(self.heap[j]<key):
				self.heap[i]=self.heap[j]
				i=j
				j=parent(i)
			else:
				break;
		self.heap[i]=key

	""" extract max extracts the minimum value and removes logically from the heap
	"""
	def extractMax(self):
		if(self.heapsize==0):
			print("Heap is empty...")
			return
		key=self.heap[0]
		self.heap[0]=self.heap[self.heapsize-1]
		self.heap[self.heapsize-1]=key
		self.heapsize-=1
		self.maxHeapify(0)
		return key

	""" findMax returns the maxmimum value of the MaxHeap if it exists
	"""
	def findMax(self):
		if(self.heapsize<=0):
			print("Heap is Empty")
			return NULL
		return self.heap[0]

	#remove method removes the the element and also maintains max-heap property
	def remove(self,data):
		if not data in self.heap:
			print("Element is not in the heap")
			return
		di=self.heap.index(data)
		self.heap[di]=self.heap[self.heapsize-1]
		self.heap[self.heapsize-1]=data
		self.heapsize-=1
		self.maxHeapify(di)
		if(self.heapsize==0):
			self.heap=[]
