# Напишите программу, которая выводит текст:

# print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:

# name = input()
# surname = input()
#
# print(f'Hello {name} {surname}! You just delved into Python')

# Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:

# teamName = input()
#
# print(f'Футбольная команда {teamName} имеет длину {len(teamName)} символов')

# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
# city1Name = input()
# city2Name = input()
# city3Name = input()
#
# if len(city1Name) == max(len(city1Name),len(city2Name),len(city3Name)):
#     if len(city2Name) == min(len(city2Name),len(city3Name)):
#         print(city2Name, city1Name, sep='\n')
#     else:
#         print(city3Name,city1Name, sep='\n')
# elif len(city2Name) == max(len(city1Name),len(city2Name),len(city3Name)):
#     if len(city1Name) == min(len(city1Name),len(city3Name)):
#         print(city1Name, city2Name, sep='\n')
#     else:
#         print(city3Name,city2Name, sep='\n')
# elif len(city3Name) == max(len(city1Name),len(city2Name),len(city3Name)):
#     if len(city2Name) == min(len(city2Name),len(city1Name)):
#         print(city2Name, city3Name, sep='\n')
#     else:
#         print(city1Name,city3Name, sep='\n')

# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
# firstString = input()
# secondString = input()
# thirdString = input()
#
# if (len(firstString)) == max(len(firstString),len(secondString),len(thirdString)):
#     if (len(firstString) - (max(len(secondString),len(thirdString)))) == (max(len(secondString),len(thirdString))) - (min(len(secondString),len(thirdString))):
#         print('YES')
#     else:
#         print('NO')
# elif len(secondString) == max(len(firstString),len(secondString),len(thirdString)):
#     if (len(secondString) - (max(len(firstString),len(thirdString)))) == (max(len(firstString),len(thirdString))) - (min(len(firstString),len(thirdString))):
#         print('YES')
#     else:
#         print('NO')
# elif len(thirdString) == max(len(firstString),len(secondString),len(thirdString)):
#     if (len(thirdString) - (max(len(firstString),len(secondString)))) == (max(len(firstString),len(secondString))) - (min(len(firstString),len(secondString))):
#         print('YES')
#     else:
#         print('NO')

# Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.
# word = 'синий'
# phrase = input()
# if word in phrase:
#     print('YES')
# else:
#     print('NO')

# Напишите программу, которая считывает одну строку, после чего выводит «YES»,
# если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.

# word1 = 'суббота'
# word2 = 'воскресенье'
#
# phrase = input()
#
# if word1 in phrase or word2 in phrase:
#     print('YES')
# else:
#     print('NO')

# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.
email = input()
if '@' not in email:
    print('NO')
elif '.' not in email:
    print('NO')
else:
    print('YES')


