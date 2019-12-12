# 1 (1)
a = [29, 36.6, 'hello', True, "world!"]
print(a)
print(type(a))

for i in range(len(a)):
    print(type(a[i]))
    print(a[i])

# 1 (2)
a = [29, 36.6, 'hello', True, "world!"]
print(a)
print(type(a))
p = dict()
for i in range(len(a)):
    p[i] = type(a[i])
print(p)

# 1 (3)
a = [29, 36.6, 'hello', True, "world!"]
print(a)
print(type(a))
p = dict()
for i, item in enumerate(a):
    print(f"{i}) {item} - {type(item)}")

# 2
my_list = input('Вводите элементы через пробел\n').split()
i = 0
while i + 1 < len(my_list):
    if i % 2 == 0:
        my_list.insert(i, my_list.pop(i + 1))
    i += 1

print(f'Измененный список {my_list}')


# 3
seasons_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
season = int(input('Введите номер месяца\n'))

for i in range(len(seasons_list)):
    if season == i+1:
        if 3 <= season <= 5:
            print(f'Сейчас весна, месяц - {seasons_list[i]}')
        elif 6 <= season <= 8:
            print(f'Сейчас лето, месяц - {seasons_list[i]}')
        elif 9 <= season <= 11:
            print(f'Сейчас осень, месяц - {seasons_list[i]}')
        else:
            print(f'Сейчас зима, месяц - {seasons_list[i]}')

# 4 (1)
string = (input('введите строку из нескольких слов, разделённых пробелами\n').split())
print(string)

for i in range(len(string)):
    if len(string[i]) <= 10:
        print(i, string[i])
    else:
        print(i, string[10])

# 4(2)
string = (input('введите строку из нескольких слов, разделённых пробелами\n').split())
for i, word, in enumerate(string, 1):
    print(f'{i} {word[:10]}')

# 5
my_list = [7, 5, 3, 3, 2]

while True:
    print(f'Текущий рейтинг: {my_list}')
    number = input('Введите новый элемент рейтинга\n Или 007 для выхода\n')
    if number.isdigit() and number != '007':
        number = int(number)
        if my_list.count(number):
            my_list.insert(my_list.index(number) + my_list.count(number), float(number))
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number > i:
                    my_list.insert(n, number)
                    break
                else:
                    my_list.append(number)
    elif not number.isdigit():
        print('введите число')
    else:
        break

# 6
goods = []
features = {'название': '', 'цена': '', 'кол-во': '', 'ед.изм.': ''}
analytics = {'название': [], 'цена': [], 'кол-во': [], 'ед.изм.': []}
num = 0
while True:
    if input('Для выхода нажмите Q, Enter - для продолжения:').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        _ = input(f'Введите значение свойства "{f}": ')
        features[f] = _ if (f == 'цена' or 'кол-во') else _
        analytics[f].append(features[f])
    goods.append((num, features))
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print("*" * 30)
