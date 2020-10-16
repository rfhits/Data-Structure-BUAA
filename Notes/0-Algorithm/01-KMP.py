def get_prefix(a):
    pat = list(a)
    prefix = [0, ]
    i = 1
    l = 0
    while(i < len(pat)-1):
        if(pat[i] == pat[l]):
            l += 1
            prefix.append(l)
            i += 1
        else:
            l = prefix[l]
            if(l == 0):
                prefix.append(0)
                i += 1
    prefix.insert(0, -1)
    return prefix


def KMP_search(text, pat):
    list_match = []
    prefix = get_prefix(pat)
    i, j = 0, 0
    while(i <= len(text) and j <= len(pat) and (len(pat)-j) <= (len(text)-i)):
        if(j == len(pat)):
            list_match.append(i-j)
            j = prefix[j-1]
        if(i == len(text)):
            break
        if (text[i] == pat[j]):
            i += 1
            j += 1
        else:
            if(j == 0):
                i += 1
            else:
                j = prefix[j]
                if(j == -1):
                    j = 0
    return list_match


match = KMP_search("ababcabcab", 'abc')
print(match)
