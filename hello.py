# # Задача 1

# dayNum = int(input("Введите день недели: "))
# if (dayNum == 6 or dayNum == 7):
#     print("Выходной")
# else:
#     print("Будний день")


# # Задача 2

# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             check = (not (x or y or z)) == ((not (x)) and not (y) and not (z))
#             print(
#                 f' {x}, {y}, {z} - не ({x} или {y} или {z}) =  (не {x} и не {y} и не {z})  - {check}')


# # Задача 3

# x = int(input("Введите Х: "))
# y = int(input("Введите Y: "))
# if (x > 0 and y > 0):
#     print("1-ая четверть")
# elif (x < 0 and y > 0):
#     print("2-ая четверть")
# elif (x < 0 and y < 0):
#     print("3-я четверть")
# else:
#     print("4-ая четверть")


# # Задача 4

# quart = int(input("Введите номер четверти (от 1 до 4): "))
# if quart == 1:
#     print("Х и Y должны быть положительными")
# elif quart == 2:
#     print("Х - отрицательное, Y - положительное")
# elif quart == 3:
#     print("Х и Y должны быть отрицательными")
# elif quart == 4:
#     print("Х - положительное, Y - отрицательное")
# else:
#     print("Введите число от 1 до 4")


# # Задача 5

# a = int(input("Введите X для первой координаты: "))
# b = int(input("Введите Y для первой координаты: "))
# c = int(input("Введите X для второй координаты: "))
# d = int(input("Введите Y для второй координаты: "))
# distance = float((((c-a)**2) + (d-b)**2)**(0.5))
# fixedDistance = '{:.2f}'.format(distance)
# print(fixedDistance)
