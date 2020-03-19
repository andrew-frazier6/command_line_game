

total_questions = 25
correct_answers = 0
incorrect_answers = 0


def flash_game()


for x in questions:
    user = input(f"x['front-of-card]")
    if user == x['back-of-card']:
        print("correct!")
        correct_answers += 1
        total_questions -= 1
    elif user != x['back-of-card']:
        print("my goodness you need help")
        incorrect_answers += 1
        total_questions -= 1
