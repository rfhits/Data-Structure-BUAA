#复习的时候写的
def gen_next(pat):
    k, i, l = 0, 1, len(pat)
    next = [0]*l
    if l == 0:
        return False
    while i < l:
        if pat[i] == pat[k]:
            k += 1
            next[i] = k
            i += 1
        else:
            if k == 0:
                next[i] = 0
                i += 1
            else:
                k = next[k]
    return [-1] + next[0:-1]