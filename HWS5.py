
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
a = int(input("Введите число: "))
b = int(input("Введите степень: "))
def exponentiation(x, n, s):
    if n > 0:
        s *= x
        n -= 1
        # print(s, n)
        return exponentiation(x, n, s)
    return s
print(exponentiation(a, b, 1))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def sum(a, b):
    if b > 0:
        a += 1
        b -= 1
        # print (a)
        return sum(a, b)
    return a
print (sum(a, b))
