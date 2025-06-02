from pydantic import BaseModel
from typing import List

from models.Option import Option


class Question():
    id: int
    value: str
    options: List[Option]

    def __init__(self, id: int, value: str, options: List[Option]):
        self.id = id
        self.value = value
        self.options = options

    @classmethod
    def create_question(cls, id: int, value: str, options: List[Option]):
        return cls(id=id, value=value, options=options)
