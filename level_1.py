


a = [10,6,35,2,12,24,25,16]

def merge_sort(a):
    if len(a) < 2:
        return a[:]
    else:
        median = int(len(a)/2)
        left = merge_sort(a[:median])
        right = merge_sort(a[median:])
        res = merge(left,right)
        return res

def merge(left,right):
    l = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i +=1
    while j < len(right):
        l.append(right[j])
        j +=1
    return l

res = merge_sort(a)
print (res)





