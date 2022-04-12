#spmatrix = [int, dict[tuple[int,int],float]]
position = tuple [int,int]

def position_create(row: int, col: int) -> position:
    if isinstance(row,int) and isinstance(col,int) and row>=0 and col >=0:
        return (row,col)
    else:
        raise ValueError('position_create: invalid arguments')

def position_is(pos: position) -> bool:
    #print("pos beginning: ",pos)
    #print("type pos beginning: ", type(pos))
    if isinstance(pos, tuple) and len(pos) == 2:
        row,col = pos
       # print(row, col)
        #print(type(row),type(col))
        if isinstance(row, int) and row >= 0 and isinstance(col, int) and col >= 0:
            #print("valid pos")
            return True
        else:
            #print("2 values in tuple, but not int and >= 0")
            return False
    else:
        #print("not a tuple or tuple without only 2 values")
        return False

def position_row(pos: position) -> int:
    if position_is(pos):
        row,col = pos
        return row
    else:
        raise ValueError('position_row: invalid arguments')

def position_col(pos: position) -> int:
    if position_is(pos):
        row,col = pos
        return col
    else:
        raise ValueError('position_col: invalid arguments')

def position_equal(pos1: position, pos2: position) -> bool:
    if position_is(pos1) and position_is(pos2):
        row1,col1 = pos1
        row2,col2 = pos2
        if row1 == row2 and col1 == col2:
            return True
        else:
            return False
    else:
        raise ValueError('position_equal: invalid arguments')

def position_str(pos: position) -> str:
    if position_is(pos):
        return str(pos)
    else:
        raise ValueError('position_str: invalid arguments')

#position_create(-1,-1)
#position_is(position_create(-1, -1))
#position_row(position_create(1, 2))
#position_is((3, 1))
#position_is((3.0, 0))
#position_is((3, 1.0))
#position_is((-1,-1))
#position_is((3,-1))
#position_is((-1,2))
#position_is((3,1,2))