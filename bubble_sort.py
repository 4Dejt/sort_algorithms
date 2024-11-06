from random import randint, seed

seed(123)
n = 20
# T = []
# for _ in range(n):
#     T.append(randint(-1000, 1000))

T = [randint(-100, 100) for _ in range(n)]

print(T)
T = [6, 1, 8, 4, 10, 10, 5, 14, 2]
def LO31_bubble_sort(A, n):
    for i in range(n-1):
        flag = True
        for j in range(n-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = False
        if flag:
            break

LO31_bubble_sort(T, len(T))
print(T)

def bubble_sort(T, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
    print('Sorted array: ', T)

bubble_sort(T, n)