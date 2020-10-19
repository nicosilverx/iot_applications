import random

card_suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
card_value_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

class Card:
    def __init__(self, suit, value):
        if(card_suit_list.__contains__(suit) and card_value_list.__contains__(value)):
            self.suit = suit
            self.value = value
        else:   
            print("ERROR: Insert a correct suit and value")
            self.suit="null"
            self.value="null"
    def __repr__(self):
        return (f"{self.value} of {self.suit}")

class Deck:
    def __init__(self):
        self.card_deck = []
    def deal(self, *card_list):
        for card in card_list:
            if(self.card_deck.__contains__(card)):
                self.card_deck.remove(card)
            else:
                self.card_deck.append(card)
    def shuffle(self):
        random.shuffle(self.card_deck)
    def __repr__(self):
        str_to_ret = "Deck has: \n"
        for card in self.card_deck:
            str_to_ret += (f"{card.value} of {card.suit}\n")
        return str_to_ret

if __name__=="__main__":
    card1 = Card("Hearts", "J")
    card2 = Card("Diamonds", "4")
    card3 = Card("Spades", "K")
    
    deck1 = Deck()
    deck1.deal(card1, card2, card3)
    print(deck1)

    deck1.shuffle()
    print(deck1)

    deck1.deal(card1)
    print(deck1)