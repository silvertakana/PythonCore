import random
A = [random.randint(0,1e3) for i in range(0,10)]

counter = 0
for j in range(0,len(A)):
    for i in range(0,len(A)):
        if A[i] > A[j] and i < j:
            counter += 1
print(A)
print(counter)
