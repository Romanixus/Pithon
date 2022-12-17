import random
task = 12

if task == 10:
    n = int(input('Введите число монет: '))
    list = []
    sum = 0
    for num in range(0, n):
        number = random.randint(0, 1)
        list.append(number)
        sum += list[num]
    print(list)
    if sum < (n/2):
        min = sum
    else:
        min = n-sum
    print(f"Нужно перевернуть {min} монет")

if task == 12:
    b = int(input('Введите сумму чисел X и Y: '))
    c = int(input('Введите произведение чисел X и Y: '))
    D = b*b-4*c
    x = (b + D**0.5)/2
    y = b-x
    print(f"{x} и {y}")

if task == 14:
    n = int(input('Введите крайнюю степень: '))
    list = []
    count = 0
    while count != (n+1):
        list.append(2**count)
        count+=1
    print(list)
