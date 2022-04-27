# Programme pour vérifier les nombres cubes dans un certain intervalle

lower = 100
upper = 499

for num in range(lower, upper + 1):

    order = len(str(num))
    
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        num = str(num)
        print(num, " = ", num[0], " **3 + ", num[1], " **3 + ", num[2], " **3 = ", (int(num[0]))**3, " + ", (int(num[1]))**3, " + ", (int(num[2]))**3)
       



