#https://stackoverflow.com/questions/45037977/get-the-types-of-the-keys-in-a-dictionary
#https://stackoverflow.com/questions/29218750/what-is-the-best-way-to-remove-a-dictionary-item-by-value-in-python
#https://github.com/microsoft/pyright/issues/1321
#https://stackoverflow.com/questions/53781109/python-typing-union-of-subscriptable-type
#https://www.geeksforgeeks.org/python-program-to-find-the-key-of-maximum-value-tuples-in-a-dictionary/
#https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
#https://www.geeksforgeeks.org/python-program-to-find-tuples-with-positive-elements-in-list-of-tuples/
#https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
from typing import Union
from position_ric import *
import sys

for i in range(len(sys.path)):
    print(sys.path[i])
pos = position
spmatrix = [float, dict[pos,float]] #1st float is the spcmatrix's zero  ,  2nd float is the value in each pos

def spmatrix_create(zero: float = 0) -> spmatrix:
    if isinstance(zero,float) or isinstance(zero,()) or isinstance(zero,int):
        if isinstance(zero,int):
            print("IS INT WHAT")
            return [float(zero), {}]   # 0 (int) is converted to 0.0 (float) to keep the spmatrix structure
        elif isinstance(zero,float):
            print("not 0 zero: ",zero)
            return [zero, {}]
        else:
            print("0 zero: ",zero)
            return [0,{}]
    else:
        raise ValueError('spmatrix_create: invalid arguments')

def spmatrix_is(mat: spmatrix) -> bool:
    if isinstance(mat, list) and len(mat) == 2 and type(mat[0]) == float and type(mat[1]) == dict: 
        print(mat)      
        #Check if all keys are tuples        
        #key_types = set(type(k) for k in mat[1].keys())    #Also works
        key_list = [*mat[1]]   #this '*' is called unpacking and works with any object that is iterable, such as dict.keys()
        #print("KEY LIST: ",key_list)
        key_types = set(map(type, key_list))
        if len(key_types) == 0:
            #print("Empty dictionary, return True")
            return True
        elif(len(key_types) == 1) and key_types == {tuple}:
            #print("tuple keys only")
            #check if all positions' values are of type float
            value_types = set(map(type, mat[1].values()))
            if(len(value_types) == 1) and value_types == {float}:
                #print("float values only")
                #check if all positions are valid and values are != from mat_zero
                for i in range(len(key_list)):
                    if position_is(key_list[i]) == False or mat[1][key_list[i]] == mat[0]:
                        return False
                return True
            else:
                #print("values aren't float only")
                return False
        else:
            #print("keys aren't tuple only")
            return False
    else:
        return False

def spmatrix_zero_get(mat: spmatrix) -> float:
    if spmatrix_is(mat):
        return mat[0]
    else:
        raise ValueError('spmatrix_zero_get: invalid arguments')

def spmatrix_zero_set(mat: spmatrix, zero: float):
    if spmatrix_is(mat) and isinstance(zero, float):
        print("Matrix before: ",mat)
        mat[1] = {key:val for key, val in mat[1].items() if val != zero}
        mat[0] = zero
        print("Matrix after: ",mat)
    else:
        raise ValueError("spmatrix_zero_set: invalid arguments")

def spmatrix_value_get(mat: spmatrix, pos: position) -> float:
    #CHECK if pos doesn't exist, then it's a zero. Return the zero of the matrix?
    if spmatrix_is(mat) and position_is(pos):
        if pos in mat[1].keys():
            print(mat[1][pos])
            return mat[1][pos]
        else:
            #if pos doesn't exist, then it's a zero. Return the zero of the matrix
            return mat[0]
    else:
        raise ValueError("spmatrix_value_get: invalid arguments")

def spmatrix_value_set(mat: spmatrix, pos: position, val: float):
    if spmatrix_is(mat) and position_is(pos) and (isinstance(val, float) or isinstance(val, int)):
        if isinstance(val, int):
            val = float(val)
        #check if position exists and val != mat[0]
        if val == mat[0] and pos in mat[1].keys():
            #print("val is zero, removing pos")
            #print(mat)
            mat[1].pop(pos)
            #print(mat)
        else:
            #whether pos in mat[1].keys() or not, same outcome
            #print("val isn't zero, adding or changing entry in dict")
            #print(mat)
            mat[1][pos] = val
            #print(mat)
    else:
        raise ValueError("spmatrix_value_set: invalid arguments")

