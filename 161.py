"""
idea: represent a n by m board as a bit string int
"""
def triominoes(board_rows: int, board_cols: int):
    res = []
    if board_rows >= 2 and board_cols >= 2:
        """
        ..  ..  .   .
        .    .  .. ..
        """
        res.append(0b11 + (0b1 << board_cols))
        res.append(0b11 + (0b10 << board_cols))
        res.append(0b1 + (0b11 << board_cols))
        res.append(0b10 + (0b11 << board_cols))
    if board_rows >= 3:
        res.append(0b1  + (0b1 << board_cols) +  + (0b1 << (board_cols)*2))
    if board_cols >= 3:
        res.append(0b111)
    return tuple(res)

assert len(triominoes(2,9)) == 5

from functools import lru_cache

@lru_cache(maxsize=None)
def place(board: int, triominoe: int) -> int:
    return 0

@lru_cache(maxsize=None)
def count_tilings(board: int, board_rows: int, board_cols: int, triominoes: tuple[int]) -> int:
    if board == (1 << (board_cols * board_rows)) - 1:
        return 1
    res = 0
    for triominoe in triominoes:
        placement = place(board, triominoe)
    return res

assert count_tilings(0b1111, 2, 2, tuple()) ==  1
