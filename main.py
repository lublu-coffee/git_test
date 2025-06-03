def get_int_range():
    n = int(input('Введите для второго цикла: '))
    for v2 in range(n):
        print(v2)
    if input('Хотите продолжить ') == 'y':
        get_int_range()


get_int_range()