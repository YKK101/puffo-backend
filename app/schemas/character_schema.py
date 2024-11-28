from pydantic import BaseModel

class Element(BaseModel):
    atomic_number: int
    element_symbol: str
    element_name: str
    atomic_mass: float
    group: str
    status: str
    grid_location: list[int]

