"""
A python program about while loop.
"""

i = 1
while i <= 10:  # condition 
    print(i)
    i += 1

print('Done with loop')

# Building a guessing game using while loop.

secret_word = 'apple'
guess = ''
no_of_tries = 1
total_tries = 3

while guess != secret_word and no_of_tries <= total_tries:
    guess = input('Enter the secret word: ')
    no_of_tries += 1
    if guess == secret_word:
        print('Congratulations! You have guessed the word correctly.')
    elif no_of_tries > total_tries:
        print('GAME OVER!')
    else: print('Unlucky! Try again.')
