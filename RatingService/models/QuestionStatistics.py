from pydantic import BaseModel
from typing import Any


class QuestionStatistics():
    type: str
    value: Any

    def __init__(self, type: str, value: Any):
        self.type = type
        self.value = value

    @classmethod
    def create_statistics(cls, type: str, value: Any) -> 'QuestionStatistics':
        return cls(type=type, value=value) 
    
    def update_statistics(self, value: Any) -> 'QuestionStatistics':
        self.value = value
    
    def get_statistics(self) -> 'QuestionStatistics':
        return self.value
    
    def get_type(self) -> str:
        return self.type
    
    def get_value(self) -> Any:
        return self.value
    