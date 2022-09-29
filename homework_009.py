# напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N,N]. Найдите произведение элементов на указанных позициях(не индексах)

import random

def generator():
    N = random.randrange(1, 11)
    new_list = []
    for i in range(-N, N+1):
        new_list.append(i)
    return new_list

def product_of_numbers(new_list):
    while True:
        try:
            position_one = int(input("Введите номер первой позиции: ")) -1
            position_two = int(input("Введите номер второй позиции: ")) -1
        except ValueError:
            print("Введенный символ не является номером позиции")
            continue
        if position_one >= len(new_list) or position_two >= len(new_list): 
            print("Введенный номер позиции больше длины списка")
            continue
        return new_list[position_one]*new_list[position_two]
    



new_list = generator()
print(new_list)
print(product_of_numbers(new_list))


