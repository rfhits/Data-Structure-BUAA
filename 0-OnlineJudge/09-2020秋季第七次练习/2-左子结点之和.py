class Node():
    def __init__(self, data=None, left=None, right=None):
        if data == "None":
            self.data = None
        else:
            self.data = data
        self.left = left
        self.right = right


list_in = input().split()

for a in list_in:
    if a != "None":
        a = int(a)
n = len(list_in)

node_list = []

node_list.append(Node(list_in[0]))
for i in range(1, n):
    new_Node = Node(list_in[i])
    node_list.append(new_Node)
    if i % 2 == 0:
        node_list[int((i-2)/2)].right = new_Node
    else:
        node_list[int((i-1)/2)].left = new_Node

ans = 0

for i in node_list:
    if i.left == None:
        pass
    elif i.left.data == None:
        pass
    else:
        ans = ans + int(i.left.data)

print(ans)
