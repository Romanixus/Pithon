import function as fn

menuitems = [
("1", "Вывод автобусов"),
("2", "Добавление автобуса"),
("3", "Вывод водителей"),
("4", "Добавление водителя"),
("5", "Вывод маршрутов"),
("6", "Добавление маршрута"),
("7", "Выход")]

for i in menuitems:
        print(i[0],i[1])


text = input("Введите номер: ")
if text == '1':
        print(fn.read_data_from_file('buses.txt'))
if text == '2':
        fn.save_data_to_file('buses.txt', input("Введите данные автобуса: "))
if text == '3':
        print(fn.read_data_from_file('drivers.txt'))
if text == '4':
        fn.save_data_to_file('drivers.txt', input("Введите данные водителя: "))
if text == '5':
        print(fn.routes_output())
if text == '6':
        fn.save_data_to_file('drivers.txt', input("Введите данные маршрута: "))
