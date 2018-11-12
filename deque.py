# deque not prnounced as de- queue but as deck
# called "double ended queue"

from collections import deque
from string import ascii_letters


def main():
    deck = deque(ascii_letters.upper(), 26)
    print(deck)

    # can remove the items from both ends
    deck.popleft()
    deck.pop()
    print(deck)

    # can add the items to both ends
    deck.appendleft(11)
    deck.append(2)
    print(deck)

    # can rotate the items,
    # the number of times rotation happen last item goes to first position
    # more like deck.appendLeft(deck.pop())
    deck.rotate(3)
    # deck.rotate(3) is equal to these:
    # deck.appendleft(deck.pop())
    # deck.appendleft(deck.pop())
    # deck.appendleft(deck.pop())
    print(deck)


main()
