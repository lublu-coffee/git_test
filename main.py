from dataclasses import dataclass, field
from add_id_class import add_id


@dataclass
class Cinema:
    Id: int = field(init=False)
    Title: str
    Address: str = field(init=False, default='')
    Halls: list = field(default_factory=list)

    def __post_init__(self):
        self.Id = add_id(self.__class__.__name__)

    def get_count_hall(self):
        return len(self.Halls)

    def full_halls_lst(self, halls):
        for h in halls:
            self.Halls.append(h)
            
    def get_address(self, address):
        self.Address = address


@dataclass
class Hall:
    Id: int = field(init=False)
    Title: str
    Row: int = 0
    Seats: int = 0

    def __post_init__(self):
        self.Id = add_id(self.__class__.__name__)

    def get_count_seats(self):
        return self.Row * self.Seats

@dataclass
class Address:
    Id: int = field(init=False)
    Title: str

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

    def get_genres(self, *args):
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


# Адреса
adr1 = Address('Баумана 21')
adr2 = Address('Адоратского 10а')
adr3 = Address('Сибгата Хакима 40')

# Залы
h1 = Hall('A2', 20, 10)
h2 = Hall('B4', 20, 15)
h11 = Hall('A2', 30, 10)
h22 = Hall('B4', 20, 15)
h3 = Hall('D2', 20, 10)
h4 = Hall('Y4', 10, 15)

# Кинотеатры
c1 = Cinema('Кинотеатр 1')
c2 = Cinema('Кинотеатр 2')
c3 = Cinema('Кинотеатр 3')
c1.full_halls_lst([h1, h2])
c1.get_address(adr1)

# Фильмы
f1 = Film('Шрек', '', 120, [Genre('приключение')])
f2 = Film('Моана', '', 90, [Genre('приключение'), Genre('романтика')])
f3 = Film('Миньоны 3', '', 59, [Genre('приключение'), Genre('боевик')])

# Сеансы
s1 = Session('2025-06-06', '12:00', f1)
s2 = Session('2025-06-06', '13:30', f1)
s3 = Session('2025-07-08', '11:10', f3)


print(c1.__dict__)
print(s1.__dict__)
print(s2.__dict__)