from dataclasses import dataclass, field


@dataclass
class Cinema:
    Id: int
    Title: str
    Address: str
    CountHalls: int
    Halls: field(default_factory=list)


@dataclass
class Hall:
    Id: int
    Title: str
    Cinema: Cinema
    Row: int
    Seats: int

