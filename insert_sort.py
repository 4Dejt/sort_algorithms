def insert_sort(array, n):
    for i in range(1, n):
        x = array[i] # 'wyciągnięcie' elme
        j = i-1
        while j >= 0 and array[j] > x: # szukamy miejsca do wstawienia elementu
            array[j+1] = array[j]
            j -= 1
        array[j+1] = x # wstawienie elementu x
    print(array)

array = [3, 1, 2, 4, 0]
insert_sort(array, len(array))

def insert_sort_2(array, n):
    array.insert(0, '#')
    for i in range(2, n+1):
        x = array[i]
        array[0] = x
        j = i - 1
        while x < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = x
    print(array)

array = [3, 1, 2, 4, 0, 6, 5, 3, 10, 9]
insert_sort_2(array, len(array))