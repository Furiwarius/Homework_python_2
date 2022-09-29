# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

from multiprocessing.sharedctypes import Value
import random

def generator():
    random_number = random.randrange(5,20)
    new_list = []
    for i in range(1, random_number+1):
        value = round((1+1/i)**i)
        new_list.append(value)
    return new_list

new_list = generator()
print(new_list)
print(sum(new_list))