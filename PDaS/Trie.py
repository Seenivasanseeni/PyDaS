#Algorithms for Trie
class Node():
    def __init__(self,letter=None):
        self.letter=letter
        self.isEnd=False
        self.branches={}
        return
    def __getitem__(self,index):
        if index in self.branches:
            return self.branches[index]
        else:
            return False
    def __setitem__(self,index,data):
        self.branches[index]=data
    def __str__(self):
        return '%s: %s'%(self.letter,','.join(self.branches.keys()))
    def __repr__(self):
        return str(self)
def add(T,data):
    #T is a trie and data
    if(len(data)==0):
        return
    CNode=T
    for cletter in data:
        if not CNode[cletter]:
            Tprime=Node(cletter)
            CNode[cletter]=Tprime
        CNode=CNode[cletter]
    CNode.isEnd=True

def search(T,data):
    if(len(data)==0):
        return False
    CNode=T
    for cletter in data:
        if not CNode[cletter]:
            return False
        CNode=CNode[cletter]
    return CNode.isEnd

def searchPrefix(T,prefix):
    if(len(prefix)==0):
        return False
    CNode=T
    for cletter in prefix:
        if not CNode[cletter]:
            return False
        CNode=CNode[cletter]
    return True

T=Node()

add(T,'adadd')
add(T,'adbc')
add(T,'bcd')

class Trie():
    def __init__(self):
        self.T=Node()
        return
    def add(self,word):
        return add(self.T,word)
    def search(self,word):
        return search(self.T,word)
    def searchPrefix(self,prefix):
        return searchPrefix(self.T,prefix)

def test():
    print("Testing Trie methods")
    T=Trie()
    T.add('adadd')
    T.add('adbc')
    T.add('bcd')
    print(T.search('adadd'),"==>should be True")
    print(T.search('bcd'),"===>should be True")
    print(T.search('a'),"===>should be False")
    print(T.searchPrefix('a'),"===>should be True")
    print(T.searchPrefix('bc'),"===>should be True")
    print(T.searchPrefix('d'),"===>should be False")

if __name__ == "__main__":
    test()