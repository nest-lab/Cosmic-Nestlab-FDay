arr_1 = [1,2,3,4,5]
arr_2 = [2,3,1,0,5]

def item_not_find_in_2nd_arr(arr_1, arr_2):
    not_found = []
    for x in arr_1:
        if x not in arr_2:
            not_found.append(x)
    return not_found

print item_not_find_in_2nd_arr(arr_1, arr_2)