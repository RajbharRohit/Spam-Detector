# Merge sort

A = [15, 28, 46, 60]
B = [12, 25, 40, 70]

m = []

i = 0
j = 0

while i < len(A) and j < len(B):
    if A[i] < B[j]:
        m.append(A[i])
        i += 1
    else:
        m.append(B[j])
        j += 1

while i < len(classA):
    m.append(A[i])
    i += 1

while j < len(classB):
    m.append(B[j])
    j += 1

print("Merged List:")
print(m)
