
from pydantic import BaseModel
from typing import List, Dict

from models.Question import Question
from models.QuestionStatistics import QuestionStatistics
from models.UserResponse import UserResponse


class Survey:
    title: str
    description: str
    questions: List[Question]
    responses: List[UserResponse]
    question_based_agg: Dict[int, List[QuestionStatistics]]


    def __init__(self, title: str, description: str, questions: List[Question]):
        self.title = title
        self.description = description
        self.questions = questions
        self.responses = []
        self.question_based_agg = {q.id: [QuestionStatistics(type='avarage', value=0)] for q in questions}

    @classmethod
    def create_survey(cls, title: str, description: str, questions: List[Question]) -> 'Survey':
        return cls(title=title, description=description, questions=questions)
    
    # get avarage of any of user , query can be user name or user id 
    def get_avarage_of_user(self, user_name: str) -> float:
        for response in self.responses:
            if response.user.name == user_name:
                return response.avg_of_options
            
        # if user not found, return 0 or -1 or any identifier 
        return 0
    


    def get_avarage_of_question(self, question_id: int) -> float:
        all_statistics = self.question_based_agg[question_id]
        for statistics in all_statistics:
            if statistics.get_type() == "avarage":
                return statistics.get_value()

        return 0


    def submit_response(self, response: UserResponse) -> None:
        self.responses.append(response)
        for question, option in zip(response.question, response.option):
            all_statistics = self.question_based_agg[question.id]
            for statistics in all_statistics:
                if statistics.get_type() == "avarage":
                    
                    value = statistics.get_value() # 2.5
                    sum_value = value * (len(self.responses)-1)
                    sum_value += option.weight # 5.5
                    new_avg = sum_value / len(self.responses)
                    statistics.update_statistics(new_avg)



            
        


    def display_survey(self) -> None:
        print(self.title)
        print(self.description)
        for question in self.questions:
            print(question.value)
            for option in question.options:
                print(option.value)

    def display_responses(self) -> None:
        print(self.title)
        print(self.description)
        for response in self.responses:
            print(response.user.name)
            for question in response.question:
                print(question.value)
                for option in question.options:
                    print(option.value)