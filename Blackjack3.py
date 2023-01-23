import random

class cards:
    #the cards
    suit = ["spades", "clubs", "diamonds", "hearts"]
    rank = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    deck = []
    player_hand = []
    dealer_hand = []
    player_total = 0
    dealer_total = 0
    #create deck 
    def __innit__(deck, self, suit, rank, player_hand, dealer_hand,player_total,dealer_total):
        self.suit = suit
        self.rank = rank
        self.deck = deck
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
        self.player_total = player_total
        self.dealer_total = dealer_total
    
    def create_deck(self):
        for suits in self.suit:
            for ranks in self.rank:
                self.deck.append(ranks + " of "  + suits)

    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def dealing_hand(self, player_hand, dealer_hand):
        player_hand = [self.deck.pop(), self.deck.pop()]
        dealer_hand = [self.deck.pop(), self.deck.pop()]

    def dealing_PC(self, player_hand):
        player_hand = [self.deck.pop()]

    
    def dealing_DC(self):
        dealer_hand = [self.deck.pop()]

    def check_player_value(self):
        for cards in self.player_hand:
            value = card.split()[0]
            if value = "2":
                self.player_total += 2
            elif value = "3":
                self.player_total += 3
            elif value = "4":
                self.player_total += 4
            elif value = "5":
                self.player_total += 5
            elif value = "6":
                self.player_total += 6
            elif value = "7":
                self.player_total += 7
            elif value = "8":
                self.player_total += 8
            elif value = "9":
                self.player_total += 9
            elif value = 10:
                self.player_total += 10
            elif value = "jack":
                value = 10
            elif value = "queen":
                value = 10 
            elif value = "king":
                value = 10
    def ace_decider(self):
        ace_value = input("1 or 11?: ")
        if ace_value = "1":
            self.player_total += 1
        elif ace_value