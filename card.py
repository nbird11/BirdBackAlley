class Card:
    # Values 11=j; 12=Q; 13=K; 14=A; 15=jk; 16=JK
    values_enum = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    suits_enum = ["spades", "hearts", "clubs", "diamonds", "joker"]

    def __init__(self, value=None, suit=None):
        self.value = value
        self.suit = suit

        # Invalid value
        if self.value not in self.values_enum:
            raise ValueError(f"'{self.value}' is not a vaild value.")

        # Invalid suit
        if self.suit not in self.suits_enum:
            raise ValueError(f"'{self.suit}' is not a valid suit.")

        # Joker case (joker has no suit)
        if self.suit == "joker" and self.value < 15:
            raise ValueError(f"Joker cards should have a value of 15 or 16")

    def __eq__(self, _other):
        return self.suit == _other.suit and self.value == _other.value

    def __repr__(self):
        suit = (
            "\u2660"
            if self.suit == "spades"
            else "\u2665"
            if self.suit == "hearts"
            else "\u2663"
            if self.suit == "clubs"
            else "\u2666"
            if self.suit == "diamonds"
            else ""
        )
        value = (
            "J"
            if self.value == 11
            else "Q"
            if self.value == 12
            else "K"
            if self.value == 13
            else "A"
            if self.value == 14
            else "jk"
            if self.value == 15
            else "JK"
            if self.value == 16
            else self.value
        )
        return f"{value}{suit}"


deck = []
for suit in [suit for suit in Card.suits_enum if suit != "joker"]:
    for value in [value for value in Card.values_enum if value < 15]:
        deck.append(Card(value, suit))
for _ in range(2):
    value += 1
    deck.append(Card(value, "joker"))

print(deck)
