# n = int(input())
# k = int(input())
#S
# if n>k:
#     print('NO')
# elif n<k:
#     print('YES')
# else:
#     print("Don't know")

# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
# a = int(input())
# b = int(input())
# c = int(input())
#
#
# if a==b==c:
# elif a==b or a==c or b==c:
#     print('Равнобедренный')
# else:
#     print("Разносторонний")

# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
# a = int(input())
# b = int(input())
# c = int(input())
#
#
# if a<b<c or a>b>c:
#     print(b)
# elif b<a<c or b>a>c:
#     print(a)
# else:
#     print(c)

# monthNum = int(input())
#
# if monthNum == 2:
#     print('28')
# elif monthNum == 4 or monthNum == 6 or monthNum == 9 or monthNum == 11:
#     print('30')
# else:
#     print('31')

# Напишите программу, определяющую, в какой категории будет выступать данный боксер.

# weight = int(input())
#
# if weight < 60:
#     print('Легкий вес')
# elif 60 <= weight < 64:
#     print('Первый полусредний вес')
# else:
#     print('Полусредний вес ')

# Напишите программу, которая считывает с клавиатуры два целых числа и строку.
# Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /),
# то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция».
# Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».

# firstNum = int(input())
# secondNum = int(input())
# sign = input()
#
# if sign == '+':
#     print(firstNum + secondNum)
# elif sign == '-':
#     print(firstNum - secondNum)
# elif sign == '*':
#     print(firstNum * secondNum)
# elif sign == '/':
#     if secondNum == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(firstNum / secondNum)
# else:
#     print('Неверная операция')

# микшер цветов

# firstColor = input()
# secondColor = input()
#
# if firstColor == 'красный' or firstColor == 'синий' or firstColor == 'желтый':
#     if secondColor == 'красный' or secondColor == 'синий' or secondColor == 'желтый':
#         if firstColor == "красный" and secondColor == "синий" or firstColor == "синий" and secondColor == "красный":
#             print('фиолетовый')
#         elif firstColor == "красный" and secondColor == "желтый" or firstColor == "желтый" and secondColor == "красный":
#             print('оранжевый')
#         elif firstColor == "желтый" and secondColor == "синий" or firstColor == "синий" and secondColor == "желтый":
#             print('зеленый')
#         else:
#             print(firstColor)
#     else:
#         print('ошибка цвета')
# else:
#     print('ошибка цвета')
# else:
#     if firstColor == "красный" and secondColor == "синий" or firstColor == "синий" and secondColor == "красный":
#         print('фиолетовый')
#     elif firstColor == "красный" and secondColor == "желтый" or firstColor == "желтый" and secondColor == "красный":
#         print('оранжевый')
#     elif firstColor == "желтый" and secondColor == "синий" or firstColor == "синий" and secondColor == "желтый":
#         print('зеленый')
#     else:
#         print('ошибка цвета')

# a = input()
# b = input()
# ab = a+b
# if (ab == "красныйсиний") or (ab == "синийкрасный"):
#     print("фиолетовый")
# elif (ab == "красныйжелтый") or (ab == "желтыйкрасный"):
#     print("оранжевый")
# elif (ab == "синийжелтый") or (ab == "желтыйсиний"):
#     print("зеленый")
# elif (ab == "красныйкрасный") or (ab == "синийсиний") or (ab == "желтыйжелтый"):
#     print(a)
# else:
#     print("ошибка цвета")

# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным.
# Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

# number = int(input())
#
# if number == 0:
#     print('зеленый')
# elif 1 <= number <= 10:
#     if number % 2 == 1:
#         print('красный')
#     else:
#         print('черный')
# elif 11 <= number <= 18:
#     if number % 2 == 1:
#         print('черный')
#     else:
#         print('красный')
# elif 19 <= number <= 28:
#     if number % 2 == 1:
#         print('красный')
#     else:
#         print('черный')
# elif 29 <= number <= 36:
#     if number % 2 == 1:
#         print('черный')
#     else:
#         print('красный')
# else:
#     print('ошибка ввода')

# найти пересечение отрезков

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

# проверяем на точку:
if a1 == b2:
    print(a1)
elif b1 == a2:
    print(b1)
# проверяем на пустое множество:
elif a2 > b1 or a1 > b2:
    print('пустое множество')
# проверяем на отрезок:
else:
    if a2 == a1 and b2 == b1:
        print(a2, b2)
    elif a2 <= a1 < b2:
        if b2 >= b1:
            print(a1, b1)
        elif b1 >= b2:
            print(a1, b2)
    elif a1 <= a2 < b1:
        if b2 >= b1:
            print(a2, b1)
        elif b1 >= b2:
            print(a2, b2)