def spmatrix_copy(mat: spmatrix) -> spmatrix:
    if spmatrix_is(mat):
        mat2 = mat.copy()
        print(mat)
        print(mat2)
        return mat2
    else:
        raise ValueError("spmatrix_copy: invalid arguments")

def spmatrix_dim(mat: spmatrix) -> Union[tuple[position, position], tuple[()]]:
    if spmatrix_is(mat):
        if(mat[1]):
            #this means dict isn't empty
            """ max_mat_pos = max(mat[1].keys())
            min_mat_pos = min(mat[1].keys())
            print("dim min max: ",min_mat_pos, max_mat_pos)
            return [min_mat_pos,max_mat_pos] """
            max_pos_row_related, col = max(mat[1].keys(), key=lambda sub: sub[0])
            row ,max_pos_col_related = max(mat[1].keys(), key=lambda sub: sub[1])
            min_pos_row_related, col2 = min(mat[1].keys(), key=lambda sub: sub[0])
            row2 ,min_pos_col_related = min(mat[1].keys(), key=lambda sub: sub[1])
            #print("min pos row: ",min_pos_row_related)
            #print("min pos col: ",min_pos_col_related)
            #print("max pos row: ",max_pos_row_related)
            #print("max pos col: ",max_pos_col_related)
            min_mat_pos = (min_pos_row_related,min_pos_col_related)
            max_mat_pos = (max_pos_row_related,max_pos_col_related)
            #print("Min spcmatrix pos: ", min_mat_pos)
            #print("Max spcmatrix pos: ",max_mat_pos)
            return [min_mat_pos,max_mat_pos]
        else:
            #this means dict is empty
            #print("Dict is empty")
            return ()
    else:
        raise ValueError("spmatrix_dim: invalid arguments")

def spmatrix_sparsity(mat: spmatrix) -> float:
    #sparcity is the number of zero values in the matrix divided by the total number of elements in the sub_matrix
    #sub_matrix_dimension = (max_row+1 - min_row) * (max_col+1 - min_col)
    #
    if spmatrix_is(mat):
        if(mat[1]):
            #The dict isn't empty
            min_row, min_col = spmatrix_dim(mat)[0]
            max_row, max_col = spmatrix_dim(mat)[1]
            nr_non_zero_elements = len(mat[1].keys())
            sub_matrix_dimension = abs(max_row+1 - min_row) * abs(max_col+1 - min_col)
            nr_zero_elements = sub_matrix_dimension - nr_non_zero_elements       
            sparsity = nr_zero_elements / sub_matrix_dimension
            #shouldn't sparsity be nr_zero_elements / sub_matrix_dimension ?
            #print("sparsity: ",sparsity)
            return sparsity
        else:
            #The dict is empty, so all elements are zero, which means sparcity == 1.0
            return 1.0
    else:
        raise ValueError("spmatrix_sparsity: invalid arguments")

""" def spmatrix_sort(mat: spmatrix) -> list:
    if spmatrix_is(mat):
        #max_pos_row_related, col = max(mat[1].keys(), key=lambda sub: sub[0])
        max_row, max_col = spmatrix_dim(mat)[1]
        sorted_mat = sorted(mat[1].keys(), key=lambda sub: sub[0])
        return sorted_mat
    else:
        raise ValueError("spmatrix_sort: invalid arguments") """

def spmatrix_str(mat: spmatrix, format: str) -> str:
    #TO DO maybe check the actual characters in format to make sure it's suitable for prints?
    if spmatrix_is(mat) and isinstance(format,str):
        #sorted_mat = spmatrix_sort(mat)  #not used but was created anyway
        min_row, min_col = spmatrix_dim(mat)[0]
        max_row, max_col = spmatrix_dim(mat)[1]
        r = min_row
        c = min_col
        mat_str = ''
        while(r <= max_row):
            while(c <= max_col):
                if (r,c) in mat[1].keys():
                    mat_str += format % mat[1][(r,c)]   #deve ser position_create(r,c) ?
                else:
                    mat_str += format % mat[0]
                if c < max_col:
                    mat_str += ' '
                c += 1
            r += 1
            c = min_col
            if r <= max_row:
                mat_str += '\n'         
        #print(mat_str)
        #for k in range(len(mat_str)):
            #print(mat_str[k]+'/')
        print("mat_Str: ",mat_str)
        return(mat_str)
    else:
        raise ValueError("spmatrix_str: invalid arguments")

