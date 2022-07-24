from question_model import Question
from quizdata import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")












#Class is a blueprint
#How to create classes
#Classes are used to create objects
#can use keyword pass to temporarily bypass errors
#Name of class should have PascalCase where first letter of each word is capitalized


#Syntax
#class Car:

# class User:
#     pass

# user_1 = User()
#How to create an attribute for the class
#user_1.id = 001
#user_1.username = "Aaron"
#An attribute is a variable that is associated with an object
#If you need multiples of objects, you need constructors
#When an object is initialized you can preset things

#Constructor uses the init function   __init__
#Special method with special function
#Normally used to initialize the attribute
#We create the starting values for our attributes
#Is called everytime you create a new object from the class
#Attributes are just things the object will have
#How to set attributes

# class Car:
#     def __init__(self, seats):
#         self.seats = seats



# class User:

#     def __init__(self):
#         print("new user being created...")

# user_1 = User()


# class User:
#     #name of parameter is usually the same as the name of the attribute
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1



# user_1 = User("001", "aaron")
# user_2 = User("002", "jack")

# user_1.follow(user_2)

# print(user_1.id)
# print(user_1.following)
# print(user_1.followers)

# print(user_2.following)
# print(user_2.followers)

#We can also create methods
#Attributes are things the object has
#Method is things objects does

#Method
#When a function is attached to an object, it's called a method

# class Car:
#     def enter_race_mode():
#         self.seats = 2

#Methods always need a self parameter

#Quiz game

#Model question
#Question object with text attribute and answer attribute
#Attributes should be initialized with a value when a new question is created
#new_q = Question()