num = input("Enter a Number: ")

list_no = list(str(num))

for i in list_no:
    solve = int(i)**3
    solve+=solve

if solve == num:
    print(solve, "it is an amstrong number")
else:
    print(solve, "It is not an amstrong number")