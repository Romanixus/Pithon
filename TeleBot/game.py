import random

def print_field():
    print(field[0],field[1],field[2])
    print(field[3],field[4],field[5])
    print(field[6],field[7],field[8])
    print('---')

def check_victory():
    if field[0] == field[1] == field[2]:
        print(f'Победили {field[1]}')
    elif field[3] == field[4] == field[5]:
        print(f'Победили {field[4]}')
    elif field[6] == field[7] == field[8]:
        print(f'Победили {field[7]}')
    elif field[0] == field[3] == field[6]:
        print(f'Победили {field[3]}')
    elif field[1] == field[4] == field[7]:
        print(f'Победили {field[4]}')
    elif field[2] == field[5] == field[8]:
        print(f'Победили {field[5]}')
    elif field[0] == field[4] == field[8]:
        print(f'Победили {field[4]}')
    elif field[2] == field[4] == field[6]:
        print(f'Победили {field[4]}')
    else: return 0

def bot_motion():
    number = random.randint(0, 8)
    if (field[number]=='X') or (field[number]=='O'):
        return bot_motion()
    field[number] ='X'
    print(f"Бот ходит на {number+1}")
    print_field() 
    if check_victory() == 0:
        player_motion()  

def player_motion():
    motion = int(input('Куда поставить нолик? '))
    field[motion-1] = 'O'
    print_field()
    if check_victory() == 0:
        bot_motion()

field = [1,2,3,4,5,6,7,8,9]

bot_motion()

