#using:
#https://www.geeksforgeeks.org/python-__iter__-__next__-converting-object-iterator/
#https://www.pythontutorial.net/python-oop/python-__eq__/
#https://stackoverflow.com/questions/61657240/iterating-over-dictionary-using-getitem-in-python
#https://datagy.io/python-replace-item-in-list/

from __future__ import annotations
from typing import Union
from MatrixSparse import *
from Position import *

spmatrix = dict[Position, float]

def spmatrix_is_error(mat: MatrixSparseDOK, error: str):
    if not(spmatrix_is(mat)):
        raise ValueError(error)

"""spmatrix_is_error(mat, error):
Checks if the matrix is a valid sparse matrix.
Raises a ValueError if the matrix is not valid.
"""
def spmatrix_is(mat: MatrixSparseDOK) -> bool:
    if not(isinstance(mat, MatrixSparseDOK)) or not(isinstance(mat._zero,(float,int))) or not(isinstance(mat._items, dict)):
        print(1)
        return False
    for k in mat._items.keys():
        if not(position_is(k)):
            print(3)
            return False
        if not(isinstance(mat[k],(float,int)) and mat[k] != mat.zero): #,float
            print(4)
            return False
    return True
    """spmatrix_is(mat):
    Checks if the matrix is a valid sparse matrix.
    Args:
        mat (_type_, optional): matrix to be checked
    Returns:
        bool: True if the matrix is valid, False otherwise.
    """

def compressed_vector_is(compressed_vector: compress) -> bool:
    if not(isinstance(compressed_vector[0][0],int) and isinstance(compressed_vector[0][1],int)):
        return False
    if(len(compressed_vector[0])) != 2:
        return False
    for i in compressed_vector[0]:
        if not(isinstance(i,int)):
            return False
    if not(isinstance(compressed_vector[1], float)):
        return False
    if not(isinstance(compressed_vector[2],tuple) and isinstance(compressed_vector[3],tuple) and isinstance(compressed_vector[4],tuple)):
        return False
    for l in range(2, len(compressed_vector)+1):
        for i in compressed_vector[2]:
            if not(isinstance(i,float) or isinstance(i,int)):
                return False
    return True
