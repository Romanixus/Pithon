# Задача 2
text = input()
sum = 0
for i in range(0, len(text)):
    sum += int(text[i])
print(sum)

# # Задача 4
vsego = int(input())
K = vsego//6*4
P = S = K//4
print(P, K, S)
print(f'Подкинули: {vsego % 6}')

# Задача 6
bilet = input()
sum = [0, 0, 0]
for i in range(0, 2):
    for j in range(0, 3):
        sum[i] = sum[i]+int(bilet[j+i*3])
    print(sum[i])
if sum[0] == sum[1]:
    print('yes')
else:
    print('no')

# Задача 8
a = int(input())
b = int(input())
dolki = int(input())
if dolki>(a*b):
     print('mnogo')
elif (dolki % a) == 0 or (dolki % b) == 0:
    print('yes')
else:
    print('no')