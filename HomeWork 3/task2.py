# Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.
# Если в списке несколько чисел "равноблизких" к заданному числу X, то выводим первое встретившееся.

# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10
# (*) Усложнение. Если в списке несколько чисел "равноблизких" к заданному числу X, выводим все числа в отсортированном виде (по возрастанию)

x = int(input("Введите ваше число: "))
array = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]

def find_closest_numbers_sorted(numbers, X):
    closest_numbers = []
    min_diff = None

    for num in numbers:
        diff = num - X
        if diff < 0:
            diff = -diff
        if min_diff is None or diff < min_diff:
            min_diff = diff
            closest_numbers = [num]
        elif diff == min_diff:
            closest_numbers.append(num)

    closest_numbers.sort()
    return closest_numbers

print(*find_closest_numbers_sorted(array, x))