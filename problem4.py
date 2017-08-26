def second_largest(arr):
    
    arr.remove(max(arr))
    return(max(arr))

print second_largest([46,5,1,3])