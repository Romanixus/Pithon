def snail (forward, back, distance, way, count):
    way += forward
    count += 1
    if way < distance:
        way -= back
        print(count, way)
        return snail(forward, back, distance, way, count)
    print(count, way)
    return count

# snail(5, 4, 158, 0, 0)


import datetime as dt

def read_data_from_file():
    spisok_dat = []
    with open('Birthdays.txt', encoding='utf-8') as datafile:
        for line in datafile:
            spisok_dat.append(line.split()[0])  
    return spisok_dat


print(read_data_from_file())
# print(dt.datetime.today())
# print(dt.datetime.now())

# d1 = dt.datetime.today()
# d2 = d1 + dt.timedelta(days=10)
# print((d2-d1).days)