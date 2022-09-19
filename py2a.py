def oddeven(a):
    if a%2==0:
        return "EVEN"
    else:
        return "ODD"
num = int(input("Enter a number: "))
print("The given number is ",oddeven(num))