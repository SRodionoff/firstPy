# # Задача 1

# letter = input('Введите строку: ')
# letList = letter.split(' ')
# banWord = ('абв')
# print(letList)
# newList = ' '.join(list(filter(lambda word: not banWord in word, letList)))
# print(newList)


# # Задача 2

# import random
# print('Можно забрать не более 28 конфет за ход')


# def game():
#     who1st = random.randint(1, 2)
#     print((f'Первым ходит: {who1st}'))
#     sweets = 100
#     if who1st == 1:
#         while (sweets >= 0):
#             step1 = int(input('1-ый игрок: '))
#             while step1 > 28:
#                 step1 = int(
#                     input(('... не больше 28: ')))
#             sweets -= step1
#             print(f'Конфет осталось: {sweets}')
#             if sweets == 0:
#                 print('Победил 1-ый игрок, вот тебе 2021 конфета и инсулин')
#                 quit()
#             step2 = int(input('2-ой игрок: '))
#             while step2 > 28:
#                 step2 = int(
#                     input(('... не больше 28: ')))
#             sweets -= step2
#             print(f'Конфет осталось: {sweets}')
#             if sweets == 0:
#                 print('Победил 2-ой игрок, вот тебе 2021 конфета и инсулин')
#                 quit()
#     else:
#         while (sweets >= 0):
#             step2 = int(input('2-ой игрок: '))
#             while step2 > 28:
#                 step2 = int(
#                     input(('... не больше 28: ')))
#             sweets -= step2
#             print(f'Конфет осталось: {sweets}')
#             if sweets == 0:
#                 print('Победил 1-ый игрок, вот тебе 2021 конфета и инсулин')
#                 quit()
#             step1 = int(input('1-ый игрок: '))
#             while step1 > 28:
#                 step1 = int(
#                     input(('... не больше 28: ')))
#             sweets -= step1
#             print(f'Конфет осталось: {sweets}')
#             if sweets == 0:
#                 print('Победил 1-ый игрок, вот тебе 2021 конфета и инсулин')
#                 quit()


# game()


# # Задача 3

# board = list(range(1, 10))


# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print(f"| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |")
#         print("-" * 13)


# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input(f'Введите {player_token}: ')
#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Нужно ввести число от 1 до 9")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print("Клетка уже занята")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9: ")


# def check_win(board):
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
#                  (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False


# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, "выиграл")
#                 win = True
#                 quit()
#         if counter == 9:
#             print("Ничья")
#             quit()
#     draw_board(board)


# main(board)


# # Задача 4

# from pathlib import Path
# inputWay = Path('main text.txt')
# toEncode = inputWay.read_text()
# outputWay = Path('rle text.txt')


# def rle(file):
#     encode = ''
#     prevLetter = ''
#     count = 1
#     if not file:
#         return ''
#     for letter in file:
#         if letter != prevLetter:
#             if prevLetter:
#                 encode += str(count) + prevLetter
#             count = 1
#             prevLetter = letter
#         else:
#             count += 1

#     else:
#         encode += str(count) + prevLetter
#         return encode


# outputWay.write_text(rle(toEncode))
