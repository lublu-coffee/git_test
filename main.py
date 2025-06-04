from dataclasses import dataclass, field


@dataclass
class Cinema:
    count_id = 0
    Id: int = field(init=False)
    Title: str
    Address: str = field(init=False, default='')
    Halls: list = field(default_factory=list)

    def __post_init__(self):
        Cinema.count_id += 1
        self.Id = Cinema.count_id

    def get_count_hall(self):
        return len(self.Halls)

    def full_halls_lst(self, halls):
        for h in halls:
            self.Halls.append(h)
            
    def get_address(self, adress):
        self.Address = adress


@dataclass
class Hall:
    count_id = 0
    Id: int = field(init=False)
    Title: str
    Row: int = 0
    Seats: int = 0

    def __post_init__(self):
        Hall.count_id += 1
        self.Id = Hall.count_id


@dataclass
class Address:
    count_id = 0
    Id: int = field(init=False)
    Title: str

    def __post_init__(self):
        Address.count_id += 1
        self.Id = Address.count_id

@dataclass
class Film:
    count_id = 0
    Id: int = field(init=False)
    Title: str
    Description: str
    Duration: int
    Genres: list = field(default_factory=list)

    def __post_init__(self):
        Film.count_id += 1
        self.Id = Film.count_id




h1 = Hall('A2', 20, 10)
h2 = Hall('B4', 30, 15)
c1 = Cinema('Кинотеатр 1')
adr1 = Address('Баумана 21')
c1.full_halls_lst([h1, h2])
c1.get_address(adr1)
print(h1.__dict__)
print(h2.__dict__)
print(c1.__dict__)
