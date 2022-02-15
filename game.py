'''
To play, > python3 game.py
'''

import blackjack
import os

game = blackjack.Blackjack()
game.makeDeck()

name = input('What\'s your name?')
player = blackjack.Player(name)

dealer = blackjack.Player('Dealer')

for i in range(2):
    player.addCard(game.pullCard())
    dealer.addCard(game.pullCard())

player.showHand()
dealer.showHand()

player_bust = False
while input('Would you like to stay or hit?').lower() != 'stay':
    player.addCard(game.pullCard())
    player.showHand()
    dealer.showHand()
    if player.calcHand() > 21:
        player_bust = True
        print('You lose!')
        break

dealer_bust = False
if not player_bust:
    while dealer.calcHand() < 17:
        dealer.addCard(game.pullCard())
        if dealer.calcHand(False) > 21:
            dealer_bust = True
            print('You win!')
            break

player.showHand()
dealer.showHand(False)

if player_bust:
    print('You busted, better luck next time!')
elif dealer_bust:
    print('The dealer busted, you win!')
elif dealer.calcHand(False) > player.calcHand():
    print('Dealer has higher cards, you lose!')
elif dealer.calcHand(False) < player.calcHand():
    print('You beat the dealer! Congrats!')
else:
    print('You pushed, no one wins!')
