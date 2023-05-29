def powers_of_two(N):
    power = 0
    result = []
    
    while 2**power <= N:
        result.append(2**power)
        power += 1
    
    return result

n = int(input("Введите ваше число N: "))
powers = powers_of_two(n)
print(*powers)