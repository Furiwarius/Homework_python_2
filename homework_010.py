# Реализуйте алгоритм перемешивания списка.

import random

def generator():
    new_list = []
    for i in range(1, 11): new_list.append(i)
    return new_list

def search(l, value):  
    for n, i in enumerate(l):
        if value==i: return n

def mixing(l):
    count_l=l
    new_list=[]
    for i in range(len(l)):
        count = count_l[random.randrange(0,len(count_l))]
        new_list.append(count)
        del(count_l[search(count_l, count)])
    return new_list

random_list = generator()
print(f"отсортированный список - {random_list}")
new_list = mixing(random_list)
print(f"перемешанный список - {new_list}")

