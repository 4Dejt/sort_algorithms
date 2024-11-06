from random import randint, seed

seed(123)
n = 20

T = [randint(-1000, 1000) for i in range(n)]

def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(float('inf')) # wstawienie wartowników
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A,q + 1, r)
        merge(A,p,q,r)
    return A

# array = [5, 1, 3, 4, 2, 10, 14, 11, 9, 12]
print(T)
merge_sort(T, 0, len(T)-1)
print(T)