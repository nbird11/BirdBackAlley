class Card:
    # Values 11=j; 12=Q; 13=K; 14=A; 15=jk; 16=JK
    values_enum = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    suits_enum = ["spades", "hearts", "clubs", "diamonds", "joker"]

    def __init__(self, value, suit):
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

    def _get_suit_symbol(self):
        return (
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

    def _get_value_top(self):
        return (
            f"{self.value}"
            if self.value == 10
            else "J "
            if self.value == 11
            else "Q "
            if self.value == 12
            else "K "
            if self.value == 13
            else "A "
            if self.value == 14
            else "jk"
            if self.value == 15
            else "JK"
            if self.value == 16
            else f"{self.value} "
        )

    def _get_value_bottom(self):
        return (
            f"{self.value}"
            if self.value == 10
            else " J"
            if self.value == 11
            else " Q"
            if self.value == 12
            else " K"
            if self.value == 13
            else " A"
            if self.value == 14
            else "jk"
            if self.value == 15
            else "JK"
            if self.value == 16
            else f" {self.value}"
        )

    def __eq__(self, _other):
        return self.suit == _other.suit and self.value == _other.value

    def __repr__(self):
        value = self.value
        suit = self.suit
        return f"Card({value=}, {suit=})"

    def __str__(self):
        lines = ["" for _ in range(7)]
        suit = self._get_suit_symbol()
        value_top = self._get_value_top()
        value_bottom = self._get_value_bottom()

        # Jokers
        if self.suit == "joker":
            # Little joker
            if self.value == 15:
                lines[0] = "┌─────────┐"
                lines[1] = "│jk  j    │"
                lines[2] = "│     o   │"
                lines[3] = "│    k    │"
                lines[4] = "│   e     │"
                lines[5] = "│    r  jk│"
                lines[6] = "└─────────┘"
            # Big joker
            elif self.value == 16:
                lines[0] = "┌─────────┐"
                lines[1] = "│JK  J    │"
                lines[2] = "│     O   │"
                lines[3] = "│    K    │"
                lines[4] = "│   E     │"
                lines[5] = "│    R  JK│"
                lines[6] = "└─────────┘"
            else:
                assert False
            return "\n".join(lines)

        # Regular suits
        if self.value == 2:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}       │".format(value_top)
            lines[2] = "│    {}    │".format(suit)
            lines[3] = "│         │"
            lines[4] = "│    {}    │".format(suit)
            lines[5] = "│       {}│".format(value_bottom)
            lines[6] = "└─────────┘"
        elif self.value == 3:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}       │".format(value_top)
            lines[2] = "│    {}    │".format(suit)
            lines[3] = "│    {}    │".format(suit)
            lines[4] = "│    {}    │".format(suit)
            lines[5] = "│       {}│".format(value_bottom)
            lines[6] = "└─────────┘"
        elif self.value == 4:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}       │".format(value_top)
            lines[2] = "│  {}  {}   │".format(suit, suit)
            lines[3] = "│         │"
            lines[4] = "│  {}  {}   │".format(suit, suit)
            lines[5] = "│       {}│".format(value_bottom)
            lines[6] = "└─────────┘"
        elif self.value == 5:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}       │".format(value_top)
            lines[2] = "│  {}   {}  │".format(suit, suit)
            lines[3] = "│    {}    │".format(suit)
            lines[4] = "│  {}   {}  │".format(suit, suit)
            lines[5] = "│       {}│".format(value_bottom)
            lines[6] = "└─────────┘"
        elif self.value == 6:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}       │".format(value_top)
            lines[2] = "│  {}   {}  │".format(suit, suit)
            lines[3] = "│  {}   {}  │".format(suit, suit)
            lines[4] = "│  {}   {}  │".format(suit, suit)
            lines[5] = "│       {}│".format(value_bottom)
            lines[6] = "└─────────┘"
        elif self.value == 7:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}    {}  │".format(value_top, suit)
            lines[2] = "│      {}  │".format(suit)
            lines[3] = "│  {} {} {}  │".format(suit, suit, suit)
            lines[4] = "│  {}      │".format(suit)
            lines[5] = "│  {}    {}│".format(suit, value_bottom)
            lines[6] = "└─────────┘"
        elif self.value == 8:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}    {}  │".format(value_top, suit)
            lines[2] = "│    {} {}  │".format(suit, suit)
            lines[3] = "│  {}   {}  │".format(suit, suit)
            lines[4] = "│  {} {}    │".format(suit, suit)
            lines[5] = "│  {}    {}│".format(suit, value_bottom)
            lines[6] = "└─────────┘"
        elif self.value == 9:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}    {}  │".format(value_top, suit)
            lines[2] = "│  {}   {}  │".format(suit, suit)
            lines[3] = "│  {} {} {}  │".format(suit, suit, suit)
            lines[4] = "│  {}   {}  │".format(suit, suit)
            lines[5] = "│  {}    {}│".format(suit, value_bottom)
            lines[6] = "└─────────┘"
        elif self.value == 10:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}  {} {}  │".format(value_top, suit, suit)
            lines[2] = "│  {}   {}  │".format(suit, suit)
            lines[3] = "│  {}   {}  │".format(suit, suit)
            lines[4] = "│  {}   {}  │".format(suit, suit)
            lines[5] = "│  {} {}  {}│".format(suit, suit, value_bottom)
            lines[6] = "└─────────┘"
        elif 10 < self.value < 14:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}┌───┐  │".format(value_top)
            lines[2] = "│  |  {}|  │".format(suit)
            lines[3] = "│  |   |  │"
            lines[4] = "│  |{}  |  │".format(suit)
            lines[5] = "│  └───┘{}│".format(value_bottom)
            lines[6] = "└─────────┘"
        elif self.value == 14:
            lines[0] = "┌─────────┐"
            lines[1] = "│{}       │".format(value_top)
            lines[2] = "│         │"
            lines[3] = "│    {}    │".format(suit)
            lines[4] = "│         │"
            lines[5] = "│       {}│".format(value_bottom)
            lines[6] = "└─────────┘"
        else:
            assert False

        return "\n".join(lines)


deck = []
for suit in [suit for suit in Card.suits_enum if suit != "joker"]:
    for value in [value for value in Card.values_enum if value < 15]:
        deck.append(Card(value, suit))
for _ in range(2):
    value += 1
    deck.append(Card(value, "joker"))

[print(card) for card in deck]
