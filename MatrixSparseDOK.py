#https://www.geeksforgeeks.org/python-__iter__-__next__-converting-object-iterator/
#https://www.pythontutorial.net/python-oop/python-__eq__/
#https://stackoverflow.com/questions/61657240/iterating-over-dictionary-using-getitem-in-python

from __future__ import annotations
from pickle import TRUE
import string
from typing import OrderedDict, Union, final
from MatrixSparse import *
from Position import *

spmatrix = dict[Position, float]

def spmatrix_is_error(mat: MatrixSparseDOK, error: str):
    if not(spmatrix_is(mat)):
        raise ValueError(error)

def spmatrix_is(mat: MatrixSparseDOK) -> bool:
    #print("len(mat): ",len(mat))
    #print("mat type correct?: ",isinstance(mat, MatrixSparseDOK)) 
    #print("mat zero type correct?: ",isinstance(mat.zero, (float,int)))
    #print("mat items dict type correct?: ",isinstance(mat._items, dict))
    #mat._zero
    #mat.zero
    #removed len as mat now only has the dict and changed type(MatrixSparseDOK) to MatrixSparseDOK
    if not(isinstance(mat, MatrixSparseDOK)) or not(isinstance(mat._zero,(float,int))) or not(isinstance(mat._items, dict)):
        print(1)
        return False
    #print(1.5)
    for k in mat._items.keys():
        #print("key: ",k)
        #print("key type: ",type(k))
        if not(position_is(k)):
            print(3)
            return False
        if not(isinstance(mat[k],(float,int)) and mat[k] != mat.zero): #,float
            print(4)
            return False
    print("spmatrix_is True")
    return True

