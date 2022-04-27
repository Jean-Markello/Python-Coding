def tower_builder(n_floors):
    #Build here
    list=[]

    #Create a 2D list whith a certain number of "*":
    for i in range(n_floors):
        j=i+1
        list.append(["*"]*j*2)
        if "*" in list[i]:
            del list[i][0]

    #Adding space a certain amount of space at each extremities of element in list:
    for b, v in zip(range(len(list)), range(len(list)-1,-1,-1)):
        if v<(len(list)-1):
            list[v].insert(0, " "*b)
            list[v].insert(len(list[v]), " "*b)
    
    #Join each element (spaces and "*") in list to a new list:
    list2=[]
    for x in list:
        list2.append("".join(x))
    
    return list2

a=tower_builder(7)
for x in a:
    print(x)
