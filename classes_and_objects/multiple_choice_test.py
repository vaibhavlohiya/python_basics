"""
A python program to create a multiple choice test.
"""

from question import Question

question_prompt = [
    'What colour are apples?\n (a) Red/Green\n (b) Blue\n (c) White\n\n',
    'What colour are bananas?\n (a) Magenta\n (b) Yellow\n (c) Cyan\n\n',
    'What colour are Avacados?\n (a) Black\n (b) Purple\n (c) Green\n\n'
]

questions = [
    Question(question_prompt[0], 'a'),
    Question(question_prompt[1], 'b'),
    Question(question_prompt[2], 'c')
]

def run_test(quests):
    score = 0
    for question in quests:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    return 'You got ' + str(score) + '/' + str(len(questions)) + ' correct'

print(run_test(questions))