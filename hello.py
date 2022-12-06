# # Задача 1

# from math import pi
# d = float(input('Введите D в формате 0.(0)1: '))
# k = 0
# while d < 1:
#     d *= 10
#     k += 1
# res = int(pi * (10**(k+1)))
# if d > 1:
#     print("Введите именно в формате 0.(0)1")
#     KeyboardInterrupt
# else:
#     res = res // 10 * (10**(-k))
#     print(res)


# # Задача 2

# n = int(input("Введите N: "))


# def primMults(n):
#     i = 2
#     primMult = []
#     while i * i <= n:
#         while n % i == 0:
#             primMult.append(i)
#             n /= i
#         i += 1
#     if n > 1:
#         primMult.append(n)
#     print(primMult)


# primMults(n)


# # Задача 3

# n = input("Введите числа в список через запятую: ")
# numList = n.split(",")
# i = 0
# print(f'Исходный список: {numList}')
# while i < (len(numList) - 1):
#     counter = 1
#     for j in range(i+1, len(numList)):
#         if numList[i] == numList[j]:
#             counter += 1
#     if counter > 1:
#         t = numList[i]
#         i -= 1
#         for j in range(counter):
#             numList.remove(t)
#     i += 1
# print(f'Результирующий список из неповторяемых чисел: {numList}')


# # Задача 4

# from random import randint

# k = int(input('k = '))
# string = ''
# for i in range(k, -1, -1):
#     temp = randint(0, 100)
#     if temp > 0:
#         if i < k:
#             string += ' + '
#         string += str(temp)
#         if i > 1:
#             string += '*x^' + str(i)
#         elif i == 1:
#             string += '*x'
# data = open('test.txt', 'a')
# data.write(string + '\n')
# data.close()
