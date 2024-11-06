def quick_sort(array):
    if len(array) < 2:
        return array # <- przypadek podstawowy (z góry posortowane pojedyncze elementy)
    else:
        pivot = array[0] # <- element osiowy
        less = [i for i in array[1:] if i <= pivot] # <- podtablica z elementami mniejszymi od elementu osiowego
        greater = [i for i in array[1:] if i > pivot] # <- podtablica z elementami większymi od elementu osiowego
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 5, 2, 3]))

def quick_sort_2(A, p, r):
    if p > r:
        q = A[p]
        s = p
        for i in range(p+1, r+1):
            if A[i] < q:
                s += 1
                A[s], A[i] = A[i], A[s]
        A[s], A[p] = A[p], A[s]
        quick_sort(A, p, s-1)
        quick_sort(A, s+1, r)

print(quick_sort_2([10,5,2,3]))