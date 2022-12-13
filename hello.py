# # Задача 2 семинара 2

# quantity = int(input("Введите количество чисел, которое будет указано: "))
# numList = [(int(input(f"Введите {i}-е число: ")))
#            for i in range(1, quantity + 1)]
# print("Введенные числа: ", numList)
# sum = 0
# for i in range(0, len(numList)):
#     sum += numList[i]
# print("Сумма введенных чисел: ", sum)


# # Задача 2 семинар 3

# def func():
#     numList = list(input("Введите элементы списка: "))
#     newList = [(int(numList[i]) * ((int(numList[0 + len(numList) - 1 - i]))))
#                for i in range(0, (round(len(numList)//1.5)))]
#     print(numList)
#     if ((len(numList) % 2) == 0):
#         newList.pop()
#     print(newList)


# func()

# # Задача 4 семинар 2

# n = int(input("Введите число: "))
# numList = [i for i in range(-n, n + 1)]
# indList = []
# print("Список: ", numList)
# indexQuantity = int(
#     input(f"Введите количество индексов чисел, произведение которых нужно найти в пределах от 1 до {len(numList)}: "))
# indList = list(
#     (input("Введите индекс(ы): ")).split(" "))
# print("Индексы: ", indList)
# mult = 1
# for i in range(0, len(indList)):
#     mult *= int(numList[int(indList[i])])
# print(f"Произведение чисел под индексами {indList} равна: {mult}")


# # Задача 5 семинар 3

# def func(n):
#     num = 1
#     if n > 2:
#         num = func(n-1) + func(n-2)
#     return num


# elem = int(input('Введите число: '))
# numList = [func(i) for i in range(1, elem + 1)]
# newList = [(func(i) * (-1)**(i+1)) for i in range(1, elem + 1)]
# fstElem = [0]
# for i in range(1, elem + 1):
#     revList = list(reversed(newList))
# print(revList + fstElem + numList)
