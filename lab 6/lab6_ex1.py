def compteV1(s,c):
    return s.count(c)

def comptev2(s,c):
    count =0
    for x in s:
        if x ==c:
            count=count+1
    return count

s= input("SVP donner une chaome de charactère: ")

print("l'occurence de", "a", "dans", s, "est", compteV1(s,"a"))
print("l'occurence de", "a", "dans", s, "est", comptev2(s,"a"))
