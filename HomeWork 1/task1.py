#Найдите сумму цифр трехзначного числа.

number = int(input("Введите ваше число: "))
summ = 0
while number > 0:
    i = number % 10
    number = int(number / 10)
    summ = summ + i

print(f"Сумма цифр в вашем числе = {summ}")
