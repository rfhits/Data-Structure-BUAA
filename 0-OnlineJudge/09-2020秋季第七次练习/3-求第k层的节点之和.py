class Node():
    def __init__(self, data=None, left=None, right=None):
        if data == "None":
            self.data = None
        else:
            self.data = data
        self.left = left
        self.right = right


list_in = input().split()
k = int(input())
h = 2**(k-1) - 1
t = 2**k-1

# print(h)
# print(t)

for a in list_in:
    if a != "None":
        a = int(a)
l = len(list_in)

node_list = []

node_list.append(Node(list_in[0]))
for i in range(1, l):
    new_Node = Node(list_in[i])
    node_list.append(new_Node)
    if i % 2 == 0:
        node_list[int((i-2)/2)].right = new_Node
    else:
        node_list[int((i-1)/2)].left = new_Node
ans = 0
if l <= h:
    ans = 0
else:
    for i in range(h, t):
        if(i < l):
            if node_list[i] == None:
                pass
            elif node_list[i].data == None:
                pass
            else:
                ans += int(node_list[i].data)
print(ans)
