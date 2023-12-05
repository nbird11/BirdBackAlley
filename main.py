from card import Card
import cursor
import constants as c

# import pygame


def main():
    # pygame.init()
    # screen = pygame.display.set_mode((c.WINDOW_RES))
    # clock = pygame.time.Clock()
    # running = True
    # delta = 0

    deck = []
    for suit in [suit for suit in Card.suits_enum if suit != "joker"]:
        for value in [value for value in Card.values_enum if value < 15]:
            deck.append(Card(value, suit))
    for _ in range(2):
        value += 1
        deck.append(Card(value, "joker"))

    cursor.add_card(deck[20])
    cursor.draw_lines()

    # while running:


if __name__ == "__main__":
    main()
