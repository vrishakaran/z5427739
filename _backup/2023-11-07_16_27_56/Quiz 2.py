date = '10-10-2020'
mins = 90

print(f"The exams date is {date} you will have {mins} minutes")
print("The exams date is {} you will have {} minutes".format(date,mins))

print('    some text    '.strip(' '))

w = "What"
i = "IS"
c = "CamelCase?"



a = 'this is called'
b = 'problem'
a = f'{a} Parsons {b}'



x=5
y=5


l = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')


(b, s, i) = (True, 'string', 1)

dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})


tup = (1, 2, ('a', 'b'))
dic = {tup: 'value'}

# (put your answer below)
current = 21 # at this point, the 9th element of the sequence
last = 13 # at this point, the 8th element of the sequence
# Now, use parallel assignment to replace the value of `current` and `last`
# (put your answer below)
tupple = (last, current, current+last)
current = tupple[-1]
last = tupple[-2]

list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol = list_a[1:7]
sol.remove(sol[2])
sol.append('including')
sol.insert(2,"good")
sol.extend(list_b)
print(sol)
