import constants as c
from card import Card

from pprint import pprint


class _Cursor:
    def __init__(self):
        self.lines = ["" for _ in range(7)]
        self.chars_per_line_per_card = []


_cursor = _Cursor()


def add_card(card: Card):
    global _cursor

    if _cursor.lines[0]:
        for i in range(7):
            _cursor.lines[i] = _cursor.lines[i][
                : len(_cursor.lines[i]) - len(f"{c.B_RESET}{c.F_RESET}")
            ]
            _cursor.chars_per_line_per_card[-1] = [
                leng - len(f"{c.B_RESET}{c.F_RESET}")
                for leng in _cursor.chars_per_line_per_card[-1]
            ]
        lines = ["" for _ in range(7)]
    else:
        lines = [f"{c.B_WHITE}{c.F_BLACK}" for _ in range(7)]
    suit = card._get_suit_symbol()
    value_top = card._get_value_top()
    value_bottom = card._get_value_bottom()

    # Jokers
    if card.suit == "joker":
        # Little joker
        if card.value == 15:
            lines[0] += "┌─────────┐"
            lines[1] += "│jk  j    │"
            lines[2] += "│     o   │"
            lines[3] += "│    k    │"
            lines[4] += "│   e     │"
            lines[5] += "│    r  jk│"
            lines[6] += "└─────────┘"
        # Big joker
        elif card.value == 16:
            lines[0] += "┌─────────┐"
            lines[1] += "│JK  J    │"
            lines[2] += "│     O   │"
            lines[3] += "│    K    │"
            lines[4] += "│   E     │"
            lines[5] += "│    R  JK│"
            lines[6] += "└─────────┘"
        else:
            assert False

        lines = [line + c.B_RESET + c.F_RESET for line in lines]

        return lines

    # Regular suits
    if card.value == 2:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}       │".format(value_top)
        lines[2] += "│    {}{}{}    │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[3] += "│         │"
        lines[4] += "│    {}{}{}    │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[5] += "│       {}│".format(value_bottom)
        lines[6] += "└─────────┘"
    elif card.value == 3:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}       │".format(value_top)
        lines[2] += "│    {}{}{}    │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[3] += "│    {}{}{}    │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[4] += "│    {}{}{}    │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[5] += "│       {}│".format(value_bottom)
        lines[6] += "└─────────┘"
    elif card.value == 4:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}       │".format(value_top)
        lines[2] += "│  {}{}{}  {}{}{}   │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[3] += "│         │"
        lines[4] += "│  {}{}{}  {}{}{}   │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[5] += "│       {}│".format(value_bottom)
        lines[6] += "└─────────┘"
    elif card.value == 5:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}       │".format(value_top)
        lines[2] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[3] += "│    {}{}{}    │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[4] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[5] += "│       {}│".format(value_bottom)
        lines[6] += "└─────────┘"
    elif card.value == 6:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}       │".format(value_top)
        lines[2] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[3] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[4] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[5] += "│       {}│".format(value_bottom)
        lines[6] += "└─────────┘"
    elif card.value == 7:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}    {}{}{}  │".format(
            value_top,
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[2] += "│      {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[3] += "│  {}{}{} {}{}{} {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[4] += "│  {}{}{}      │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[5] += "│  {}{}{}    {}│".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            value_bottom,
        )
        lines[6] += "└─────────┘"
    elif card.value == 8:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}    {}{}{}  │".format(
            value_top,
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[2] += "│    {}{}{} {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[3] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[4] += "│  {}{}{} {}{}{}    │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[5] += "│  {}{}{}    {}│".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            value_bottom,
        )
        lines[6] += "└─────────┘"
    elif card.value == 9:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}    {}{}{}  │".format(
            value_top,
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[2] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[3] += "│  {}{}{} {}{}{} {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[4] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[5] += "│  {}{}{}    {}│".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            value_bottom,
        )
        lines[6] += "└─────────┘"
    elif card.value == 10:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}  {}{}{} {}{}{}  │".format(
            value_top,
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[2] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[3] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[4] += "│  {}{}{}   {}{}{}  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[5] += "│  {}{}{} {}{}{}  {}│".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
            value_bottom,
        )
        lines[6] += "└─────────┘"
    elif 10 < card.value < 14:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}┌───┐  │".format(value_top)
        lines[2] += "│  │  {}{}{}│  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[3] += "│  │   │  │"
        lines[4] += "│  │{}{}{}  │  │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[5] += "│  └───┘{}│".format(value_bottom)
        lines[6] += "└─────────┘"
    elif card.value == 14:
        lines[0] += "┌─────────┐"
        lines[1] += "│{}       │".format(value_top)
        lines[2] += "│         │"
        lines[3] += "│    {}{}{}    │".format(
            c.F_RED if card.suit in ["hearts", "diamonds"] else "",
            suit,
            c.F_BLACK if card.suit in ["hearts", "diamonds"] else "",
        )
        lines[4] += "│         │"
        lines[5] += "│       {}│".format(value_bottom)
        lines[6] += "└─────────┘"
    else:
        assert False

    lines = [line + c.B_RESET + c.F_RESET for line in lines]

    assert len(lines) == len(_cursor.lines) == 7

    _cursor.chars_per_line_per_card.append([len(line) for line in lines])
    for i in range(7):
        _cursor.lines[i] += lines[i]

    # for line in _cursor.lines:
    #     print(line)
    # pprint(_cursor.lines)
    # pprint(_cursor.characters_per_card)


# TODO
def draw_lines():
    global _cursor

    while _cursor.lines[0]:
        if len(_cursor.chars_per_line_per_card) > c.CARDS_PER_LINE:
            # lines = [
            #     line[: sum(_cursor.chars_per_line_per_card[: c.CARDS_PER_LINE])]
            #     for line in _cursor.lines
            # ]
            # _cursor.lines = [
            #     line[sum(_cursor.chars_per_line_per_card[: c.CARDS_PER_LINE]) :]
            #     for line in _cursor.lines
            # ]
            # pprint(lines)
            # # print("\n".join(lines))
            ...
        else:
            print("\n".join(_cursor.lines))
            _cursor.lines = ["" for _ in range(7)]

    _cursor.lines = ["" for _ in range(7)]
