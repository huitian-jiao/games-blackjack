from random import randint

class Blackjack():
    def __init__(self):
        self.deck = []
        self.suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
    def makeDeck(self):
        for suit in self.suits:
            for val in self.values:
                self.deck.append((val, suit))
    def pullCard(self):
        return self.deck.pop(randint(0, len(self.deck)-1))

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

    def showHand(self, dealer_start = True):
        print(f'\n{self.name}')
        print('===============')
        for i in range(len(self.hand)):
            if self.name == 'Dealer' and i == 0 and dealer_start:
                print('- of -')
            else:
                card = self.hand[i]
                print(f'{card[0]} of {card[1]}')
        print(f'Total = {self.calcHand(dealer_start)}')

    def calcHand(self, dealer_start = True):
        total = 0
        aces = 0
        card_values = {i:i for i in range(2, 11)}
        card_values['J'], card_values['Q'], card_values['K'] = 10, 10, 10
        card_values['A'] = 11
        if self.name == 'Dealer' and dealer_start:
            return card_values[self.hand[1][0]]
        for v, s in self.hand:
            if v == 'A':
                aces += 1
            else:
                total += card_values[v]
        for i in range(aces):
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        return total