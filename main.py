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



h1 = Hall('A2', 20, 10)
h2 = Hall('B4', 30, 15)
c1 = Cinema('Кинотеатр 1')
adr1 = Address('Баумана 21')
c1.full_halls_lst([h1, h2])
c1.get_address(adr1)
print(h1.__dict__)
print(h2.__dict__)
print(c1.__dict__)
