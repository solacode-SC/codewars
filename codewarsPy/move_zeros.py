def move_zeros(lst):
    
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == 0:
            lst.remove(lst[i])
            lst.append(0)
    
    return lst


print(move_zeros([1,2,0,1,0,1,0,3,0,1]))