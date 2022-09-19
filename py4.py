odd = set([x for x in range(1,11) if x%2 != 0])
prime = set()
for i in range(2,10):
    f = 1
    for j in range(2,i):
        if i%j == 0:
            f = 0
            break
    if f == 1:
        prime.add(i)

print("Odd numbers: ", odd)
print("Prime numbers: ", prime)
print("Union: ", odd.union(prime))
print("Intersection: ", odd.intersection(prime))
print("Difference: ", odd.difference(prime))
print("Symmetric difference: ", odd.symmetric_difference(prime))