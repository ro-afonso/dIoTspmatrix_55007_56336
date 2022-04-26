from __future__ import annotations
from ctypes import Union
from turtle import pos

#position = tuple[int, int]


class Position:
    _pos = tuple[int, int]

    def __init__(self, row: int, col: int):
        if not ((isinstance(row,int)) and row >= 0) or not((isinstance(col,int)) and col >= 0):
            raise ValueError('__init__() invalid arguments')
        self._pos = row, col

    def __str__(self):
        return str(self._pos)     #Isto fui eu que tentei, antes estava pass

    def __getitem__(self, item: int) -> int:
        if not(isinstance(item, int) and (0 <= item <= 1)):
            raise ValueError('__getitem__() invalid arguments')
        return self._pos[item]

    def __eq__(self, other: Position):  #Devemos adicionar -> Bool ?
        #print(self, "Esta é a pos:",other)
        position_is_error(other, '__eq__() invalid arguments')
        return self._pos == other._pos   #usamos other._pos para não comparar tuple com object Position

    def get_pos(self)-> tuple(int,int):
        return self._pos

def position_is_error(pos: Position, str: str):
    if not(position_is(pos)):
        raise ValueError(str)

def position_is(pos: Position) -> bool:
    #print("pos type: ",pos.__class__.__name__)
    #if it's a tuple with only 2 int values then convert to Position type
    if isinstance(pos,tuple) and len(pos) == 2:
        row,col = pos
        if isinstance(row, int) and row >= 0 and isinstance(col, int) and col >= 0:
            return True
    if not(isinstance(pos,Position)):
        #print(1)
        return False
    if not ((isinstance(pos[0],int)) and pos[0] >= 0) or not((isinstance(pos[1],int)) and pos[1] >= 0):
        #print(2)
        return False
    #print(3)
    return True

def create_pos(pos: Union[tuple, Position], str: str) -> Position:
    p = pos
    if(isinstance(pos, tuple) and len(pos) == 2):
        try:
            p = Position(pos[0], pos[1])
        except:
            raise ValueError(str)
    elif not(isinstance(pos, Position)):
        raise ValueError(str)
    return p 


#Position(1, 2, 3)