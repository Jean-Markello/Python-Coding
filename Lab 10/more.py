"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.
"""

def is_isogram(string):
    #your code here
    for x in range(len(string)):
        b=string.count(string[x])
        c=string.count((string[x].upper()))
        v=string.count((string[x].lower()))
        if b>1 or (b==c and b==v):
            return False
    return True


print(is_isogram("Dermatoglyphics")) #True
print(is_isogram("isogram")) # True 
print(is_isogram("aba")) # False, "same chars may not be adjacent"
print(is_isogram("moOse")) # False, "same chars may not be same case"
print(is_isogram("isIsogram")) #False 
print(is_isogram("")) # True, "an empty string is a valid isogram"