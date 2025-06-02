from pydantic import BaseModel



class Option():
    value: str
    weight: int
    def __init__(self, value: str, weight: int):
        self.value = value
        self.weight = weight

    @classmethod
    def create_option(cls, value: str, weight: int):
        return cls(value=value, weight=weight)