class MatrixSparseDOK(MatrixSparse):
    _items = spmatrix

    def get_items(self) -> spmatrix:
        return self._items

    def __init__(self, zero: float = 0):        #removed zero: float = 0
        #print("zero type: ",type(zero))
        if not ((isinstance(zero,float) or isinstance(zero, int)) ):
            """ and zero >= 0 """
            raise ValueError('__init__() invalid arguments')  #removed matrixsparseDOK
        """ if isinstance(zero, int):
            zero = float(zero) """
        #print("zero init dok: ",zero)
        self._items = {}
        self._zero = zero
        #print("mat: ",self)

    @property
    def zero(self) -> float:
        return self._zero

    @zero.setter
    def zero(self, val: float):
        print("ENTROU ZERO")
        MatrixSparse.zero.fset(self, val)
        temp_dict = self._items.copy()
        for k in temp_dict:
            if temp_dict[k] == self._zero:
                del self._items[k]

    def __copy__(self):
        m = MatrixSparseDOK(self.zero)
        for k in self._items:
                m[k] = self._items[k]
        return m

    def __eq__(self, other: MatrixSparseDOK):
        if isinstance(other, float):  #this is done because of test_05___eq___(self) in part2
            return False
        print("Entrou __eq__ spmatrix")
        spmatrix_is_error(other, "__eq__() invalid arguments") #removed matrixsparseDOK
        #temp = False
        print("before self.keys == other.keys")
        print(self._items.keys())
        #Check if keys are equal
        if self._items.keys() == other._items.keys():  #this seems to be enough, no need to check len()
            print("self.keys == other.keys")
            """ it = self.__iter__()
            it2 = other.__iter__()
            it2 = iter(self)
            print(it)
            print(it2)  """
            """ for key in self:
                print(key, self[key], end=" ")
            print("\n")
            for key in other:
                print(key, other[key], end=" ") """
            if self._items == other._items and self.zero == other.zero:
                return True
            """if self.zero == other.zero:
                key_found = False
                for key in self:
                    #if not(self[key] == other[key]):
                      #  return False
                    for i in range(len(self)):
                        if self[key] == other[i]:
                            key_found = True
                    if key_found == False:
                        return False
                    key_found = False
                return True """
            #Nah
            """ for (k,v), (k2,v2) in zip(self._items(), other._items()):
                print(k, v)
                print(k2, v2) """
            #Given that all keys and values are equal, lastly we check if both mat's zeros are equal
            """ if self.zero == other.zero:
                    return True """
            return False
        return False

    #makes items iterable by returning a value of type dict_keyiterator that yields the dict's keys and can be used with __getitem__
    def __iter__(self):
        #OrderedDict
        return iter(sorted(self._items))   #sorted is needed for equal with 2 dicts with unordered keys

    def __next__(self):
        print("NEXT")
        try:
            rv = self.thing.__getitem__(self.i)  #thing seams unecessary
        except IndexError:
            print("UH OH")
            raise StopIteration
        self.i += 1
        return rv
    
    def __getitem__(self, pos: Union[Position, position]) -> float:
        pos = create_pos(pos, "__getitem__() invalid arguments")
        position_is_error(pos, "__getitem__() invalid arguments")
        if pos.get_pos() in self._items.keys():    
            return self._items[pos.get_pos()]
        else:
            return self._zero
    #uncomment to get 20 errors in Part1!
    """ def __getitem__(self,key):        
        print("key type: ",key.__class__.__name__)
        if str(key.__class__.__name__) == "Position":
            row = key[0]
            col = key[1]
            newkey = (row,col)
            newkey = key._pos
            print("newkey Position: ",newkey)
        else:
            newkey = key
            print("newkey not Position: ",newkey)
        return self._items[newkey] """

    def __setitem__(self, pos: Union[Position, position], val: Union[int, float]):  #self,key,value
        #print("Entrou setitem")
        pos = create_pos(pos, "__setitem__() invalid arguments")
        position_is_error(pos, "__setitem__() invalid arguments")
        """ if isinstance(val, int):    
            val = float(val)   """  
        if not(isinstance(val, float) or isinstance(val, int)):
            raise ValueError("__setitem__() invalid arguments")
        if val < 0:
            raise ValueError("__setitem__() invalid arguments")
        print()   
        self._items[pos.get_pos()] = val
        if(val == self.zero):
            del self._items[pos.get_pos()]
        """ if key in self and isinstance(dict.__getitem__(self, key), Position):
            dict.__getitem__(self, key).thingy = value
        else:
            dict.__setitem__(self, key, value) """

    def __len__(self) -> int:
        return len(self._items)

    def _add_number(self, other: Union[int, float]) -> Matrix:
        """ if isinstance(other, int):    
            other = float(other)  """   
        if not(isinstance(other, float) or isinstance(other, int)):
            raise ValueError("_add_number() invalid arguments")
        #print("self before add:",self)
        #m2 = MatrixSparseDOK(self._zero+other)
        if self.dim():
            print(self.dim())
            #print("self before add:",self)
            #m2 = MatrixSparseDOK(self._zero*other)
            m2 = self.__copy__()
            for k in list(self._items.keys()):
                #m2[k] = self[k] + other
                m2[k] += other
            print("self after add:",self)
            print("other in add:",other)
            #m2._zero += other  
            return m2
        return self
        #print("m2 =",m2)
        #return m2
        #new_zero = self._zero + other
        #print("NEW ZERO:",new_zero)
        #self.zero(new_zero)            #This doesn't work
        #MatrixSparse.zero.fset(self, new_zero)
        #return 
        
    def _add_matrix(self, other: MatrixSparse) -> MatrixSparse:
        spmatrix_is_error(other, "_add_matrix() invalid arguments")
        if (self._zero != other._zero):
                return False
        """ dim = self.dim()
        dim1 = other.dim()
        y_dim = dim[1][0] - dim[0][0]
        x_dim = dim[1][1] - dim[0][1]
        if not(y_dim == dim1[1][0] - dim1[0][0] and x_dim == dim1[1][1] - dim1[0][1]):
            raise ValueError("_add_matrix() invalid arguments")
        self._zero = self._zero + other._zero#self.zero(self.zero() + other.zero())
        for row in range(y_dim + 1):
            for col in range(x_dim + 1):
                if self[Position(dim[0][0] + row, dim[0][1] + col)] != self._zero or other[Position(dim1[0][0] + row, dim1[0][1] + col)] != self._zero:
                    print("m1: ",self[Position(dim[0][0] + row, dim[0][1] + col)])
                    self[Position(dim[0][0] + row, dim[0][1] + col)] += other[Position(dim1[0][0] + row, dim1[0][1] + col)]
                #else:
                    #self[Position(dim[0][0] + row, dim[0][1] + col)] = self[Position(dim[0][0] + row, dim[0][1] + col)]
        m2 = self.__copy__()
        return m2 """
        self_min_dim,self_max_dim = self.dim()
        print("self matr dim from",(self_min_dim[0],self_min_dim[1]),"to",(self_max_dim[0],self_max_dim[1]))
        self_min_row = self_min_dim[0]
        self_max_row = self_max_dim[0]
        self_min_col = self_min_dim[1]
        self_max_col = self_max_dim[1]

        other_min_dim,other_max_dim = other.dim()
        print("other matr dim from",(other_min_dim[0],other_min_dim[1]),"to",(other_max_dim[0],other_max_dim[1]))
        other_min_row = other_min_dim[0]
        other_max_row = other_max_dim[0]
        other_min_col = other_min_dim[1]
        other_max_col = other_max_dim[1]

        if other_min_row > self_min_row:    #For 2nd test
            self_max_row = other_min_row    #self matr dim from (1, 1) to (1, 3)
                                            #other matr dim from (2, 1) to (2, 3)
        
        """ if other_max_row > self_max_row:   #This might be the correct one actually
            self_max_row = other_max_row """   

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
                    print("row,col = ",(row,col))
                    print("self value = ",self.__getitem__((row,col)))
                    print("other value =",other.__getitem__((row,col)))
                    print("m3 value =",m3[(row,col)])
        print("FINAL m3:",m3)
        return m3

    def _mul_number(self, other: Union[int, float]) -> Matrix:
        """ if isinstance(other, int):    
            other = float(other)   """  
        """ if not(isinstance(other, float) or isinstance(other, int)):
            raise ValueError("_mul_number() invalid arguments")
        for k in list(self._items.keys()):
            self[k] *= other
        self.zero(self.zero * other) """
        if not(isinstance(other, float) or isinstance(other, int)):
            raise ValueError("_add_number() invalid arguments")
        if self.dim():
            print("self before add:",self)
            #m2 = MatrixSparseDOK(self._zero*other)
            m2 = self.__copy__()
            for k in list(self._items.keys()):
                #m2[k] = self[k] + other
                m2[k] *= other
            print("self after add:",self)
            print("other in add:",other)
            m2._zero *= other  
            return m2
        return self

    def _mul_matrix(self, other: MatrixSparse) -> MatrixSparse:
        spmatrix_is_error(other, "_mul_matrix() invalid arguments")
        #TODO verificar se as matrizes sao multiplicaveis
        if (self._zero != other._zero):
                raise ValueError('_mul_matrix() incompatible matrices')
        self_min_dim,self_max_dim = self.dim()
        print("self matr dim from",(self_min_dim[0],self_min_dim[1]),"to",(self_max_dim[0],self_max_dim[1]))
        self_min_row = self_min_dim[0]
        self_max_row = self_max_dim[0]
        self_min_col = self_min_dim[1]
        self_max_col = self_max_dim[1]

        other_min_dim,other_max_dim = other.dim()
        print("other matr dim from",(other_min_dim[0],other_min_dim[1]),"to",(other_max_dim[0],other_max_dim[1]))
        other_min_row = other_min_dim[0]
        other_max_row = other_max_dim[0]
        other_min_col = other_min_dim[1]
        other_max_col = other_max_dim[1]

        """ if other_max_row > self_max_row:    #For 2nd test
            self_max_row = other_max_row    #self matr dim from (1, 1) to (1, 3)
                                            #other matr dim from (2, 1) to (2, 3)

        if other_max_col > self_max_col:    #For 2nd test
            self_max_col = other_max_col

        print("self min row:",self_min_row)
        print("self max row",self_max_row)
        print("other min row:",other_min_row)
        print("other max row:",other_max_row)

        print("self min col:",self_min_col)
        print("self max col",self_max_col)
        print("other min col:",other_min_col)
        print("other max col:",other_max_col) """

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
        m = MatrixSparseDOK(self.zero)
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
        m = MatrixSparseDOK(self.zero)
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
        if not(isinstance(size, int) and size >= 0 and isinstance(unitary,(float,int)) and isinstance(zero,(float,int))):
            raise ValueError('eye() invalid parameters')
        m1 = MatrixSparseDOK(zero)
        for i in range(size):
            m1[Position(i,i)] = unitary
        return m1

    def transpose(self) -> MatrixSparseDOK:
        print("self.dim =",self.dim())
        if self.dim():                      #if self.dim() returns () then the matrix has no values, so no transpose
            min_dim,max_dim = self.dim()
            print("matr dim from",(min_dim[0],min_dim[1]),"to",(max_dim[0],max_dim[1]))
            min_row = min_dim[0]
            max_row = max_dim[0]
            min_col = min_dim[1]
            max_col = max_dim[1]
            """ total_rows = max_dim[0] - min_dim[0] + 1
            total_collumns = max_dim[1] - min_dim[1] + 1
            print("total_rows =",total_rows)
            print("total_collumns =",total_collumns) """
            m_transposed = MatrixSparseDOK(self._zero)
            for row in range(min_row, max_row+1):
                for col in range(min_col, max_col+1):
                    print("get item transposed: ",self.__getitem__((row,col)))
                    #if self.__getitem__((row,col)) != self._zero:                  #is this if necessary?
                    #    m_transposed[(row,col)] = self.__getitem__((row,col))      #it hasn't been so far...
                    m_transposed[(col,row)] = self.__getitem__((row,col))
            print("final m_transposed:\n",m_transposed)
            return m_transposed
        return self

    def compress(self) -> compressed:
        pass

    @staticmethod
    def doi(compressed_vector: compressed, pos: Position) -> float:
        pass

    @staticmethod
    def decompress(compressed_vector: compressed) -> MatrixSparse:
        #TODO Check if compressed_vector has a valid format
        """ for i in range(len(compressed_vector)):
            print(compressed_vector[i]) """
        mat_dc = MatrixSparseDOK(compressed_vector[1]) #create mat with compressed_vector's zero
        first_row = compressed_vector[0][0]
        first_col = compressed_vector[0][1]
        print("first col:",first_col)
        additional_remove = False
        rows_list = list(compressed_vector[3])
        offset_list = list(compressed_vector[4])
        sorted_rows_list = sorted(list(filter((-1).__ne__, rows_list)))
        print("sorted set offset values: ",sorted_rows_list)
        while(len(rows_list) > 0):
            print("BEGIN rows_list:",rows_list)
            highest_density_row = max(set(rows_list), key = rows_list.count)
            print("highest density row: ",highest_density_row)
            if highest_density_row == -1:
                #ignore -1 and get next highest value in rows_list
                temp_list = rows_list.copy()
                temp_list = list(filter((-1).__ne__, temp_list))
                #After the filter, if temp_list is empty, then the mat_dc is complete, so we return it
                if(temp_list):                    
                    highest_density_row = max(set(temp_list), key = temp_list.count)
                    #at the end of this cycle, we remove both -1 and highest value
                    additional_remove = True
                else:
                    return mat_dc
                
            #start with highest density row
            #compressed_vector[3][col] is row while col is collumn
            print("highest:",highest_density_row)
            print("offset_list:",offset_list)
            print("sorted set offset values: ",sorted_rows_list)
            offset_value = offset_list[highest_density_row - first_row]
            print("offset value:",offset_value)
            for col in range(len(compressed_vector[3])):
                #print("HUH: HUH")
                print("cv col",col,"=",compressed_vector[3][col])
                
                if compressed_vector[3][col] == highest_density_row:
                    print("col:",col)
                    print("first col:",first_col)
                    print("offset value:",offset_value)                    
                    print("final col:",col+first_col-offset_value)
                    print("value:",compressed_vector[2][col])
                    print("row:",compressed_vector[3][col])
                    mat_dc[compressed_vector[3][col],col+first_col-offset_value] = compressed_vector[2][col]
            print("mat_dc:")
            print(mat_dc)
            #remove highest_density_row from rows_list
            rows_list = list(filter((highest_density_row).__ne__, rows_list))
            #if -1 was found, remove it
            if additional_remove:
                rows_list = list(filter((-1).__ne__, rows_list))
                additional_remove = False
            #remove last value of offset_list using pop()
            #offset_list.pop()

        return mat_dc

    def spmatrix_is_square_error(self, str1: str):
        if not(isinstance(str1, str)):
            raise ValueError("spmatrix_is_square_error() invalid arguments")
        keys = list(self._items.keys())
        xs = [k[0] for k in keys]
        ys = [k[1] for k in keys]
        if not(max(xs) == max(ys)):
            raise ValueError(str1)

""" mat = MatrixSparseDOK()
print("len test: ",len(mat))
print("mat teste: ",mat) """

""" m1 = MatrixSparseDOK()
print("HUH")
m1_data = {(2, 3): 2.3, (1, 3): 1.3, (2, 2): 2.2, (1, 2): 1.2, (2, 1): 2.1, (1, 1): 1.1}
for key, value in m1_data.items():
    m1[Position(key[0], key[1])] = value
print("HUH2")
test = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
print(m1)
test_list = list(test)
i = 0
for pos in m1:
    #print(m1[pos])
    #print(m1_data[test_list[i]])
    m1.__eq__(m1_data[test_list[i]])
    i += 1 """