def compare(self,Node2):
		if(self.data==None and Node2.data==None):
			return True
		if((self.data!=None and Node2.data==None)or (self.data==None and Node2.data!=None)):
			return False
		if(self.data==Node2.data):
			ans=True
			ans = ans and self.link[0].compare(Node2.link[0]) and self.link[1].compare(Node2.link[1])
			return ans	
		return False