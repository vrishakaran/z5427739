def process_string(s):
    s = s.lower()
    list_a = s.split()
    list_b = []
    for i in range(len(list_a)):

        if i % 2 == 0:
            list_b.append(list_a[i].lower())
        else:
            list_b.append(list_a[i].upper())

    return list_b


print(process_string("This is my test String"))


def fizz_buzz_sumz(i):
    s = 0
    if i > 0:

        for x in range(0,i+1):

            if x % 3 == 0 and x % 5 != 0:

                s += x*3


            elif x % 5 == 0 and x % 3 != 0:

                s += x*5


            elif x % 5 == 0 and x % 3 == 0:

                continue

            else:
                s += x

    return print(s)

fizz_buzz_sumz(10)

def my_function(x):
    x = x + 1
    return x

x = 3
x = my_function(x)
print(x)


prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# replace '???' with the correct expression
sorted_keys = list(sorted(prc_dic.keys()))
print(sorted_keys)

prc_dic= {k.replace('3000-01-15','2020-01-15', ): v for k, v in prc_dic.items()}

print(prc_dic)

print('The copyright symbol is:\u00A9')

print('he copyright symbol has Unicode hex value: \\u00A9')






