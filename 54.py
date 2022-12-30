from dataclasses import dataclass
from collections import Counter

@dataclass
class Hand:
    cards: list["Card"]

    def rank(self):
        suit_counts = Counter(c.suit for c in self.cards).most_common()
        is_straight = max(c.val for c in self.cards) - min(c.val for c in self.cards) == 4
        counts = Counter(c.val for c in self.cards).most_common()
        if suit_counts[0][1] == 5 and is_straight:
            return (10, max(c.val for c in self.cards))
        if counts[0][1] == 4:
            return (8, counts[0][0], counts[1][0])
        if counts[0][1] == 3 and counts[1][1] == 2:
            return (7, counts[0][0], counts[1][0])
        if suit_counts[0][1] == 5:
            return (6,) + tuple(sorted([c.val for c in self.cards], reverse=True))
        if is_straight:
            return (5, max(c.val for c in self.cards))
        if counts[0][1] == 3:
            return (4, counts[0][0]) + tuple(sorted([c.val for c in self.cards], reverse=True))
        if counts[0][1] == 2 and counts[1][1] == 2:
            return (3, max(counts[0][0], counts[1][0]), min(counts[0][0], counts[1][0]), counts[2][0])
        if counts[0][1] == 2:
            return (2, counts[0][0]) + tuple(sorted([c.val for c in self.cards], reverse=True))
        return (0,) + tuple(sorted([c.val for c in self.cards], reverse=True))

@dataclass
class Card:
    val: int
    suit: str

def load_card(token: str) -> Card:
    val = 0
    try:
        val = int(token[:-1])
    except:
        if token[0] == 'J':
            val = 11
        if token[0] == 'Q':
            val = 12
        if token[0] == 'K':
            val = 13
        if token[0] == 'A':
            val = 14
    return Card(val, token[-1:])


def load_hand(line: str) -> tuple[Hand, Hand]:
    cards = line.strip().split()
    return Hand([load_card(c) for c in cards[:5]]), Hand([load_card(c) for c in cards[5:]])

res = 0
with open('poker.txt') as f:
    for line in f.read().strip().splitlines():
        p1, p2 = load_hand(line)

        if p1.rank() > p2.rank():
            res += 1
print(res)
