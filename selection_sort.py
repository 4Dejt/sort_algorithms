from random import randint, seed

seed(123)
n = 20

T = [randint(-1000, 1000) for _ in range(n)]


def selection_sort(A, n):
    for i in range(n-1):
        k = i
        for j in range(i+1, n):
            if A[j] < A[k]:
                k = j
        A[i], A[k] = A[k], A[i]

print(T)
selection_sort(T, len(T))
print(T)