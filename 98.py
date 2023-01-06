with open('words.txt') as f:
    words = [w.strip('"') for w in f.read().strip().split(',')]
from collections import *
squares = set()
anagrams = defaultdict(set)
anagram_words = defaultdict(set)
anagram_counts = defaultdict(set)
for word in words:
    anagram_words[tuple(sorted(Counter(word).items()))].add(word)
to_delete = set()
for k, v in anagram_words.items():
    if len(v) == 1:
        to_delete.add(k)
for k in to_delete:
    del anagram_words[k]
words = set()
for v in anagram_words.values():
    if len(v) > 1:
        words |= v
max_len = max(len(w) for w in words)
curr = 1
while len(str(curr ** 2)) <= max_len:
    squares.add(curr**2)
    anagrams[tuple(sorted(Counter(str(curr**2)).items()))].add(curr**2)
    anagram_counts[tuple(sorted(Counter(str(curr**2)).values()))].add(curr**2)
    curr += 1
res = 0
from itertools import product

def get_encoding(word: str, i: int) -> dict[str, str]:
    encoding = {}
    for char, digit in zip(word, str(i)):
        if char in encoding and encoding[char] != digit:
            return {}
        encoding[char] = digit
    return encoding

def can_encode(word: str, i: int, encoding: dict[str, str]) -> bool:
    for char, digit in zip(word, str(i)):
        if encoding.get(char) != digit:
            return False
    return True



for words in anagram_words.values():
    words = list(words)
    for i, word in enumerate(words):
        for word2 in words[i+1:]:
            print(word, word2)
            candidates = anagram_counts[tuple(sorted(Counter(word).values()))]
            for num, num2 in product(candidates, candidates):
                if num == num2:
                    continue
                encoding = get_encoding(word, num)
                max_num = max(num, num2)
                if can_encode(word2, num2, encoding) and max_num > res:
                    res = max_num
print(res)
