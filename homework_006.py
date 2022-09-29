# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

import random

value = str(round(random.uniform(0.0, 100.0), 4))
print(value)
sum_1 = 0
for i in value:
    if i.isdigit() == True: sum_1+=int(i)
print(sum_1)