"""compressed_vector_is(compressed_vector):
Checks if the compressed vector is a valid compressed vector.
Args:
    compressed_vector (_type_, optional): comprressed vector of a matrix
Returns:
    bool: True if the compressed vector is valid, False otherwise.
"""
class MatrixSparseDOK(MatrixSparse):
    _items = spmatrix
    
    def get_items(self) -> spmatrix:
        return self._items
    """get_items(self) -> spmatrix:
    Returns the items of the matrix.
    Returns:
        spmatrix: The items of the matrix.
    """
    def __init__(self, zero: float = 0):      
        if not ((isinstance(zero,float) or isinstance(zero, int)) ):
            """ and zero >= 0 """
            raise ValueError('__init__() invalid arguments')  #removed matrixsparseDOK
        self._items = {}
        self._zero = zero
    """__init__(self, zero: float = 0):
    Initializes the matrix.
    Args:
        zero (_type_, optional): zero of the matrix. Defaults to 0.
    """
    @property
    def zero(self) -> float:
        return self._zero
    """zero(self) -> float:
    Returns the zero value of the matrix.
    Returns:
        float: The zero value of the matrix."""

    @zero.setter
    def zero(self, val: float):
        self._zero = val
        temp_dict = self._items.copy()
        for k in temp_dict:
            if temp_dict[k] == self._zero:
                del self._items[k]
    """zero(self, val: float):
    Sets the zero value of the matrix.
    Args:
        val (_type_, optional): zero new valor. Defaults to 0.
    """

    def __copy__(self):
        m = MatrixSparseDOK(self.zero)
        for k in self._items:
                m[k] = self._items[k]
        return m
    """__copy__(self):
    Returns a copy of the matrix.
    Returns:
        MatrixSparseDOK: A copy of the matrix."""

    def __eq__(self, other: MatrixSparseDOK):
        if isinstance(other, float):  #this is done because of test_05___eq___(self) in part2
            return False
        spmatrix_is_error(other, "__eq__() invalid arguments") #removed matrixsparseDOK
        #Check if keys are equal
        if self._items.keys() == other._items.keys():  #this seems to be enough, no need to check len()
            if self._items == other._items and self.zero == other.zero:
                return True
            return False
        return False
    """__eq__(self, other: MatrixSparseDOK):
    Checks if the matrix is equal to another matrix.
    Args:
        other (_type_, optional): other matrix to compare
    Returns:
        bool: True if the matrix is equal to another matrix, False otherwise.
    """

    #makes items iterable by returning a value of type dict_keyiterator that yields the dict's keys and can be used with __getitem__
    def __iter__(self):
        #OrderedDict
        return iter(sorted(self._items))   #sorted is needed for equal with 2 dicts with unordered keys
    """__iter__(self):
    Returns an iterator over the matrix.
    Returns:
        dict_keyiterator: An iterator over the matrix."""

    def __next__(self):
        try:
            rv = self.thing.__getitem__(self.i)
        except IndexError:
            raise StopIteration
        self.i += 1
        return rv
    """__next__(self):
    Returns the next item in the matrix.
    Returns:
        dict_keyiterator: The next item in the matrix."""

    def __getitem__(self, pos: Union[Position, position]) -> float:
        pos = create_pos(pos, "__getitem__() invalid arguments")
        position_is_error(pos, "__getitem__() invalid arguments")
        if pos.get_pos() in self._items.keys():    
            return self._items[pos.get_pos()]
        else:
            return self._zero
    """__getitem__(self, pos: Union[Position, position]):
    Returns the value of the matrix at the given position.
    Args:
        pos (_type_, optional): position of item.
    Returns:
        float: The value of the matrix at the given position."""

    def __setitem__(self, pos: Union[Position, position], val: Union[int, float]):  #self,key,value
        pos = create_pos(pos, "__setitem__() invalid arguments")
        position_is_error(pos, "__setitem__() invalid arguments")
        if not(isinstance(val, float) or isinstance(val, int)):
            raise ValueError("__setitem__() invalid arguments")
        if val < 0:
            raise ValueError("__setitem__() invalid arguments")
        print()   
        self._items[pos.get_pos()] = val
        if(val == self.zero):
            del self._items[pos.get_pos()]
    """__setitem__(self, pos: Union[Position, position], val: Union[int, float]):
    Sets the value of the matrix at the given position.
    Args:
        pos (_type_, optional): position of the item. 
        val (_type_, optional): valor of the item.
    """

    def __len__(self) -> int:
        return len(self._items)
    """__len__(self) -> int:
    Returns the length of the matrix.
    Returns:
        int: The length of the matrix."""

    def _add_number(self, other: Union[int, float]) -> Matrix:
        if not(isinstance(other, float) or isinstance(other, int)):
            raise ValueError("_add_number() invalid arguments")
        if self.dim():
            print(self.dim())
            m2 = self.__copy__()
            for k in list(self._items.keys()):
                m2[k] += other
            return m2
        return self
    """_add_number(self, other: Union[int, float]) -> Matrix:
    Adds a number to the matrix.
    Args:
        other (_type_, optional): number to add.
    Returns:
        Matrix: The matrix with the number added."""
        
    def _add_matrix(self, other: MatrixSparse) -> MatrixSparse:
        spmatrix_is_error(other, "_add_matrix() invalid arguments")
        if (self._zero != other._zero):
                return False
        
        self_min_dim,self_max_dim = self.dim()
        self_min_row = self_min_dim[0]
        self_max_row = self_max_dim[0]
        self_min_col = self_min_dim[1]
        self_max_col = self_max_dim[1]

        other_min_dim,other_max_dim = other.dim()
        other_min_row = other_min_dim[0]
        other_max_row = other_max_dim[0]
        other_min_col = other_min_dim[1]
        other_max_col = other_max_dim[1]

        if other_min_row > self_min_row:    
            self_max_row = other_min_row    
                                            
        

        m3 = MatrixSparseDOK(self._zero)
        for row in range(self_min_row, self_max_row+1):
                for col in range(self_min_col, self_max_col+1):                    
                    self_value = self.__getitem__((row,col))
                    other_value = other.__getitem__((row,col))
                    if self_value == self._zero:
                        self_value = 0
                    if other_value == other._zero:
                        other_value = 0                    
                    m3[(row,col)] = self_value + other_value
        return m3
    """_add_matrix(self, other: MatrixSparse):
    Adds a matrix to the matrix.
    Args:
        other (_type_, optional): other matrix to add.
    Returns:
        MatrixSparse: The matrix with the matrix added."""

    def _mul_number(self, other: Union[int, float]) -> Matrix:
        if not(isinstance(other, float) or isinstance(other, int)):
            raise ValueError("_add_number() invalid arguments")
        if self.dim():
            m2 = self.__copy__()
            for k in list(self._items.keys()):
                m2[k] *= other
            m2._zero *= other  
            return m2
        return self
    """_mul_number(self, other: Union[int, float]) -> Matrix:
    Multiplies a number to the matrix.
    Args:
        other (_type_, optional): number to multply.
    Returns:
        Matrix: The matrix with the number multiplied."""

    def _mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
        spmatrix_is_error(other, "_mul_matrix() invalid arguments")
        if (self._zero != other._zero):
                raise ValueError('_mul_matrix() incompatible matrices')
        self_min_dim,self_max_dim = self.dim()
        self_min_row = self_min_dim[0]
        self_max_row = self_max_dim[0]
        self_min_col = self_min_dim[1]
        self_max_col = self_max_dim[1]

        other_min_dim,other_max_dim = other.dim()
        other_min_row = other_min_dim[0]
        other_max_row = other_max_dim[0]
        other_min_col = other_min_dim[1]
        other_max_col = other_max_dim[1]

        #When we multiply 2 matrices:
        #The number of columns of the 1st matrix must equal the number of rows of the 2nd matrix
        #And the result will have the same number of rows as the 1st matrix,
        #and the same number of columns as the 2nd matrix

        m3 = MatrixSparseDOK(self._zero)
        for row in range(self_max_row-self_min_row + 1):
            for col in range(other_max_col-other_min_col + 1):
                final_value = 0
                num = 0
                for move in range(other_max_row-other_min_row + 1):
                    self_value = self.__getitem__(Position(row + self_min_row, move+self_min_col))
                    other_value = other.__getitem__(Position(move+other_min_row ,col+ other_min_col))  
                    if self_value == self._zero:
                        self_value = 0
                        num+=1
                    if other_value == other._zero:
                        other_value = 0   
                        num+=1   
                    final_value += self_value * other_value
                if num != other_max_row-other_min_row + 1:
                    m3[Position(row+self_min_row,col+other_min_col)] = final_value
        return m3
    """_mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
    Multiplies a matrix with other matrix.
    Args:
        other (_type_, optional): second matrix to multiply.
    Returns:
        MatrixSparse: The matrix with the matrix multiplied."""

    def dim(self) -> tuple[Position, ...]:
        if(len(self._items) == 0):
            return tuple()
        positions = list(self._items.keys())
        min_col = min(pos[1] for pos in positions)
        min_row = min(pos[0] for pos in positions)
        max_col = max(pos[1] for pos in positions)
        max_row = max(pos[0] for pos in positions)
        return (Position(min_row, min_col), Position(max_row, max_col))
    """dim(self) -> tuple[Position, ...]:
    Returns the minimum and maximum position of the matrix.
    Returns:
        tuple[Position, ...]: The minimum and maximum position of the matrix."""

    def row(self, row: int) -> Matrix:
        if not(isinstance(row, int)):
            raise ValueError("row() invalid arguments")
        if row < 0:
            raise ValueError("row() invalid arguments")
        m = MatrixSparseDOK(self.zero)
        keys = list(self._items.keys())
        for num in range(len(keys)):
            if keys[num][0] == row:
                val = self._items[keys[num]]
                m[keys[num]] = val
        return m
    """row(self, row: int) -> Matrix:
    Returns a matrix with the row of the matrix.
    Args:
        row (_type_, optional): row to return.
    Returns:
        Matrix: The matrix with the row."""

    def col(self, col: int) -> Matrix:
        if not(isinstance(col, int)):
            raise ValueError("col() invalid arguments")
        if col < 0:
            raise ValueError("col() invalid arguments")
        m = MatrixSparseDOK(self.zero)
        keys = list(self._items.keys())
        for num in range(len(keys)):
            if keys[num][1] == col:
                val = self._items[keys[num]]
                m[keys[num]] = val
        return m
    """col(self, col: int) -> Matrix:
    Returns a matrix with the column of the matrix.
    Args:
        col (_type_, optional): column to return.
    Returns:
        Matrix: The matrix with the column."""

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
    """diagonal(self) -> Matrix:
    Returns a matrix with the diagonal of the matrix.
    Returns:
        Matrix: The matrix with the diagonal."""

    @staticmethod
    def eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparseDOK:
        if not(isinstance(size, int) and size >= 0 and isinstance(unitary,(float,int)) and isinstance(zero,(float,int))):
            raise ValueError('eye() invalid parameters')
        m1 = MatrixSparseDOK(zero)
        for i in range(size):
            m1[Position(i,i)] = unitary
        return m1

    """eye(size: int, unitary: float = 1.0, zero: float = 0.0) -> MatrixSparseDOK:
    Returns a matrix with the identity of the size.
    Args:
        size (_type_, optional): size of the matrix.
        unitary (_type_, optional): value of the identity.
        zero (_type_, optional): value of the zero.
    Returns:
        MatrixSparseDOK: The matrix with the identity."""

    def transpose(self) -> MatrixSparseDOK:
        if self.dim():                      #if self.dim() returns () then the matrix has no values, so no transpose
            min_dim,max_dim = self.dim()
            min_row = min_dim[0]
            max_row = max_dim[0]
            min_col = min_dim[1]
            max_col = max_dim[1]
            m_transposed = MatrixSparseDOK(self._zero)
            for row in range(min_row, max_row+1):
                for col in range(min_col, max_col+1):
                    m_transposed[(col,row)] = self.__getitem__((row,col))
            return m_transposed
        return self
    """transpose(self) -> MatrixSparseDOK:
    Returns the transpose of the matrix.
    Returns:
        MatrixSparseDOK: The transpose of the matrix."""

    def compress(self) -> compressed:
        if self.sparsity() < 0.5:
            raise ValueError('compress() dense matrix')
        min_dim,max_dim = self.dim()
        min_row = min_dim[0]
        max_row = max_dim[0]
        min_col = min_dim[1]
        max_col = max_dim[1]
        #total_nr_rows = max_row-min_row
        final_values_list = []
        final_rows_list = []
        offset_list = []
        rows_list = []
        for row in range(min_row, max_row+1):
            rows_list.append(row)
            offset_list.append(0)
        most_dense_row = None
        most_dense_row_amount = 0
        while(rows_list):
            for row in rows_list:
                amount = 0
                for value in self.row(row):
                    if value != self._zero:
                        amount += 1
                if most_dense_row == None:
                    most_dense_row = row
                    most_dense_row_amount = amount
                elif amount > most_dense_row_amount:
                    most_dense_row = row
                    most_dense_row_amount = amount

            if not(final_values_list):
                for col in range(min_col,max_col+1):
                    final_values_list.append(float(self[most_dense_row,col]))
                i = 0
                for value in final_values_list:
                    if value != self._zero:
                        final_rows_list.insert(i,most_dense_row)
                    else:
                        final_rows_list.insert(i,self._zero)
                    i+=1 
                rows_list.remove(most_dense_row)
                most_dense_row = None
            else:            
                done = False
                cols_free = True
                extra_cols = False
                temp_offset = 0
                keys_list = []
                for col in range(min_col,max_col+1):
                    keys_list.append((most_dense_row,col))
                while not(done):     
                    temp_final_values_list = final_values_list.copy()
                    temp_final_rows_list = final_rows_list.copy()
                    for k in keys_list:                          
                        if k[1]+temp_offset-min_col > len(final_values_list)-1:                                
                            temp_final_values_list.insert(k[1]+temp_offset-min_col,self.__getitem__((k[0],k[1])))
                            temp_final_rows_list.insert(k[1]+temp_offset-min_col,most_dense_row)
                            extra_cols = True
                        elif final_values_list[k[1]+temp_offset-min_col] != self._zero and self.__getitem__((k[0],k[1])) != self._zero:
                            cols_free = False
                        else:
                            if final_values_list[k[1]+temp_offset-min_col] == self._zero:
                                temp_final_values_list[k[1]+temp_offset-min_col] = self.__getitem__((k[0],k[1]))
                                temp_final_rows_list[k[1]+temp_offset-min_col] = most_dense_row
                    if cols_free:
                        done = True
                    else:
                        temp_offset+=1
                        cols_free = True
                        extra_cols = False
                if extra_cols:
                    final_values_list = temp_final_values_list.copy()
                    final_rows_list = temp_final_rows_list.copy()
                else:
                    for k in keys_list:
                            if self.__getitem__((k[0],k[1])) != self._zero:
                                final_values_list[k[1]+temp_offset-min_col] = self.__getitem__((k[0],k[1]))
                                final_rows_list[k[1]+temp_offset-min_col] = most_dense_row                    
                offset_list[most_dense_row-min_row] = temp_offset
                rows_list.remove(most_dense_row)
                most_dense_row = None
        for i in range(len(final_values_list)):
            if final_values_list[i] == self._zero:
                final_rows_list[i] = -1
        if len(offset_list) == 1:
            offset_tuple = (offset_list[0])
        else:
            offset_tuple = tuple(offset_list)
        mat_c = ((min_row,min_col),float(self._zero),tuple(final_values_list) ,tuple(final_rows_list),offset_tuple)
        return mat_c
    """compress(self) -> compressed:
    Returns the compressed version of the matrix.
    Returns:
        compressed: The compressed version of the matrix."""

    def compressed_is_dense(self):
        if self.is_empty():
            return False
        else:
            return True
    """compressed_is_dense(self) -> bool:
    Returns whether the matrix is dense or not.
    Returns:
        bool: True if the matrix is dense, False otherwise."""

    @staticmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        if not(position_is(compressed_vector[0])):
            raise ValueError('doi() invalid parameters')
        if not(compressed_vector_is(compressed_vector)):
            raise ValueError('doi() invalid parameters')

        try:
            first_row = compressed_vector[0][0]
            first_col = compressed_vector[0][1]
            additional_remove = False
            values_list = list(compressed_vector[2])
            rows_list = list(compressed_vector[3])
            offset_list = list(compressed_vector[4])
            sorted_rows_list = sorted(list(filter((-1).__ne__, rows_list)))
            highest_density_row = max(set(rows_list), key = rows_list.count)
            offset_value = offset_list[pos[0]-first_row]
            final_pos = (pos[0],pos[1]+offset_value)
            for col in range(len(rows_list)):
                if rows_list[col] == pos[0]:
                    if col == pos[1]+offset_value-first_col:   
                        return values_list[col]
        except:
            raise ValueError('doi() invalid parameters')

        return compressed_vector[1]
    """doi(compressed_vector: compressed, pos: Position) -> float:
    Returns the value of the matrix at the given position.
    Parameters:
        compressed_vector: The compressed vector to get the value from.
        pos: The position to get the value from.
    Returns:
        float: The value at the given position."""

    @staticmethod
    def decompress(compressed_vector: compressed) -> MatrixSparse:
        mat_dc = MatrixSparseDOK(compressed_vector[1]) #create mat with compressed_vector's zero
        first_row = compressed_vector[0][0]
        first_col = compressed_vector[0][1]
        additional_remove = False
        rows_list = list(compressed_vector[3])
        offset_list = list(compressed_vector[4])
        sorted_rows_list = rows_list.copy()
        for value in sorted_rows_list:
            if value == -1:
                sorted_rows_list.remove(-1)
        while(len(rows_list) > 0):
            highest_density_row = max(set(rows_list), key = rows_list.count)
            if highest_density_row == -1:
                #ignore -1 and get next highest value in rows_list
                temp_list = rows_list.copy()
                temp_list = list(filter(lambda a: a != -1, temp_list))
                #After the filter, if temp_list is empty, then the mat_dc is complete, so we return it
                if(temp_list):                    
                    highest_density_row = max(set(temp_list), key = temp_list.count)
                    #at the end of this cycle, we remove both -1 and highest value
                    additional_remove = True
                else:
                    return mat_dc
                
            #start with highest density row
            #compressed_vector[3][col] is row while col is collumn
            offset_value = offset_list[highest_density_row - first_row]
            for col in range(len(compressed_vector[3])):
                
                if compressed_vector[3][col] == highest_density_row:
                    mat_dc[compressed_vector[3][col],col+first_col-offset_value] = compressed_vector[2][col]
            rows_list = list(filter(lambda a: a != highest_density_row, rows_list))
            if additional_remove:
                rows_list = list(filter(lambda a: a != -1, rows_list))
                additional_remove = False

        return mat_dc
    """decompress(compressed_vector: compressed) -> MatrixSparse:
    Returns the decompressed version of the matrix.
    Parameters:
        compressed_vector: The compressed vector to get the value from.
    Returns:
        MatrixSparse: The decompressed version of the matrix."""

    def spmatrix_is_square_error(self, str1: str):
        if not(isinstance(str1, str)):
            raise ValueError("spmatrix_is_square_error() invalid arguments")
        keys = list(self._items.keys())
        xs = [k[0] for k in keys]
        ys = [k[1] for k in keys]
        if not(max(xs) == max(ys)):
            raise ValueError(str1)
    """spmatrix_is_square_error(self, str1: str):
    Raises a ValueError if the matrix is not square.
    Parameters:
        str1: The string to raise the ValueError with.
    Raises:
        ValueError: If the matrix is not square."""