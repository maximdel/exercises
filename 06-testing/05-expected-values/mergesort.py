def split_in_two(ns):
    half = len(ns) // 2 
    ns1 = ns[:half]
    ns2 = ns[half:]
    return (ns1, ns2)

def merge_sorted(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(ns):
    if len(ns) <= 1:
        return ns
    left, right = split_in_two(ns)
    sort_left = merge_sort(left)
    sort_right = merge_sort(right)
    return merge_sorted(sort_left, sort_right)