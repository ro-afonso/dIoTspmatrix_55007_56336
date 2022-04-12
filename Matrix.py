from __future__ import annotations
from abc import ABC, abstractmethod
from Position import *


class Matrix(ABC):

    @abstractmethod
    def __getitem__(self, item):
        raise NotImplementedError

    @abstractmethod
    def __setitem__(self, key, value):
        raise NotImplementedError

    @abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @abstractmethod
    def __next__(self):
        raise NotImplementedError

    @abstractmethod
    def __copy__(self):
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self._add_number(other)
        if isinstance(other, Matrix):
            return self._add_matrix(other)
        raise ValueError('_add__ invalid argument')

    @abstractmethod
    def _add_number(self, other: [int, float]) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def _add_matrix(self, val: Matrix) -> Matrix:
        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self._mul_number(other)
        if isinstance(other, Matrix):
            return self._mul_matrix(other)
        raise ValueError('__mul__ invalid argument')

    @abstractmethod
    def _mul_number(self, other: [int, float]) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def _mul_matrix(self, other: Matrix) -> Matrix:
        raise NotImplementedError

    def __str__(self):
        pass

    @abstractmethod
    def dim(self) -> tuple[Position, ...]:
        raise NotImplementedError

    @abstractmethod
    def row(self, row: int) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def col(self, col: int) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def diagonal(self) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def transpose(self) -> Matrix:
        raise NotImplementedError
