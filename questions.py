from peewee import *


db = PostgresqlDatabase('trivia', user='postgres',
                        password='', host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Question(BaseModel):
    front = CharField()
    back = CharField()


db.drop_tables([Question])
db.create_tables([Question])


card_data = [
    {
        "front": "In 2005, Nick Swisher finished behind which teammate in the Rookie of the Year voting?",
        "back": "Huston Street"
    }, {
        "front": "Tim Hudson and Barry Zito were members of Oakland's ""Big Three"" pitchers along with what other player?",
        "back": "Mark Mulder"
    }, {
        "front": "Who had 59 wins for the Oakland A's from 1972-1974?",
        "back": "Ken Holtzman"
    }, {
        "front": "Who managed the A's in their first year in Oakland?",
        "back": "Bob Kennedy"
    }, {
        "front": "Which National League team did the Athletics defeat three different times for the World Series championship?",
        "back": "Giants"
    }, {
        "front": "Which year did the franchise move from Philadelphia to Kansas City?",
        "back": "1955"
    }, {
        "front": "The Athletics' Major League debut was on April 26th, 1901, against which team?",
        "back": "Washington Senators"
    }, {
        "front": "In what year did the Atheltics win their first World Series?",
        "back": "1910"
    }, {
        "front": "The Kansas City Athletics' first regular season game resulted in a victory over which team?",
        "back": "Detroit Tigers"
    }, {
        "front": "The Athletics franchise began in 1901. When was their first World Series appearance?",
        "back": "1905"
    }]

for cards in card_data:
    cards = Question(front=cards["front"], back=cards["back"])
    cards.save()


total_answers = 10
correct_answers = 0

welcome_message = "Who doesn't love extremely specific Oakland Athletics questions that aren't multiple choice? Lets get started!"


def flash_game():
    flash_cards = Question.select()
    global correct_answers
    global total_answers
    print(welcome_message)
    for question in flash_cards:
        print(f"{question.front}")
        user_answer = input("")
        if user_answer == question.back:
            correct_answers += 1
            total_answers -= 1
        else:
            total_answers += 1
        if total_answers == 10:
            print(correct_answers)
            user_answer = input("Try again?")
        if user_answer == "yes":
            flash_game()


flash_game()
