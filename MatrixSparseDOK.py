from __future__ import annotations
from pickle import TRUE
import string
from typing import Union
from MatrixSparse import *
from Position import *

spmatrix = dict[Position, float]

def spmatrix_is_error(mat: MatrixSparseDOK, str: str):
    if not(spmatrix_is(mat)):
        raise ValueError(str)

def spmatrix_is(mat: MatrixSparseDOK) -> bool:
    if not(isinstance(mat, type(MatrixSparseDOK)) and len(mat) == 2) or not(isinstance(mat.zero,(float,int)) and mat[0] >= 0) or not(isinstance(mat.get_items, dict)):
        return False
    for k in list(mat.get_items.keys()):
        if not(position_is(k)):
            return False
        if not(isinstance(mat[k],(float)) and mat[k] != mat.zero): #,float
            return False
    return True

class MatrixSparseDOK(MatrixSparse):
    _items = spmatrix

    def get_items(self) -> spmatrix:
        return self._items

    def __init__(self, zero: float = 0.0):        
        if not ((isinstance(zero,float) or isinstance(zero, int)) and zero >= 0):
            raise ValueError('__init__() invalid arguments')  #removed matrixsparseDOK
        if isinstance(zero, int):
            zero = float(zero)
        self._items = {}
        self._zero = zero
        #print("mat: ",self)

    def __copy__(self):
        return self.copy()

    def __eq__(self, other: MatrixSparseDOK):
        spmatrix_is_error(other, "__eq__() invalid arguments") #removed matrixsparseDOK
        temp = False
        if self._items.keys() == other.get_items.keys():            
            for k in list(self._items.keys()):
                if(self[k] == 
                other[k]):
                    temp == True
            
        if temp == True and self.zero == other.zero:
            return True

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __getitem__(self, pos: Union[Position, position]) -> float:
        pos = create_pos(pos, "__getitem__() invalid arguments")
        position_is_error(pos, "__getitem__() invalid arguments")
        if pos.get_pos() in self._items.keys():    
            return self._items[pos.get_pos()]
        else:
            return self._zero

    def __setitem__(self, pos: Union[Position, position], val: Union[int, float]):
        pos = create_pos(pos, "__setitem__() invalid arguments")
        position_is_error(pos, "__setitem__() invalid arguments")
        if isinstance(val, int):    
            val = float(val)    
        if not(isinstance(val, float)):
            raise ValueError("__setitem__() invalid arguments")
        if val < 0:
            raise ValueError("__setitem__() invalid arguments")    
        self._items[pos.get_pos()] = val
        if(val == self.zero):
            del self._items[pos.get_pos()]

    def __len__(self) -> int:
        return len(self._items)

    def _add_number(self, other: Union[int, float]) -> Matrix:
        if isinstance(other, int):    
            other = float(other)    
        if not(isinstance(other, float)):
            raise ValueError("_add_number() invalid arguments")
        for k in list(self._items.keys()):
            self[k] += other
        self.zero(self.zero + other)
        

    def _add_matrix(self, other: MatrixSparse) -> MatrixSparse:
        spmatrix_is_error(other, "_add_matrix() invalid arguments")
        dim = self.dim()
        dim1 = other.dim()
        y_dim = dim[1][0] - dim[0][0]
        x_dim = dim[1][1] - dim[0][1]
        if not(y_dim == dim1[1][0] - dim1[0][0] and x_dim == dim1[1][1] - dim1[0][1]):
            raise ValueError("_add_matrix() invalid arguments")
        self.zero(self.zero() + other.zero())
        for row in range(y_dim + 1):
            for col in range(x_dim + 1):
                self[Position(dim[0][0] + row, dim[0][1] + col)] += other[Position(dim1[0][0] + row, dim1[0][1] + col)]

    def _mul_number(self, other: Union[int, float]) -> Matrix:
        if isinstance(other, int):    
            other = float(other)    
        if not(isinstance(other, float)):
            raise ValueError("_mul_number() invalid arguments")
        for k in list(self._items.keys()):
            self[k] *= other
        self.zero(self.zero * other)

    def _mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
        pass

    def dim(self) -> tuple[Position, ...]:
        if(len(self._items) == 0):
            return tuple()
        positions = list(self._items.keys())
        min_col = min(pos[1] for pos in positions)
        min_row = min(pos[0] for pos in positions)
        max_col = max(pos[1] for pos in positions)
        max_row = max(pos[0] for pos in positions)
        return (Position(min_row, min_col), Position(max_row, max_col))

    def row(self, row: int) -> Matrix:
        if not(isinstance(row, int)):
            raise ValueError("row() invalid arguments")
        if row < 0:
            raise ValueError("row() invalid arguments")
        m = MatrixSparseDOK(self.zero())
        keys = list(self._items.keys())
        for num in range(len(keys)):
            if keys[num][0] == row:
                val = self._items[keys[num]]
                m[keys[num]] = val
        return m

    def col(self, col: int) -> Matrix:
        if not(isinstance(col, int)):
            raise ValueError("col() invalid arguments")
        if col < 0:
            raise ValueError("col() invalid arguments")
        m = MatrixSparseDOK(self.zero())
        keys = list(self._items.keys())
        for num in range(len(keys)):
            if keys[num][1] == col:
                val = self._items[keys[num]]
                m[keys[num]] = val
        return m

    def diagonal(self) -> Matrix:
        self.spmatrix_is_square_error("diagonal() invalid arguments")
        keys = list(self._items.keys())
        xs = [k[0] for k in keys]
        m = MatrixSparseDOK(self.zero)
        for num in range(1,max(xs) + 1):
                for n in range(len(keys)):
                    if Position(num,num) == keys[n]:
                        val = self._items[Position(num,num)]
                        m[Position(num,num)] = val
        return m

    @staticmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparseDOK:
        pass

    def transpose(self) -> MatrixSparseDOK:
        pass

    def compress(self) -> compressed:
        pass

    @staticmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        pass

    @staticmethod
    def decompress(compressed_vector: compressed) -> MatrixSparse:
        pass

    def spmatrix_is_square_error(self, str1: str):
        if not(isinstance(str1, str)):
            raise ValueError("spmatrix_is_square_error() invalid arguments")
        keys = list(self._items.keys())
        xs = [k[0] for k in keys]
        ys = [k[1] for k in keys]
        if not(max(xs) == max(ys)):
            raise ValueError(str1)