# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
import math

# from math import *
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
#
# p = sqrt(pow((x1-x2), 2) + pow((y1-y2), 2))
# print(p)

# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу
# from math import *
#
# R = float(input())
#
# S = pi * pow(R,2)
# P = 2 * pi * R
# print(S,P, sep='\n')

# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

# from math import *
# x = float(input())
# y = float(input())
#
# a = (x+y)/2
# b = sqrt(x*y)
# c = (2*x*y)/(x+y)
# d = sqrt((pow(x,2)+pow(y,2))/2)
#
# print(a,b,c,d, sep='\n')

# Напишите программу, вычисляющую значение тригонометрического выражения  по заданному числу градусов
# from math import *
# x = radians(float(input()))
#
# print(f'{sin(x)+cos(x)+pow(tan(x),2)}')

# from math import *
# x = float(input())
#
# print(ceil(x)+floor(x))

# Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения
# from math import *
# a = float(input())
# b = float(input())
# c = float(input())
#
# D = pow(b,2) - 4*a*c
#
# if D < 0:
#     print('Нет корней')
# elif D == 0:
#     x1 = -(b/(2*a))
#     print(x1)
# else:
#     x1 = (-b + sqrt(D))/(2*a)
#     x2 = (-b - sqrt(D))/(2*a)
#     print(min(x2,x1),max(x2,x1), sep='\n')

# Даны два числа: натуральное число n и вещественное число a. Напишите программу, которая находит площадь указанного правильного многоугольника.
# from math import *
#
# n = float(input())
# a = float(input())
#
# S = (n*pow(a, 2))/(4 * (tan((pi/n))))
# print(S)