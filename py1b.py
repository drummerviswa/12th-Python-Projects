n = int(input("enter a value of n:"))
s = 0
for i in range(1,n+1):
    a=(i**i)/i
    s=s+a
print("the sum of the series is",s)