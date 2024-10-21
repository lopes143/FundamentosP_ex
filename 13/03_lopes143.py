def sublistas(lst):
    if len(lst)==0:
        return 0
    elif isinstance(lst[0], list):
        return 1+sublistas(lst[0])+sublistas(lst[1:])
    else:
        return sublistas(lst[1:])
    
print(sublistas([[1], 2, [3]]))
print(sublistas([[[[[1]]]]]))
print(sublistas(['a', [2, 3, [[[1]], 6, 7], 'b']]))