def spmatrix_row(mat: spmatrix, row: int) -> spmatrix:
    if spmatrix_is(mat) and isinstance(row,int) and row >= 0:
        min_row, min_col = spmatrix_dim(mat)[0]
        max_row, max_col = spmatrix_dim(mat)[1]
        if row <= max_row:
            c = min_col
            mat_row = spmatrix_create(mat[0])
            print("mat_row: ",mat_row)
            for c in range(min_col,max_col+1):
                print("ENTROU")
                if (row,c) in mat[1].keys():
                    mat_row[1][(row,c)] = spmatrix_value_get(mat,(row,c))
            print("mat_row: ",mat_row)
            return mat_row
        else:
            raise ValueError("spmatrix_row: invalid arguments")
    else:
        raise ValueError("spmatrix_row: invalid arguments")

def spmatrix_col(mat: spmatrix, col: int) -> spmatrix:
    if spmatrix_is(mat) and isinstance(col,int) and col >= 0:
        min_row, min_col = spmatrix_dim(mat)[0]
        max_row, max_col = spmatrix_dim(mat)[1]
        if col <= max_col:
            r = min_row
            mat_col = spmatrix_create(mat[0])
            print("mat_col init: ",mat_col)
            for r in range(min_row,max_row+1):
                print("ENTROU")
                if (r,col) in mat[1].keys():
                    mat_col[1][(r,col)] = spmatrix_value_get(mat,(r,col))
                    print(r,col, " is ",spmatrix_value_get(mat,(r,col)))
                else:
                    print(r,col," is a zero")
            print("mat_col end: ",mat_col)
            return mat_col
        else:
            raise ValueError("spmatrix_col: invalid arguments")
    else:
        raise ValueError("spmatrix_col: invalid arguments")

def spmatrix_diagonal(mat: spmatrix) -> spmatrix:
    if spmatrix_is(mat):
        print("mat: ",mat)
        min_row, min_col = spmatrix_dim(mat)[0]
        max_row, max_col = spmatrix_dim(mat)[1]
        keys = list(mat[1].keys())
        rows = [k[0] for k in keys]
        collumns = [k[1] for k in keys]
        max_row = max(rows)
        max_col = max(collumns)
        print("min row col: ", min_row,min_col)
        print("max row col: ", max_row,max_col)
        if max_row == max_col:
            #the mat is square
            c = min_col
            r = min_row
            mat_diag = spmatrix_create(mat[0])
            print("mat_diag created: ",mat_diag)
            print("r,c = ",r,c)
            print("max row, col: ",max_row, max_col)
            for c in range(min_col,max_col+1):
                r=c
                print("ENTROU")
                print("(r,c) = ",r,c)
                if (r,c) in mat[1].keys():
                    print("Entrou rc in mat keys")
                    mat_diag[1][(r,c)] = (spmatrix_value_get(mat,(r,c)))
                print("r,c incremented: ",r,c)
            print("mat_diag final: ",mat_diag)
            return mat_diag
        else:
            raise ValueError("spmatrix_diagonal: matrix not square")
    else:
        raise ValueError("spmatrix_diagonal: invalid arguments")

