# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
fileName ='phonebook.txt'

def writeFile(file_name):
    with open(file_name, 'a') as data:

        data.writelines('\nBoss Gerare Finni 823340234')

def readFile(file_name):
    spisok = []
    with open(file_name, 'r+') as data:
        for line in data:
            spisok.append(line.split())
    return spisok

def findUser(userList):
    name = 'Gerare'
    for user in userList:
            if user[1] == name:
                print(user[3])

def delUser(file_name):
    name = 'Boss Gerare Finni 823340234'
    with open(file_name, "r") as file:
        data = file.readlines()
    with open(file_name, "w") as file:
        for line in data:
            if line.strip() != name:
                    file.write(line)
                    
writeFile(fileName)
print(readFile(fileName))
findUser(readFile(fileName))
delUser(fileName)