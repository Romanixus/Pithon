import random
task = 24

if task == 22:
    n = int(input("Количество элементов первого набора: "))
    m = int(input("Количество элементов второго набора: "))
    nabor1 = []
    nabor2 = []
    for i in range(0, n):
        number = random.randint(0, n)
        nabor1.append(number)
    for i in range(0, m):
        number = random.randint(0, m)
        nabor2.append(number)
    print(nabor1)
    print(nabor2)
    set1 = set(nabor1)
    set2 = set(nabor2)
    set3 = set1.intersection(set2)
    print(set3)

if task == 24:
    n = int(input("Количество кустов на грядке: "))
    gryadka = []
    for i in range(0, n):
        number = random.randint(5, 10)
        gryadka.append(number)
    print(gryadka)
    # чтобы не было ошибки с прибавлением куста справа к последнему (n+1)
    gryadka.append(gryadka[0])
    # чтобы не было ошибки с прибавлением куста слева от первого (-1)
    gryadka.insert(0, gryadka[n-1])
    # print(gryadka)
    sbor = []
    #сдвиг на один элемент вправо ((n+2)-n)/2
    for i in range(1, n+1):
        sum = gryadka[i]+gryadka[i+1]+gryadka[i-1]
        sbor.append(sum)
    # print(sbor)
    max = 0
    for i in sbor:
        if i > max:
            max = i
    print(max)
