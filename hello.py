# # Задача 1

# n = int(input("Введите вещественное число: "))
# b = n.split(".")
# num = int(b[1])
# sum = 0
# print(b[1])
# while num != 0:
#     sum += num % 10
#     num //= 10
# print(sum)


# # Задача 2

# n = int(input("Введите число: "))
# factorial = []
# num = 1
# for i in range(1, n+1):
#     num *= i
#     factorial.append(num)
# print(factorial)


# # Задача 3

# quantity = int(input("Введите количество чисел, которое будет указано: "))
# numList = []
# for i in range(1, quantity + 1):
#     numbers = input(f"Введите {i}-е число: ")
#     numList.append(float(numbers))
# print("Введенные числа: ", numList)
# sum = 0
# for i in range(0, len(numList)):
#     sum += numList[i]
# print("Сумма введенных чисел: ", sum)


# # Задача 4

# n = int(input("Введите число: "))
# numList = []
# indList = []
# for i in range(-n, n + 1):
#     numList.append(int((-n + i)/2))
#     n -= 1
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

# # Задача 5 По-моему читерски выполнено, но что-то мне подсказывает, что вы и ожидали самообучение в гугле :D

# import random
# numList = list((input("Введите элементы списка через пробел: ")).split(" "))
# random.shuffle(numList)
# print(numList)
