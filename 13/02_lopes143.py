def junta_ordenadas(lst1, lst2):
    if len(lst1)==0 or len(lst2)==0:
        return lst1+lst2
    
    elif lst1[0]<lst2[0]:
        return [lst1[0]]+junta_ordenadas(lst1[1:], lst2)
    
    else:
        return [lst2[0]]+junta_ordenadas(lst1, lst2[1:])
    
print(junta_ordenadas([2, 5, 90], [3, 5, 6, 12]))