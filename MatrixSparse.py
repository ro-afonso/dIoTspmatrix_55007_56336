from __future__ import annotations
from Matrix import *

position = tuple[int, int]
compressed = tuple[position, float, tuple[float], tuple[int], tuple[int]]


class MatrixSparse(Matrix):
    _zero = float

    def __init__(self, zero):
        if not ((isinstance(zero,float) or isinstance(zero, int)) ):
            raise ValueError('__init__() invalid arguments')
        self._zero = zero

    @property
    def zero(self) -> float:
        return self._zero

    @zero.setter
    def zero(self, val: float):
        if not ((isinstance(val,float) or isinstance(val, int))):
            raise ValueError('__zero__() invalid arguments')
        self._zero = val   


    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    def sparsity(self) -> float:
        dim = self.dim()
        if(len(self) == 0):
            return 1.0
        return 1.0 - (len(self) / ((dim[1][0] - dim[0][0] + 1) * (dim[1][1] - dim[0][1] + 1)))


    @staticmethod
    @abstractmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparse:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def compress(self) -> compressed:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def decompress(compressed_vector: compressed) -> Matrix:
        raise NotImplementedError
