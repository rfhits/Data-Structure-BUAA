leaf1=[]
leaf2=[]
class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def travelsal_1(node):
    if node==None:
        return
    elif node.data=="None":
        return
    travelsal_1(node.left)
    if ((node.left == None) or (node.left.data == 'None')) and ((node.right == None) or (node.right.data == 'None')):
        leaf1.append(node.data)
    travelsal_1(node.right)




def travelsal_2(node):
    if node==None:
        return
    elif node.data=="None":
        return
    travelsal_2(node.left)
    if ((node.left == None) or (node.left.data == 'None')) and ((node.right == None) or (node.right.data == 'None')):
        leaf2.append(node.data)
    travelsal_2(node.right)



in_1 = input().split()
Node_list_1 = []
n = len(in_1)

Node_list_1.append(Node(in_1[0]))
for i in range(1, n):
    new_Node = Node(in_1[i])
    Node_list_1.append(new_Node)
    if i % 2 == 0:
        Node_list_1[int((i-2)/2)].right = new_Node
    else:
        Node_list_1[int((i-1)/2)].left = new_Node

travelsal_1(Node_list_1[0])

for i in leaf1[:]:
    if i == "None":
        leaf1.remove(i)

# print(leaf1)

in_2 = input().split()
Node_list_2 = []
for a in in_2:
    if a != "None":
        a = int(a)
n = len(in_2)

Node_list_2.append(Node(in_2[0]))
for i in range(1, n):
    new_Node = Node(in_2[i])
    Node_list_2.append(new_Node)
    if i % 2 == 0:
        Node_list_2[int((i-2)/2)].right = new_Node
    else:
        Node_list_2[int((i-1)/2)].left = new_Node

travelsal_2(Node_list_2[0])

for i in leaf2[:]:
    if i == "None":
        leaf2.remove(i)


# print(leaf2)




print(leaf1 == leaf2)
