from __future__ import annotations
from turtle import pos

position = tuple[int, int]


class Position:
    _pos = tuple[int, int]

    def __init__(self, row: int, col: int):
        if not ((isinstance(row,int)) and row >= 0) or not((isinstance(col,int)) and col >= 0):
            raise ValueError('position __init__: invalid arguments')
        self._pos = row, col

    def __str__(self):
        return str(self._pos)     #Isto fui eu que tentei, antes estava pass

    def __getitem__(self, item: int) -> int:
        if not(isinstance(item, int) and (0 <= item <= 1)):
            raise ValueError('position __getitem__: invalid arguments')
        return self._pos[item]

    def __eq__(self, other: Position):
        position_is_error(other, 'position __eq__: invalid arguments')
        return self._pos == other

def position_is_error(pos: position, str: str):
    if not(position_is(pos)):
        raise ValueError(str)

def position_is(pos: position) -> bool:
    if not(type(pos) is tuple and len(pos) == 2):
        return False
    if not ((isinstance(pos[0],int)) and pos[0] >= 0) or not((isinstance(pos[1],int)) and pos[1] >= 0):
        return False
    return True