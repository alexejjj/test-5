print('Введите люой год високосного календаря: ')
flag = True
while flag:
    try:
        year = int(input())
    except ValueError:
        print('ошибка')
    else:
        flag = False
if year % 4 != 0:
    print(f'Год {year} является невисокосным годом')
else:
    if year % 100 != 0:
        print(f'Год {year} является високосным годом')
    else:
        if year % 400 == 0:
            print(f'Год {year} является високосным годом')
        else:
            print(f'Год {year} является невисокосным годом')
if year % 100 > 0:
    print(f'Год {year} относится к {(year // 100) + 1} веку')
else:
    print(f'Год {year} относится к {year // 100} веку')

