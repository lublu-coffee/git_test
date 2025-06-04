from main import Cinema, Hall, Film, Session

print('Приветствуем вас с системе управления сетью кинотеатров')

lst_cinema = []


def main():
    global lst_cinema
    current_cinema = Cinema('', '')
    print('Введите:\n1 -> чтобы создать кинотеатр\n2 -> выбрать кинотеатр\n3 -> Добавить залы в текущий кинотеатр')
    answer = input('Ввод: ').strip()

    match answer:
        case '1':
            c = input('Создание кинотеатра.\nВведите: название, адрес: ')
            lst_cinema.append(Cinema(*c.split(', ')))

        case '2':
            print('Ваши кинотеатры. Выберете один')
            if lst_cinema:
                for i, cinema in enumerate(lst_cinema):
                    print(f'{cinema.Title} - > №{i + 1}')
                ans = int(input('Введите номер кинотеатра: '))
                if 0 < ans <= len(lst_cinema):
                    current_cinema = lst_cinema[ans - 1]
            else:
                print('ПУСТО !!!')

        case '3':
            print(f'Добавление залов в кинотеатр {current_cinema.Title}')
            if lst_cinema and current_cinema:
                current_cinema.set_hall()

        case _:
            print('Неверный ввод')
            main()

    if input('Продолжить ?? y|n: ') == 'y':
        main()


main()