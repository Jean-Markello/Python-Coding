"""strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
"""


def longest_consec(strarr, k):

    #condition for the instruction to work, else return ""/blank
    if len(strarr)>0 and k>0 and k<len(strarr):

        list=[]
        b=""
        
        # concatanate the string k number of time (k=2 / strarr[0]+strarr[1], (strarr[1]+strarr[2]) and so forth
        for i in range(len(strarr)-(k-1)):
            for x in range(k):
                b+=strarr[x+i]
            list.append(b)
            b=""
        
        #Find max lenght of concatanate string  
        max=len(list[0])
        store=list[0]
        for v in range(len(list)):
            if max<len(list[v]):
                max=len(list[v])
                store=list[v]

        # return its value
        return store
    else:
        return ""

#concatenate string in list k number of time, then find lenght of e
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)) #"abigailtheta"
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)) # "oocccffuucccjjjkkkjyyyeehh"
print(longest_consec([], 3)) # ""
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)) #"wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)) # "wlwsasphmxxowiaxujylentrklctozmymu"
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)) # ""
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)) # "ixoyx3452zzzzzzzzzzzz"
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15)) # ""
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0)) # ""