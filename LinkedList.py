class Node(object):
  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next = next_node


class LinkedList(object):
  def __init__(self):
    self.head=None
    self.length=0
  def prepend(self, data):
    self.head=Node(data,self.head)
    self.length+=1
  def append(self, data):
      temp=self.head
      parent=None
      while(temp!=None):
        parent=temp
        temp=temp.next
      temp=Node(data,None)
      if(parent==None):
        self.head=temp
      else:
        parent.next=temp
      self.length+=1
  def InsertNth(self,data,position):
        temp=self.head
        index=0
        parent=None
        while(index!=position):
          parent=temp
          temp=temp.next
          index+=1
        temp=Node(data)
        if(parent==None):
          temp.next=self.head
          self.head=temp
        else:
          temp.next=parent.next
          parent.next=temp
        self.length+=1
  def printLinkedList(self,sep=" "):
    if(self.length==0):
      return None
    temp=self.head
    while (temp.next!=None):
      print(str(temp.data),end=sep)
      temp=temp.next
    print(temp.data)
  def getData(self,position):
    if(self.length<=position):
      return None
    temp=self.head
    index=0
    while(index!=position):
      temp=temp.next
      index+=1
    return temp.data
  def remove(self,data):
    temp=self.head
    parent=None
    while (temp.data!=data and temp!=None):
      parent=temp
      temp=temp.next
    if(temp==None):
      return  -1
    parent.next=temp.next
    self.length-=1
    return 0
  def removeAt(self,position):
    if(self.length<=position):
      return -1
    temp=self.head
    self.length-=1
    index=0
    if(position==0):
      self.head=self.head.next
      return 0
    while(index!=position):
      parent=temp
      temp=temp.next
      index+=1
    parent.next=temp.next
    return 0