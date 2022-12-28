with open('words.txt') as f:
    words = [w.strip('"').lower() for w in f.read().split(',')]

triangle_nums = [1]

def is_triangle_word(w: str) -> bool:
    score = sum(ord(c) - ord('a') + 1 for c in w)
    while score > triangle_nums[-1]:
        n = len(triangle_nums) + 1
        triangle_nums.append(n * (n+1) // 2)
    return score in triangle_nums


print(len([w for w in words if is_triangle_word(w)]))