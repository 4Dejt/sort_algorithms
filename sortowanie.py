from random import randint, seed

seed(123)
n = 15

T = [randint(2,5) for _ in range(n)]

print(T)
print(sorted(T))

def counting_sort(A):
    min_v = min(A)
    max_v = max(A)

    # tablica liczników
    count = [0]