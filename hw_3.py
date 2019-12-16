# # 1
#
# def div(s_1, s_2):
#     try:
#         s_1, s_2 = int(s_1), int(s_2)
#         div_num = s_1 / s_2
#     except ValueError:
#         return "Введите число"
#     except ZeroDivisionError:
#         return 'Делить на ноль нельзя'
#     return div_num
#
#
# print(div(input('Введите первое число - '), input('Введите втрое число - ')))
#
#
# # 2
# def personal_info(**kwargs):
#     return kwargs
#
#
# print(personal_info(name=input('Введите своё имя: '), surname=input('Введите свою фамилию: '),
#                     birthday=input('Введите свой день рождения: '), email=input('Введите свой email: '),
#                     phone_number=input('Введите свой телефон: ')))

# 3
# def my_func(arg1, arg2, arg3):
#     return sum(sorted([arg1, arg2, arg3])[1:])
# print(my_func(1, 2, 3))
#
# # 4
# def my_pow_fun(x, y):
#     try:
#         res = x ** y
#     except TypeError:
#         return 'Введите действительное положительное число X и целое отрицательное число Y'
#     return res
# print(my_pow_fun(3.7, -2))

# 5
# def summary():
#     ex = False
#     fresult = 0
#     while ex == False:
#         lNumbers = input('Вводите числа, разделяя пробелом (для выхода введите q):\n').split()
#         result = 0
#         for i in range(len(lNumbers)):
#             if lNumbers[i] == 'q':
#                 ex = True
#                 break
#             else:
#                 result = result + int(lNumbers[i])
#         fresult = fresult + result
#         print(f'Текущая сумма равна {fresult}')
#     print(f'Вы вышли, общая сумма равна {fresult}')
#
# summary()

# 6
int_func = lambda sentence: print(sentence.title())

int_func(input('Введите слово:\n'))
