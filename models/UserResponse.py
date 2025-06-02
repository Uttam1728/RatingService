
from pydantic import BaseModel
from typing import List

from models import Survey
from models.Option import Option
from models.Question import Question
from models.User import User


class UserResponse():
    question: List[Question]
    option: List[Option]
    user: User
    avg_of_options: float

    # get avarae of every options 

    def __init__(self, question: List[Question], option: List[Option], user: User):
        self.question = question
        self.option = option
        self.user = user
        self.avg_of_options = self.get_avarage_of_options()

    
    def get_avarage_of_options(self) -> float:
        return sum(option.weight for option in self.option) / len(self.option)
    