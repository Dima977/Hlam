print('Кол-во дисков')
print('1 - от 2, 2 - от 3, 3 - от 4, 4 - от 6, 5 - от 8')
a = int(input())

if a == 1:
    print('Уровень защиты')
    print('1 - Защиты нет, 2 - отказ одного диска диска')
    b = int(input())
    if b == 1:
        print('Скорость записи')
        print('1 - Высокая')
        c = int(input())
        if c ==1:
            print('RAID 0')
    if b == 2:
        print('Скорость записи')
        print('2 - Средняя')
        c = int(input())
        if c == 2:
            print('RAID 1')
if a == 2:
    print('Уровень защиты')
    print('2 - отказ одного диска диска')
    b = int(input())
    if b == 2:
        print('Скорость записи')
        print('2 - Средняя, 3 - Низкая ')
        c = int(input())
        if c == 2:
            print('RAID 1E')
        if c == 3:
            print('RAID 5')
if a == 3:
    print('Уровень защиты')
    print('3 - отказ двух дисков, 4 - отказ дисков в каждом суб. массиве')
    b = int(input())
    if b == 3:
        print('Скорость записи')
        print('3 - Низкая ')
        c = int(input())
        if c == 3:
            print('RAID 6')
    if b == 4:
        print('Скорость записи')
        print('2 - Средняя')
        c = int(input())
        if c == 2:
            print('RAID 10')
if a == 4:
    print('Уровень защиты')
    print('4 - отказ дисков в каждом суб. массиве')
    b = int(input())
    if b == 4:
        print('Скорость записи')
        print('2 - Средняя')
        c = int(input())
        if c == 2:
            print('RAID 50')
if a == 5:
    print('Уровень защиты')
    print('4 - отказ дисков в каждом суб. массиве')
    b = int(input())
    if b == 4:
        print('Скорость записи')
        print('2 - Средняя')
        c = int(input())
        if c == 2:
            print('RAID 60')








# print('Уровень защиты')
#     print('1 - Защиты нет, 2 - отказ одного диска диска, 3 - отказ двух дисков, 4 - отказ дисков в каждом суб. массиве')
#     b = int(input())
#
# print('Скорость записи')
# # print('1 - Высокая, 2 - Средняя, 3 - Низкая ')