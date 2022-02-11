from Question import Question
question_prompts = [
    "What would you like for breakfast?\n(a) Oatmeal\n(b) Ham&Egg\n(c) Nothing\n\n",
    "What would you like for lunch?\n(a) Noodles\n(b) Tacos\n(c) Salad\n\n",
    "What would you like for dinner?\n(a) Steak\n(b) Seafood\n(c) Rice\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)