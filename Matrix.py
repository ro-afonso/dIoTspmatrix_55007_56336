from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union
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
        #TODO change this to transform into matrix
        if isinstance(other, Matrix):
            if other.zero == self.zero:
                return self._add_matrix(other)
            raise ValueError('_add_matrix() incompatible matrices')
        raise ValueError('_add__ invalid argument')

    @abstractmethod
    def _add_number(self, other: Union[int, float]) -> Matrix:
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
    def _mul_number(self, other: Union[int, float]) -> Matrix:
        raise NotImplementedError

    @abstractmethod
    def _mul_matrix(self, other: Matrix) -> Matrix:
        raise NotImplementedError

    def __str__(self):
        strs = ''
        try:
            dim = self.dim()
            if(dim[0][0] == 1):
                pass
        except IndexError as error:
            return strs
        try:
            for x in range(dim[0][0],dim[1][0] + 1):
                for y in range(dim[0][1],dim[1][1] + 1):
                    strs += str(self[Position(x,y)])
                    if not(y == dim[1][1]):
                        strs += ' '
                strs += '\n'
        except ValueError as error:
            raise ValueError("__str__ invalid argument")
        return strs[:-1]

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
