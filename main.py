import random
import math


wallet = 50
print('you have ' + str(wallet) + '$ in your wallet')

while wallet > 0:
    # Player choose number between 0 and 49
    number = int(input('Choose a number between 0 and 49: '))
    while number < 0 or number > 49:
        number = int(input('Choose a number between 0 and 49 please: '))
    else:
        bet = int(input('Now choose your bet($): '))
        wallet -= bet
        print('You have ' + str(wallet) + '$ in your wallet left')

    # Launch roulette
    roulette = random.randrange(0, 49)
    print('They see me rollin: ' + str(roulette))

    # Check all cases
    # Win case
    if number == roulette:
        bet = bet * 3
        print('You win ' + bet + '$')
        wallet += bet
        print('You have now' + str(wallet) + '$ in you wallet!')
    # Even numbers case
    elif (roulette % 2) == 0 and (number % 2) == 0:
        print('Both numbers are even and have same Black color! You win half of your bet')
        bet = math.round(bet / 2)
        print('You win ' + str(bet) + '$')
        wallet += bet
        print('You have ' + str(wallet) + '$ in your wallet')
    # Odd numbers case
    elif (roulette % 2) != 0 and (number % 2) != 0:
        print('Both numbers are Odd and have same Red color! You win half of your bet')
        bet = round(bet / 2)
        print('You win ' + str(bet) + '$')
        wallet += bet
        print('You have ' + str(wallet) + '$ in your wallet')
    # Loose
    else:
        print('You lost' + str(bet) + '$!')
        wallet -= bet
        if wallet < 0:
            wallet = 0
        print('You have now ' + str(wallet) + '$ in your wallet')
    # Stop loop if player don't have any money left
    if wallet == 0:
        break
        print('You are out of money! GAME OVER')
