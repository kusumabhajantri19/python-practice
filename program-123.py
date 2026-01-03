
#find element -wise product of two arrays.

A = [1, 2, 3, 4]
B = [5, 6, 7, 8]

C = []  

for i in range(len(A)):
    C.append(A[i] * B[i])

print("Element-wise product:", C)