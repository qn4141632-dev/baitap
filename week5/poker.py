import random

# CARD 
class Card:
    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return str(self)

# ====================== DECK ======================
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

# ====================== HAND ======================
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return " ".join(str(c) for c in self.cards)

# ====================== PLAYER ======================
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def receive_card(self, card):
        self.hand.add_card(card)

    def show_hand(self):
        print(f"{self.name}: {self.hand}")

# POKER GAME
class PokerGame:
    def __init__(self, players):
        self.deck = Deck()
        self.players = [Player(name) for name in players]

    def deal(self, num_cards=2):
        for _ in range(num_cards):
            for player in self.players:
                card = self.deck.draw()
                if card:
                    player.receive_card(card)

    def show_all_hands(self):
        for player in self.players:
            player.show_hand()

# DEMO 
if __name__ == "__main__":
    game = PokerGame(["Quỳnh", "An", "Bình"])
    game.deal(num_cards=2)  # Mỗi người 2 lá bài
    game.show_all_hands()
