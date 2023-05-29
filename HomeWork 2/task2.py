import math

def solve_equations(S, P):
    discriminant = S**2 - 4*P
    
    if discriminant < 0:
        return None
    
    x = (S + math.sqrt(discriminant)) / 2
    y = (S - math.sqrt(discriminant)) / 2
    
    return x, y

S = int(input("Введите число S: "))
P = int(input("Введите число P: "))

result = solve_equations(S, P)
if result is not None:
    x, y = result
    print(f"X = {int(x)}, Y = {int(y)}")
else:
    print("Решений нет")

