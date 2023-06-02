# def calc_profit(x ,y, z):
#     if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
#         a = x + y + z
#         b = 1
#         return a
#     else:
#         raise TypeError

# # # calc_profit(1,2,3 + 3 ** 4)

# # def func(*args, **kwargs):
# #     print(args)
# #     print(kwargs)

# # func(1,2,3,x=3,y=78,q=988)
# # func(1,2,3)
# # func(x=3,y=78,q=988)

# c = calc_profit(1,2,3)
# v = calc_profit("1","2","3")
# print(v)
# print(c)

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите функцию, которая заменяет оценки, переданные в виде списка, но наоборот: все максимальные – на минимальные.
# Функция должна возвращать новый список оценок
# Примечание: Обратите внимание на side effects функции.
# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]
# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None
# Примеры/Тесты:
# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None
# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:
# Друзьям минимальные на максимальные, Врагам - наоборот.
# Примеры/Тесты:
# grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "friend") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "enemy") -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

# def rating_replace(grades):
#     new_grades = grades.copy()
#     max_grades = max(new_grades)
#     min_grades = min(new_grades)
#     if max_grades == min_grades: return None
#     for i,item in enumerate(new_grades):
#         if item == max_grades:
#             new_grades[i] = min_grades
#     return new_grades


# num = [3, 3, 3, 3, 3, 3, 3, 3, 3]
# print(num)
# gr = rating_replace(num)
# print(num)
# print(gr)

# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# https://ru.wikipedia.org/wiki/Числа_Фибоначчи
# Требуется найти N-е число Фибоначчи. Напишите рекурсивную функцию. Обратите внимание, что функция должна возвращать число.
# Примеры/Тесты:
# <function_name>(0) -> 0
# <function_name>(2) -> 1
# <function_name>(9) -> 34

# def Fibonacci(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return Fibonacci(x-2) + Fibonacci(x-1)
    
# print(Fibonacci(50))


# №5.3[35]. Напишите функцию, которая принимает число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя нацело: 1 и само число
# Если число простое - функция возвращает True, если нет - возвращает False
# Примеры/Тесты:
# <function_name>(13) -> True
# <function_name>(10) -> False

# def simple_num(number:int):
#     if not isinstance(number, int):
#         return "Error"
#     for devider in range(2,number//2 + 1):
#         if number % devider == 0:
#             return False
#     return True

# print(simple_num("10"))


# Напишите функцию, которая принимает натуральное число n, в теле функции считывает (input) 
# последовательность из n элементов
# Возвращает эту последовательность в виде строки в обратном порядке
# Примеры/Тесты:
# <function_name>(5) 1 2 3 4 5 -> '5 4 3 2 1'
# <function_name>(3) 8 7 9 -> '9 7 8'
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

def sequence(n:int) -> str:
    digit = input("Введите ваше число: ")
    if n == 1:
        return digit + ' '
    return sequence(n-1) + digit + ' '

print(sequence(5))