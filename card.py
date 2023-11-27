class Card():
    suits_enum = [
        "spades",
        "hearts",
        "clubs",
        "diamonds",
    ]
    values_enum = [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        "J",
        "Q",
        "K",
        "A",
        "jk",
        "JK"
    ]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

        if self.suit not in suits_enum:
            raise ValueError
        if self.value not in values_enum:
            raise ValueError
    