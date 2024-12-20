from question_model import Question
from data import question_data
from quizz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"],question["correct_answer"]))
    # question_bank.append(Question(question["text"],question["answer"]))

quizz_brain = QuizBrain(question_bank)

while quizz_brain.still_has_question():
    quizz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quizz_brain.score}/{len(quizz_brain.question_list)}")
