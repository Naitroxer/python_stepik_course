# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.

# a = float(input())
# b = float(input())
#
# S = 0.5*a*b
# print(S)

# Две старушки идут навстречу друг другу с постоянными скоростями V1 и V2 км/ч.
# Определите, через какое время старушки встретятся, если расстояние между ними равно S км.
# Примечание. Это очень быстрые старушки.

# S = float(input())
# V1 = float(input())
# V2 = float(input())
#
# t = S/(V1+V2)
# print(t)

# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).

# num = float(input())
#
# if num != 0:
#     num1 = num ** (-1)
#     print(num1)
# else:
#     print('Обратного числа не существует')

# Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.

# F = float(input())
#
# C = (5/9)*(F-32)
# print(C)

# Напишите программу, которая вычисляет возраст собаки в человеческих годах.

# dogAge = int(input())
# if dogAge <=2:
#     humanDogAge = 10.5*dogAge
# else:
#     humanDogAge = 10.5*2 + (dogAge-2) * 4
#
# print(humanDogAge)

# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

# num = float(input())
#
# x = (num * 10) % 10
# print(int(x))

# Дано положительное действительное число. Выведите его дробную часть.

# x = float(input())
#
# y = x - (int(x))
# print(y)

# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

# a,b,c,d,e = int(input()),int(input()),int(input()),int(input()),int(input())
# x = min(a,b,c,d,e)
# y = max(a,b,c,d,e)
#
# print('Наименьшее число =', x)
# print('Наибольшее число =', y)

# Напишите программу, которая упорядочивает три числа от большего к меньшему.

# a, b, c = int(input()),int(input()),int(input())
# if a >= b and a >= c:
#     print(a, max(b,c), min(b,c), sep="\n")
# elif b >= a and b >= c:
#     print(b, max(a,c), min(a,c), sep="\n")
# else:
#     print(c, max(a,b), min(a,b), sep="\n")

# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

# x = int(input())
# first = ((x % 1000) // 100)
# second = ((x % 100) // 10)
# third = (x % 10)
# diff = max(first,second, third) - min(first,second,third)
#
# if diff == first or diff == second or diff == third:
#     print('Число интересное')
# else:
#     print('Число неинтересное')


# Даны пять чисел/Напишите программу, которая вычисляет сумму их модулей
# a,b,c,d,e = float(input()),float(input()),float(input()),float(input()),float(input())
#
# print(abs(a)+abs(b)+abs(c)+abs(d)+abs(e))

# Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.

p1,p2,q1,q2 = int(input()),int(input()),int(input()),int(input())

print(abs(p1-q1)+abs(p2-q2))