from __future__ import annotations
from typing import Union

#position = tuple[int, int]


class Position:
    _pos = tuple[int, int]

    def __init__(self, row: int, col: int):
        if not ((isinstance(row,int)) and row >= 0) or not((isinstance(col,int)) and col >= 0):
            raise ValueError('__init__() invalid arguments')
        self._pos = row, col
    """__init__(self, row: int, col: int) -> Position:
    Parameters:
        row: number of row
        col: number of column
    Returns:
        Position object
    Raises:
        ValueError: if row or col is not an integer or if row or col is negative"""

    def __str__(self):
        return str(self._pos)    
    """__str__(self) -> str:
    Returns:
        string representation of the position"""

    def __getitem__(self, item: int) -> int:
        if not(isinstance(item, int) and (0 <= item <= 1)):
            raise ValueError('__getitem__() invalid arguments')
        return self._pos[item]
    """__getitem__(self, item: int) -> int:
    Parameters:
        item: 0 or 1
    Returns:
        row or column of the position"""

    def __eq__(self, other: Position)  -> bool: 
        other = create_pos(other, '__eq__() invalid arguments')
        return self._pos == other._pos   #usamos other._pos para não comparar tuple com object Position
    """__eq__(self, other: Position) -> bool:
    Parameters:
        other: Position object
    Returns:
        True if the positions are equal, False otherwise"""

    def get_pos(self)-> tuple(int,int):
        return self._pos
    """get_pos(self) -> tuple(int,int):
    Returns:
        tuple with the row and column of the position"""

    def __hash__(self) -> int:
        return hash(self._pos)
    """__hash__(self) -> int:
    Returns:
        hash of the position"""

def position_is_error(pos: Position, str: str):
    if not(position_is(pos)):
        raise ValueError(str)
"""position_is_error(pos: Position, str: str)
Parameters:
    pos: Position object
    str: string of the error
Raises:
    ValueError: if pos is not a Position object or if pos is not a tuple with 2 int values"""

def position_is(pos: Position) -> bool:
    #if it's a tuple with only 2 int values then convert to Position type
    if isinstance(pos,tuple) and len(pos) == 2:
        row,col = pos
        if isinstance(row, int) and row >= 0 and isinstance(col, int) and col >= 0:
            return True
    if not(isinstance(pos,Position)):
        return False
    if not ((isinstance(pos[0],int)) and pos[0] >= 0) or not((isinstance(pos[1],int)) and pos[1] >= 0):
        return False
    return True
"""position_is(pos: Position) -> bool:
Parameters:
    pos: Position object
Returns:
    True if pos is a Position object, False otherwise"""

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
"""create_pos(pos: Union[tuple, Position], str: str) -> Position:
Parameters:
    pos: tuple or Position object
    str: string of the error
Raises:
    ValueError: if pos is not a tuple with 2 int values or if pos is not a Position object"""