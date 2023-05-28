# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

number_s = int(input("Введите общее число журавликов: "))

def paper_cranes_count(number_s):
    x = number_s / 6
    petia = x
    katia = 2 * number_s / 3
    sereja = x
    return petia, katia, sereja

result = (paper_cranes_count(number_s))
print(f"Петя сделал {int(result[0])} журавликов")
print(f"Катя сделала {int(result[1])} журавликов")
print(f"Сережа сделал {int(result[2])} журавликов")
