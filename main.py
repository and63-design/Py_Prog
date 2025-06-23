import random

def run_guess(guess, answer):
    if guess < 11:
        if guess == answer:
            print('You guessed correctly')
            return True
        else:
            #print('Pick a number between 1 and 10')
            return False

if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('Please enter a valid number between 1 and 10')
            continue 