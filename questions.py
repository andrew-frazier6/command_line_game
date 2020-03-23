from peewee import *
import random

db = PostgresqlDatabase('Trivia', user='postgres',
                        password='', host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Question(BaseModel):
    question = CharField()
    answer = CharField()


db.drop_tables([Question])
db.create_tables([Question])


card_data = [
    {
        "question": "In 2005, Nick Swisher finished behind which teammate in the Rookie of the Year voting?",
        "answer": "Huston Street"
    }, {
        "question": "Tim Hudson and Barry Zito were members of Oakland's ""Big Three"" pitchers along with what other player?",
        "answer": "Mark Mulder"
    }, {
        "question": "Who had 59 wins for the Oakland A's from 1972-1974?",
        "answer": "Ken Holtzman"
    }, {
        "question": "Who managed the A's in their first year in Oakland?",
        "answer": "Bob Kennedy"
    }, {
        "question": "Which National League team did the Athletics defeat three different times for the World Series championship?",
        "answer": "Giants"
    }, {
        "question": "Which year did the franchise move from Philadelphia to Kansas City?",
        "answer": "1955"
    }, {
        "question": "The Athletics' Major League debut was on April 26th, 1901, against which team?",
        "answer": "Washington Senators"
    }, {
        "question": "In what year did the Atheltics win their first World Series?",
        "answer": "1910"
    }, {
        "question": "The Kansas City Athletics' first regular season game resulted in a victory over which team?",
        "answer": "Detroit Tigers"
    }, {
        "question": "The Athletics franchise began in 1901. When was their first World Series appearance?",
        "answer": "1905"
    }]


def flash_game():
    total_answers = 10
    correct_answers = 0
    incorrect_answers = 0
    for x in card_data:
        user_answer = input(f" {x['question']}? ")
        if user_answer == x['answer']:
            correct_answers += 1
            total_answers += 1
        else:
            incorrect_answers += 1
            total_answers += 1
        if total_answers == 10:
            print(correct_answers)
            user_answer = input("Try again?")
        if user_answer == "yes":
            flash_game()


welcome_message = "Who doesn't love extremely specific Oakland Athletics questions that aren't multiple choice? Lets get started!"
print(welcome_message)
flash_game()
