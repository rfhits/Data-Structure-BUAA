# 此乃非递归的中序遍历

# node非空，因为是中序，
# 所以要压栈，再往左走

stack = []  # stack既是未访问的节点，也是要回退的节点
res = []

def isN(node):
    ''''判断一个node是不是空结点'''
    return 

def tra(node):
    t = node
    while (not isN(t)) or stack:
        if not isN(t):
            stack.append(t)
            t = t.left
        else:
            t = stack.pop()
            res.append(t.data)
            t = t.right
