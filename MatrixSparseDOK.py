from __future__ import annotations
from MatrixSparse import *
from Position import *

spmatrix = dict[Position, float]


class MatrixSparseDOK(MatrixSparse):
    _items = spmatrix

    def __init__(self, zero: float = 0.0):
        pass

    def __copy__(self):
        pass

    def __eq__(self, other: MatrixSparseDOK):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __getitem__(self, pos: [Position, position]) -> float:
        pass

    def __setitem__(self, pos: [Position, position], val: [int, float]):
        pass

    def __len__(self) -> int:
        pass

    def _add_number(self, other: [int, float]) -> Matrix:
        pass

    def _add_matrix(self, other: MatrixSparse) -> MatrixSparse:
        pass

    def _mul_number(self, other: [int, float]) -> Matrix:
        pass

    def _mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
        pass

    def dim(self) -> tuple[Position, ...]:
        pass

    def row(self, row: int) -> Matrix:
        pass

    def col(self, col: int) -> Matrix:
        pass

    def diagonal(self) -> Matrix:
        pass

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
