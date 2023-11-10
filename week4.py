l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]

def even_in_list(t):
    even_l = list()
    for i in t:
        if i % 2 == 0:
            even_l.append(i)
        else:
            continue
    return print(even_l)

even_in_list(l)

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]

even_lst = [i for i in lst if i**2 > 150]

print(even_lst)

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]

even_numbers = list({i for i in numbers if i % 2 == 0})
even_numbers.sort()

print(even_numbers)
