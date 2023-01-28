# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

# def check_prime(a):
#     count = 0
#     if a == 2:
#         return True
#     else:
#         for i in range(2, a-1):
#             if a % i == 0 :
#                 count += 1
#         if count != 0:
#             return False
#         else:
#             return True

# num = int(input("Введите число N:\n"))
# if check_prime(num):
#     print(f"Вы ввели простое число, его множители только 1 и {num}")
# else:
#     list = []
#     for e in range (2, num):
#         if check_prime(e):
#             while num % e == 0:
#                 list.append(e)
#                 num = num / e
#     print(list)      

# Задача 2. В первой строке файла находится информация об ассортименте мороженного, 
# во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»

# data = open("icecream.txt",encoding= "utf-8")
# text = data.readlines()
# data.close()
# assortment = text[0].replace("\n","").split(", ")
# stock = text[1].replace("\n","").split(", ")
# oos = []
# for i in range (0, len(assortment)):
#     if assortment[i] not in stock:
#         oos.append(assortment[i])
# print(oos)



# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 3 -> 3.142


# import math

# accuracy = int(input("Введите количество знаков после запятой:\n"))
# print(round(math.pi,accuracy))


# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 2. 3x^2 + x + 8
# 3. Результат: 8x^2 + 4x + 8

# Я смогла только придумать, как получить коэффициенты, и то это будет работать корректно, 
# только, если члены уравнения расставлены в порядке убывания и степени х-ов будут одинаковые. Но я пыталась, жалко удалять.

# def data_read(file):
#     data = open(file)
#     text = data.read()
#     data.close()
#     return text

# def only_coef(str):
#     string = []
#     for i in str:
#         if i != "x":
#             string.append(i)
#         else:
#             break
#     new_string = ",".join(string).replace(",", "")
#     new_string = int(new_string)
#     return new_string

# def change_pol(pol):
#     pol = pol.replace("+ ", "").replace("- ", "")
#     pol = pol.replace("^","").split(" ")
#     for i in range(0, len(pol)):
#         if pol[i] == "x":
#             pol[i] = "1"
#     for el in range(0, len(pol)):
#         pol[el] = only_coef(pol[el])
#     return pol

# text1 = data_read("4.1.txt")
# pol1 = change_pol(text1)
# text2 = data_read("4.2.txt")
# pol2 = change_pol(text2)
# print(pol1)
# print(pol2)
# if len(pol1) != len(pol2):
#     if len(pol1) > len(pol2):
#         pol2.extend([0,]*(len(pol1)-len(pol2)))
#     else:
#         pol1.extend([0,]*(len(pol2)-len(pol1)))
# sum = list(map(sum, zip(pol1,pol2)))
# print(f"Коэффициенты суммы многочленов: {sum}")



