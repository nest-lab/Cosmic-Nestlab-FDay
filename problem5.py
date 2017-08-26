from itertools import permutations

#using iteration
input_word = raw_input("Enter any string you know: ")
perms = [''.join(p) for p in permutations(input_word)]

print "by iteration", perms

#using recursion
def perms_with_recursion(s):        
    if(len(s)==1): 
        return [s]
    result=[]
    for i,v in enumerate(s):
        result += [v+p for p in perms_with_recursion(s[:i]+s[i+1:])]
    return result

print "by recursion", perms_with_recursion(input_word)
