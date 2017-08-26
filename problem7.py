from random import randint

def dup_items(arr):
    dup_one_time = []
    new_arr = list(set(arr))
    for i in range(len(new_arr)):
        num = arr.count(new_arr[i])
        if num == 1:
            dup_one_time.append(new_arr[i])
    return dup_one_time

array = []
for i in range(101):
    array.append(randint(1,101))

print dup_items(array)
