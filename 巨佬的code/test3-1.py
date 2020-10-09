# 优秀的类
class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
n = int(input())
i = 0
my_stack = Stack()
while i < n:
    my_stack.push(input())
    i += 1
m = int(input())
i = 0
store = []
while i < m:
    str = input().split()
    if str[0] == 'A':
        my_stack.push(str[1])
    if str[0] == 'B':
        try:
            store.append(my_stack.pop())
        except:
            print('No')
            while len(store)!=0:
                store.pop()
            break
    i += 1
print(' '.join(store))
i = len(my_stack.items)
while i > 0:
    print(my_stack.pop(),end=' ')
    i -= 1