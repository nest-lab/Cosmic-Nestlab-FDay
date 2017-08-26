def is_anagram(s1,s2):
    a = len(s1)
    b = len(s2)
    if a == b:
        for l in s1:
            if l in s2:
                return True
    return False

string_1 = raw_input("Enter any string: ")
string_2 = raw_input("Enter any string: ")

print is_anagram(string_1, string_2)