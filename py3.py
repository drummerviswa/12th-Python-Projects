num = []
for i in range(1,11):
    num.append(i)
print("Numbers from 1 to 10: .... \n", num)
for i in num:
    if (i%2 == 0):
        num.remove(i)
print("The value after removing odd numbers \n", num)