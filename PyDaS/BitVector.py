class BitVector(object):
	"""docstring for BitVector"""
	"""infinite array of bits is present in bitvector"""
	def __init__(self):
		self.BitNum=0
		self.length=0
	def set(self,i):
		self.BitNum=self.BitNum | 1 << i
		self.length=self.BitNum.bit_length()
	def reset(self,i):
		resetValue=1<<i
		self.BitNum=self.BitNum  - resetValue
		self.length=self.BitNum.bit_length()
	def at(self,i):
		if(i<0):
			raise ValueError
		if(i >=self.length):
			return 0
		return int(bin(self.BitNum)[-(i+1)])
	def __repr__(self):
		return bin(self.BitNum)[2:]
	def __str__(self):
		return bin(self.BitNum)[2:]
