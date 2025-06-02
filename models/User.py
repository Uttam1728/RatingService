from pydantic import BaseModel


class User():
    id: int
    name: str
    email: str

    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def create_user(cls, id: int, name: str, email: str):
        return cls(id=id, name=name, email=email)