class Card:
    values_enum = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    suits_enum = ["spades", "hearts", "clubs", "diamonds", None]
    joker_enum = ["jk", "JK"]

    def __init__(self, value=None, suit=None):
        self.value = value
        self.suit = suit

        # Invalid value
        if self.value not in self.values_enum and self.value not in self.joker_enum:
            raise ValueError(f"'{self.value}' is not a vaild value.")

        # Invalid suit
        if self.suit not in self.suits_enum:
            raise ValueError(f"'{self.suit}' is not a valid suit.")

        # Joker case (joker has no suit)
        if self.value in self.joker_enum and self.suit is not None:
            raise ValueError(f"Joker cards should have a suit of 'None'")

    def __eq__(self, _other):
        return self.suit == _other.suit and self.value == _other.value

    def __repr__(self):
        if self.suit:
            suit = (
                "♠"
                if self.suit == "spades"
                else "♡"
                if self.suit == "hearts"
                else "♣"
                if self.suit == "clubs"
                else "♢"
            )
            return f"{suit}{self.value}"
        else:
            return f"{self.value}"


deck = []
for suit in [suit for suit in Card.suits_enum if suit]:
    for value in Card.values_enum:
        deck.append(Card(value, suit))
for value in Card.joker_enum:
    deck.append(Card(value))


print(deck)
