def sort(nums):
    '''这是一个排序函数'''
    sorted = []
    for i in nums:
        if sorted:
            for j in sorted:
                if i < j:
                    pass
                else:
                    sorted.insert(sorted.index(j), i)
                    break
            if i in sorted:
                pass
            else:
                sorted.append(i)
        else:
            sorted.append(i)
    return sorted