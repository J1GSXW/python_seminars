# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
# 1   1   1   1
# 2   4   8  16
# 3   9  27  81
# 4  16  64 256
# print_operation_table(lambda x,y: x*y)
# 1   2   3   4   5   6
# 2   4   6   8  10  12
# 3   6   9  12  15  18
# 4   8  12  16  20  24
# 5  10  15  20  25  30
# 6  12  18  24  30  36
# (*) Усложнение. Сформируйте форматированный вывод с номерами строк и столбцов
# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
#        1   2   3   4
#     ----------------
# 1 |    1   1   1   1
# 2 |    2   4   8  16
# 3 |    3   9  27  81
# 4 |    4  16  64 256

# print_operation_table(lambda x,y: x*y)
#        1   2   3   4   5   6
#     ------------------------
# 1 |    1   2   3   4   5   6
# 2 |    2   4   6   8  10  12
# 3 |    3   6   9  12  15  18
# 4 |    4   8  12  16  20  24
# 5 |    5  10  15  20  25  30
# 6 |    6  12  18  24  30  36



def print_operation_table(operation, num_rows=6, num_columns=6):
    print(f"   ", end="")
    for column in range(1, num_columns + 1):
        print(f"{column:4}", end="")
    print()
    print("   " + "-" * (4 * num_columns))
    for row in range(1, num_rows + 1):
        print(f"{row:2} |", end="")
        for column in range(1, num_columns + 1):
            value = operation(row, column)
            print(f"{value:4}", end="")
        print()


print_operation_table(lambda x, y: x ** y, 4, 4)
print()
print_operation_table(lambda x, y: x * y)
