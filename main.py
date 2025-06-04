from dataclasses import dataclass, field
from add_id_class import add_id


@dataclass
class Cinema:
    Id: int = field(init=False)
    Title: str
    Address: str
    Halls: list = field(default_factory=list)

    def __post_init__(self):
        self.Id = add_id(self.__class__.__name__)

    def set_hall(self):
        title, row, seats = input('введите: название, ряды, места: ').split(', ')
        hall = Hall(title, int(row), int(seats))
        self.Halls.append(hall)


@dataclass
class Hall:
    Id: int = field(init=False)
    Title: str
    Row: int = 0
    Seats: int = 0

    def __post_init__(self):
        self.Id = add_id(self.__class__.__name__)


@dataclass
class Film:
    Id: int = field(init=False)
    Title: str
    Description: str
    Duration: int
    Genres: list = field(default_factory=list)

    def __post_init__(self):
        self.Id = add_id(self.__class__.__name__)

    def set_genres(self, *args):
        self.Genres = list(args)


@dataclass
class Genre:
    Id: int = field(init=False)
    Title: str

    def __post_init__(self):
        self.Id = add_id(self.__class__.__name__)


@dataclass
class Session:
    Id: int = field(init=False)
    Data: str
    Time: str
    Film: Film

    def __post_init__(self):
        self.Id = add_id(self.__class__.__name__)


if __name__ == '__main__':
    # Залы
    h1 = Hall('A2', 20, 10)
    h2 = Hall('B4', 20, 15)
    h11 = Hall('A2', 30, 10)
    h22 = Hall('B4', 20, 15)
    h3 = Hall('D2', 20, 10)
    h4 = Hall('Y4', 10, 15)

    # Кинотеатры
    c1 = Cinema('Кинотеатр 1', 'hhhh')
    c2 = Cinema('Кинотеатр 2', 'jjj')
    c3 = Cinema('Кинотеатр 3', 'jjj')
    # c1.set_halls_lst([h1, h2])

    # Фильмы
    f1 = Film('Шрек', '', 120, [Genre('приключение')])
    f2 = Film('Моана', '', 90, [Genre('приключение'), Genre('романтика')])
    f3 = Film('Миньоны 3', '', 59, [Genre('приключение'), Genre('боевик')])

    # Сеансы
    s1 = Session('2025-06-06', '12:00', f1)
    s3 = Session('2025-07-08', '11:10', f3)

    print(c1.__dict__)
    print(s1.__dict__)
    print(s3.__dict__)