# Требуется определить, можно ли от шоколадки размером
# n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

def can_break_chocolate(n, m, k):

    if k > n * m:
        return False

    if k == n * m:
        return False

    if k % n == 0 or k % m == 0:
        return True
    
    return False

n = int(input("Введите число долек по вертикали: "))
m = int(input("Введите число долек по горизонтали: "))
k = int(input("Введите количество долек которые нужно отломить: "))
result = can_break_chocolate(n, m, k)
if result:
    print("Разломить получится")
else:
    print("Разломить не получится")