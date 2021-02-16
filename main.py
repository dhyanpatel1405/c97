import random
print('Number_guessing_game')
number=random.randint(1,9)
chances=0
print('Guess_a_number')

while chances<5:
    guess=int(input('Enter_your_guess'))

    if guess==number:
        print('U won  WOO')
        break
    else:
        print('U lose  LOL')
        