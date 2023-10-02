number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

while number_1 != 0 and number_2 != 0:
    if number_1 > number_2:
        number_1 = number_1 % number_2
    else:
        number_2 = number_2 % number_1

print(number_1 + number_2)