def coder(s):
    s2=""
    for i in range(0, len(s),2):
        s2 +=(s[i+1] if i+1 <len(s) else"") + s[i]
    return  s2

s=input("donner une chaine: ")
print(coder(s))