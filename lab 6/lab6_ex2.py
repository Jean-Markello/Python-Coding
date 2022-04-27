def espaces(s):
    s2=""
    for c in s:
        s2 += c+ " "
    print(s2)
    s2=s2[:-1]
    return s2

s=input("SVP donner une chaine de charactere: ")
print(espaces(s))
