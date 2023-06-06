# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры
# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку
# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

string_1 = '2 4 6 8 10 12 10 8 6 4 2'
string_2 = '3 6 9 12  15 18'
string_3 = '3 9 12 15 18'
string_4 = '2 4 6 8 10 10 8 6 4 2'

def duplicate_num_found(string1: str, string2: str) -> None:
    result_list = []
    split_str_1 = string1.split()
    split_str_2 = string2.split()
    for item in split_str_1:
        if item in split_str_2 and item not in result_list:
            result_list.append(item)

    if result_list == []:
        print("Повторений нет")
    else:
        print(*result_list)


duplicate_num_found(string_1, string_2)
duplicate_num_found(string_3, string_4)


