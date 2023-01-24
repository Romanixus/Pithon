#import os
#os.chdir('Getting to know Python\HomePython\HWS7')

def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split())
        return result

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
            datafile.write(data_list +'\n')

def routes_output():
    for route in read_data_from_file('routes.txt'):
        print(route[0], route[1])
        for bus in read_data_from_file('buses.txt'):
            if route[2] == bus[0]: print(bus[0], bus[1])
        for driver in read_data_from_file('drivers.txt'):
            if route[3] == driver[0]: print(driver[0], driver[1])
        print()