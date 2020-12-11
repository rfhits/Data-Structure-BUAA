import bisect
import collections

class KeyValue(object):
    def __init__(self,key,value):
        self.key=key
        self.value=value
    def __str__(self):
        return str((self.key,self.value))
    def __cmp__(self,key):
        if self.key>key:
            return 1
        elif self.key==key:
            return 0
        else:
            return -1
    def __lt__(self,other):
        if type(other)==KeyValue:
            return self.key<other.key
        elif type(other)==int:
            return self.key<other

class InterNode:
    def __init__(self,keynum):
        self.parent=None
        self.keynum=keynum
        self.keylist=[]
        self.sonlist=[]
    def isleaf(self):
        return False
    def isfull(self):
        return (len(self.keylist) >= self.keynum-1)
    def isempty(self):
        return (len(self.keylist) <= (self.keynum+1)/2-1)
    
class LeafNode:
    def __init__(self,valuenum):
        self.valuenum=valuenum
        self.valuelist=[]
        self.brother=None
        self.parent=None
    def isleaf(self):
        return True
    def isfull(self):
        return (len(self.valuelist)>self.valuenum)
    def isempty(self):
        return (len(self.valuelist)<=(self.valuenum+1)/2)
    def __lt__(self,other):
        return self

class Bptree:
    def __init__(self,keynum,valuenum):
        if valuenum>keynum:
            raise ValueError
        else:
            self.valuenum = valuenum
            self.keynum = keynum
            self.root = LeafNode(valuenum)
            self.leaf = self.root
    def insert(self,keyvalue):
        def split_node(n1):
            mid = int(self.keynum/2)
            newnode = InterNode(self.keynum)
            newnode.keylist = n1.keylist[mid:]
            newnode.sonlist = n1.sonlist[mid:]
            newnode.parent = n1.parent
            for son in newnode.sonlist:
                son.parent = newnode
            if n1.parent is None:    #split root
                newroot = InterNode(self.keynum)
                newroot.keylist = [n1.keylist[mid-1]]
                newroot.sonlist = [n1,newnode]
                n1.parent = newroot
                newnode.parent = newroot
                self.root = newroot
            else:
                i = n1.parent.sonlist.index(n1)
                n1.parent.keylist.insert(i,n1.keylist[mid-1])
                n1.parent.sonlist.insert(i+1,newnode)
            n1.keylist = n1.keylist[:mid-1]
            n1.sonlist = n1.sonlist[:mid]
            return n1.parent
        def split_leaf(n2):
            mid=int((self.valuenum+1)/2)
            newleaf=LeafNode(self.valuenum)
            newleaf.valuelist=n2.valuelist[mid:]
            if n2.parent==None:
                newroot=InterNode(self.keynum)
                newroot.keylist=[n2.valuelist[mid].key]
                newroot.sonlist=[n2,newleaf]
                n2.parent=newroot
                newleaf.parent=newroot
                self.root=newroot
            else:
                i=n2.parent.sonlist.index(n2)
                n2.parent.keylist.insert(i,n2.valuelist[mid].key)
                n2.parent.sonlist.insert(i+1,newleaf)
                newleaf.parent=n2.parent
            n2.valuelist=n2.valuelist[:mid]
            n2.brother=newleaf
        def insert_node(n):
            if n.isleaf()==False:
                if n.isfull():
                    insert_node(split_node(n))
                else:
                    p = bisect.bisect_right(n.keylist,keyvalue)
                    insert_node(n.sonlist[p])
            else:   #n is leaf node
                p = bisect.bisect_right(n.valuelist,keyvalue)
                n.valuelist.insert(p,keyvalue)
                if n.isfull():
                    split_leaf(n)
                
        node = self.root
        insert_node(node)
    
    def traversal(self):
        result=[]
        l=self.leaf
        while True:
            result.extend(l.valuelist)
            if l.brother==None:
                return result
            else:
                l=l.brother
                
    def show(self):
        print('this b+tree is:\n')
        q=collections.deque()
        h=0
        leaf_count=0
        q.append([self.root,h])
        while True:
            try:
                node,height=q.popleft()
            except IndexError:
                return
            else:
                if not node.isleaf():
                    print(str(node.keylist),'height: '+str(height))
                    if height==h:
                        h+=1
                    q.extend([[i,h] for i in node.sonlist])
                else:
                    leaf_count += 1
                    print('leaf'+str(leaf_count)+": "+str([v.key for v in node.valuelist]))
    
    def search(self,mi):
        node=self.root
        def search_key(n,k):
            if n.isleaf():
                p=bisect.bisect_left(n.valuelist,k)
                return (p,n)
            else:
                p=bisect.bisect_right(n.keylist,k)
                return search_key(n.sonlist[p],k)
        
        i,l=search_key(node,mi)
        try:
            if l.valuelist[i].key==mi:
                return l.valuelist[i]
        except:
            return None
    
    
if __name__=='__main__':
    testlist=[]
    for i in range(1,10):
        key=i
        value=i
        testlist.append(KeyValue(key,value))
    mybptree=Bptree(3,3)
    for kv in testlist:
        mybptree.insert(kv)
    mybptree.show()
    print('\nkey of this b+tree is \n')
    print(set([kv.key for kv in mybptree.traversal()]))
    print(mybptree.search(5))
    
    
    
    
    