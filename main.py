from dataclasses import dataclass, field


@dataclass
class Cinema:
    count_id = 0
    Id: int = field(init=False)
    Title: str
    Address: str
    CountHalls: int
    Halls: list = field(default_factory=list)

    def __post_init__(self):
        Cinema.count_id += 1
        self.Id = Cinema.count_id

    def full_halls_lst(self, halls):
        for h in halls:
            self.Halls.append(h)
            h.get_cinema(self)


@dataclass
class Hall:
    count_id = 0
    Id: int = field(init=False)
    Title: str
    Row: int = 0
    Seats: int = 0
    Cinema: Cinema = None

    def __post_init__(self):
        Hall.count_id += 1
        self.Id = Hall.count_id

    def get_cinema(self, cinema):
        self.Cinema = cinema


h1 = Hall('A2', 20, 10)
h2 = Hall('B4', 30, 15)
print(h1.__dict__)
print(h2.__dict__)

c1 = Cinema('Кинотеатр 1', 'Баумана 10', 2)
c1.full_halls_lst([h1, h2])
print()
print(h1.__dict__)
print(h2.__dict__)
print(c1.__dict__)