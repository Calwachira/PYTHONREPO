secret_number =20
guess = 0
while guess != secret_number:
    guess=int(input('Guess the number (1-40): '))
    if guess !=secret_number:
        print('Wrong! Try again.')

print ('You got it')