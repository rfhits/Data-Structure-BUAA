leaf_1=[]
leaf_2=[]
# useing 

class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def input_tree(node_list):
    ''' input the data by the layer, make a tree, the root is stored in node_list[0]'''

    input_list=input().split()
    l= len(input_list)
    node_list.append(Node(input_list[0]))
    for i in range(1,l):
        if input_list[i] == "None":
            node_list.append(None)
        else:
            node = Node(input_list[i])
            node_list.append(node)
            if i%2 == 1:
                k=(i-1)//2
                while(node_list[k]==None):
                    k+=1
                node_list[k].left=node
            else:
                k=(i-2)//2
                while(node_list[k]==None):
                    k+=1
                node_list[k].right=node

def leafa(node):
    if node == None:
        return
    if (node.left == None) and (node.right == None): # 若是叶子，则无再leaf的必要
        leaf_1.append(node.data)
    leafa(node.left)
    leafa(node.right)

node_list_1=[]
node_list_2=[]
input_tree(node_list_1)
input_tree(node_list_2)
leafa(node_list_1[0])
print(leaf_1)