#spmatrix_create(0)
#spmatrix_is([1,2])
#spmatrix_is(spmatrix_create())
#spmatrix_is([1.0, {(1,2):1.0, (3,4):6}])
#spmatrix_zero_set([3.0, {(1,2):1.0, (3,4):1.0}],1.0)
#spmatrix_is([1.0, {(1,2):1.0, (3,4):'zé'}])
#spmatrix_is([1.0, { (1,2):1, 1:1, 'zé':3, 'zéeeee':6}])
#spmatrix_zero_set([1.0, { (1,2):1.0, 1:1.0, (6,6):3.0, (7,3):6.0}], 1.0)
#spmatrix_value_get([4.0, { (1,2):1.0, (1,1):2.0, (6,6):3.0, (7,3):6.0}], (7,3))
#spmatrix_copy([4.0, { (1,2):1.0, (1,1):2.0, (6,6):3.0, (7,3):6.0}])
#spmatrix_value_set([4.0, { (1,2):1.0, (1,1):2.0, (6,6):3.0, (7,3):6.0}], (1,3), 10.0)
#spmatrix_dim([4.0, {(1,2):1.0, (0,1):2.0, (1,1):56.0, (6,2):56.0, (6,6):3.0, (7,3):6.0, (7,4):9.0, (1,9):2.0}])
#spmatrix_sparsity([4.0, {(1,2):1.0, (1,3):2.0, (0,5):56.0, (6,2):56.0, (6,6):3.0, (7,3):6.0, (7,4):9.0, (1,9):2.0}])
#spmatrix_str([4.0, {(1,2):1.0, (1,3):2.0, (0,5):56.05, (6,2):56.0, (6,3):3.0}], '%.2f')
#spmatrix_dim([4.0, {(3,2):1.0, (6,6):2.0, (2,4):3.0}]) 
""" mat = spmatrix_create()
spmatrix_value_set(mat, position_create(1,1), 12.5)   #if changed to (0,0)
spmatrix_value_set(mat, position_create(2,2), 5.0)    #and (1,1) then works
print(spmatrix_sparsity(mat) == 0.5) """

""" mat = spmatrix_create()
spmatrix_value_set(mat, position_create(1,2), 12.5)   #if changed to (0,1)
spmatrix_value_set(mat, position_create(2,1), 5.0)    #and to (1,0)
spmatrix_value_set(mat, position_create(1,0), 5.0)
spmatrix_zero_set(mat, 12.5)
print(spmatrix_sparsity(mat) == 1.0)  """                #and to 0.5 then works

""" mat = spmatrix_create()
spmatrix_value_set(mat, position_create(0,0), 12.5)      #if changed to (0,0)
spmatrix_value_set(mat, position_create(1,1), 5.0)       #and to (0,0)
mat_row = spmatrix_create()
spmatrix_value_set(mat_row, position_create(0,0), 12.5)  #and to (0,0)
print(spmatrix_row(mat, 0) == mat_row) """                   #and to (0)    works

""" mat = spmatrix_create()
spmatrix_value_set(mat, position_create(0,0), 12.5)
spmatrix_value_set(mat, position_create(1,1), 5.0)
mat_col = spmatrix_create()
spmatrix_value_set(mat_col, position_create(1,1), 5.0)
print(spmatrix_col(mat, 1) == mat_col) """

""" mat = spmatrix_create()
spmatrix_value_set(mat, position_create(0,0), 12.5)
spmatrix_value_set(mat, position_create(1,1), 5.0)
print(spmatrix_diagonal(mat) == mat) """

""" mat = spmatrix_create()
spmatrix_value_set(mat, position_create(0,1), 12.5)
spmatrix_value_set(mat, position_create(1,0), 5.0)
mat_diagonal = spmatrix_create()
print(spmatrix_diagonal(mat) == mat_diagonal) """

#test_spmatrix_diagonal_m2x2_diagonal_zero():
""" mat = spmatrix_create()
spmatrix_value_set(mat, position_create(1,1), 12.5)
spmatrix_value_set(mat, position_create(2,2), 5.0)

print("final diagonal mat: ", spmatrix_diagonal(mat))
print(spmatrix_diagonal(mat) == mat) """

#spmatrix_diagonal([4.0, {(1,1):12.5, (2,2):5.0,}])

#def test_spmatrix_diagonal_m2x2_anti_diagonal_zero():
""" mat = spmatrix_create()
spmatrix_value_set(mat, position_create(1,2), 12.5)
spmatrix_value_set(mat, position_create(2,1), 5.0)
mat_diagonal = spmatrix_create()
print(spmatrix_diagonal(mat) == mat_diagonal) """
""" mat = spmatrix_create()
spmatrix_value_set(mat, position_create(1,1), 12.5)      #if changed to (0,0)
spmatrix_value_set(mat, position_create(2,2), 5.0)       #and (1,1) then works
spmatrix_str(mat, "%.1f")
print(spmatrix_str(mat, "%.1f")== '12.5 0.0\n0.0 5.0') """