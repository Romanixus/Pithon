import random
task = 20

if task == 16:
    spisok = []
    n = int(input("Количество элементов в массиве: "))
    x = int(input("Число, которое необходимо проверить: "))
    for i in range(0, n):
        number = random.randint(0, n//2)
        spisok.append(number)
    print(spisok)
    count = 0
    for num in spisok:
        if num == x:
            count += 1
    print(f"Число {x} встречается {count} раз")

if task == 18:
    spisok = []
    n = int(input("Количество элементов в массиве: "))
    x = int(input("Число, которое необходимо проверить: "))
    for i in range(0, n):
        number = random.randint(0, n//2)
        spisok.append(number)
    print(spisok)
    set = set(spisok)
    # print(set)
    count = -1
    num = x
    end = 0
    while end != 1:
        for i in set:
            if num == i:
                print("Ближайший к X элемент:", num)
                end = 1
        if count < 0:
            num = x + count
            count *= (-1)
        elif count > 0:
            num = x + count
            count = (count+1)*(-1)
        # print (count, num)

if task == 20:
    txt = input("Введите слово: ")
    sum = 0
    spisok1 = ("a", "e", "i", "o", "u", "l", "n", "s", "t", "r",
     "а", "в", "е", "и", "н", "о", "р","с", "т")
    spisok2 = ("d","g","д","к","л","м","п","у")
    spisok3 = ("b","c","m","p","б","г","ё","ь","я")
    spisok4 = ("f","h","v","w","y","й","ы")
    spisok5 = ("k","ж","з","х","ц","ч")
    spisok8 = ("j","x","ш","э","ю")
    spisok10 = ("q","z","ф","щ","ъ")
    for bukva in txt:
        for bukva1 in spisok1: 
            if bukva == bukva1:
                sum += 1
        for bukva2 in spisok2: 
            if bukva == bukva2:
                sum += 2
        for bukva3 in spisok3: 
            if bukva == bukva3:
                sum += 3
        for bukva4 in spisok4: 
            if bukva == bukva4:
                sum += 4
        for bukva5 in spisok5: 
            if bukva == bukva5:
                sum += 5
        for bukva8 in spisok8: 
            if bukva == bukva8:
                sum += 8
        for bukva10 in spisok10: 
            if bukva == bukva10:
                sum += 10
        #print(bukva, sum)
    print(sum)
