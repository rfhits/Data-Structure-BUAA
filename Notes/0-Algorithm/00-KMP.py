# 只给出第一次匹配到的地方
def gen_next(pat):
    """
    gennerate pattern string's next
    """
    i, k, m = 0, -1, len(pat)
    next = [-1] * m
    while i < m-1:
        if k == -1 or pat[i] == pat[k]:
            i, k = i + 1, k + 1
            if pat[i] == pat[k]:
                next[i] = next[k]
            else:
                next[i] = k
        else:
            k = next[k]
    return next


def KMP_search(text, pat):
    i, j = 0, 0
    n, m = len(text), len(pat)
    next = gen_next(pat)
    while(i < n and j <= m):
        if(text[i] == pat[j] or j == -1):
            i += 1
            j += 1
        else:
            j = next[j]
    if(j == m):
        return i-j
    else:
        return -1


print(KMP_search('aaababc', 'ababc'))
