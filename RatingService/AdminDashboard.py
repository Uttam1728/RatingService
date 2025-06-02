

from models.User import User
from models.Survey import Survey
from models.Question import Question
from models.Option import Option
from models.UserResponse import UserResponse


class AdminDashboard:

    def init(self):
        # create question and answer and survays

        very_good_option = Option(value="very poor", weight=1)
        poor_option = Option(value="poor", weight=2)
        avg_option = Option(value="avarage", weight=3)
        good_option = Option(value="good", weight=4)
        very_good_option = Option(value="very good", weight=5)
        
        question1 = Question(id = 1, value="how well did you do this round", 
                            options=[very_good_option, poor_option, avg_option, good_option, very_good_option])
    
        easy_option = Option(value="easy", weight=1)
        ok_option = Option(value="ok", weight=2)
        difficult_option = Option(value="difficult", weight=3)
        very_difficult_option = Option(value="very difficult", weight=4)

        question2 = Question(id = 2,value="how difficult was this question", 
                            options=[easy_option, ok_option, difficult_option, very_difficult_option])
        
        survey = Survey(title="Sample Survay", description="for testing", questions=[question1, question2])

        survey.display_survey()

        user1 = User(id=1, name="Ushank", email="ushank@example.com")
        user2 = User(id=2, name="kartik", email="kartik@example.com")

        # submitting sum response

        response1 = UserResponse(user=user1, question=[question1, question2], option=[very_good_option, easy_option])
        response2 = UserResponse(user=user2, question=[question1, question2], option=[poor_option, difficult_option])

        survey.submit_response(response1)
        survey.submit_response(response2)

        survey.display_responses()

        print("aggratings")
        print(survey.get_avarage_of_question(1))
        print(survey.get_avarage_of_question(2))
        print(survey.get_avarage_of_user(user1.name))
        print(survey.get_avarage_of_user(user2.name))


