# # Задача 1

# def func():
#     sum = 0
#     numList = list(input("Введите элементы списка: "))
#     print(numList)
#     for i in range(0, len(numList)-1):
#         if (i % 2 != 0):
#             sum += int(numList[i])
#     print(sum)


# func()


# # Задача 2

# def func():
#     mult = 0
#     newList = []
#     numList = list(input("Введите элементы списка: "))
#     print(numList)
#     for i in range(0, (round(len(numList)//1.5))):
#         mult = int(numList[i]) * ((int(numList[0 + len(numList) - 1 - i])))
#         newList.append(mult)
#     if ((len(numList) % 2) == 0):
#         newList.pop()
#     print(newList)


# func()


# # Задача 3

# def func():
#     floList = []
#     numQuant = input("Введите количество элементов в списке: ")
#     for i in range(1, int(numQuant) + 1):
#         num = float(input(f"Введите {i}-e вещественнoe числo: "))
#         floList.append(num)
#         highest = floList[0]
#         lowest = floList[0]
#         if (num > highest):
#             highest = num
#         if (lowest > num):
#             lowest = num
#         dif = (highest % 1) - (lowest % 1)
#     print(floList)
#     print(dif)


# func()


# # Задача 4

# def func():
#     n = int(input("Введите число для перевода в двоичную систему: "))
#     b = ''
#     while n > 0:
#         b += str(n % 2)
#         n //= 2
#     print(f"В двоичном виде будет: {b}")


# func()


# # Задача 5

# def func(n):
#     num = 1
#     if n > 2:
#         num = func(n-1) + func(n-2)
#     return num


# elem = int(input('Введите число: '))
# numList = []
# newList = []
# fstElem = [0]
# for i in range(1, elem + 1):
#     value = func(i)
#     anVal = func(i) * (-1)**(i+1)
#     numList.append(value)
#     newList.append(anVal)
#     revList = list(reversed(newList))
# print(revList + fstElem + numList)
