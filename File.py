from MatrixSparseDOK import *

def write_MatrixDOK_to_txt(mat: MatrixSparseDOK):
    spmatrix_is_error(mat, "Write to file invalid arguments")
    compressed = mat.compress()
    stri = "("
    for i in range(len(compressed)):
        if isinstance(compressed[i],tuple):
            stri += "("
            for j in range(len(compressed[i])):
                    stri += str(compressed[i][j]) + ","
            stri = stri[:-1]
            stri += "),"
        else:
            stri += str(compressed[i]) + ","

    stri = stri[:-1]
    stri += ")"

    print("string:"+stri)
    with open('informacao.rb', 'w') as f:
        f.write(stri)
        
def read_MatrixDOK_from_txt():
    f = open('informacao.rb', 'r')
    stri = f.read()
    if stri[-1] != ')' or stri[0] != '(':
        raise ValueError("1File doesnt contain a compressed matrix")
    main_list = []
    i = 1
    while(i <= (len(stri) - 2)):
        i2=i
        if(stri[i] == '('):
            print("1 "+stri[i])
            i+=1
            list = []
            while(i <= (len(stri) - 2)):
                if(stri[i] == ')'):
                    main_list.append(list)
                    print("2 "+stri[i])
                    i+=1
                    break
                elif(stri[i] == ','):
                    print("v "+stri[i])
                    i+=1
                    continue
                elif(check_if_num(stri[i])):
                    stri_temp = ""
                    val = 0
                    while(stri[i] == '.' or check_if_num(stri[i])):
                        if(stri[i] == '.'):
                            val = 1
                        stri_temp += stri[i]
                        print("3 "+stri[i])
                        i+=1
                    if(val == 1):
                        list.append(float(stri_temp))
                    else:
                        list.append(int(stri_temp))
                else:
                    raise ValueError("2File doesnt contain a compressed matrix")
        if(i <= (len(stri) - 2)):
            if(stri[i] != ',' and check_if_num(stri[i]) == 0):
                raise ValueError("3File " + stri[i-1] + " " + stri[i] + " doesnt contain a compressed matrix")
            else:
                print("4 "+stri[i] + " " + stri[i+1])
                i+=1
                if(check_if_num(stri[i]) == 1):
                    stri_temp = ""
                    val = 0
                    while(stri[i] == '.' or check_if_num(stri[i]) ==1):
                        if(stri[i] == '.'):
                            val = 1
                        stri_temp += stri[i]
                        print("5 "+stri[i])
                        i+=1
                    if(val == 1):
                        main_list.append(float(stri_temp))
                    else:
                        main_list.append(int(stri_temp))
    um = tuple(main_list[0])
    dois = main_list[1]
    tres = tuple(main_list[2])
    quatro = tuple(main_list[3])
    cinco = tuple(main_list[4])
    compressed = (um,dois,tres,quatro,cinco)
    
    return MatrixSparseDOK.decompress(compressed)

def check_if_num(stri: str):
    if(stri == '0' or stri == '1' or stri == '2' or stri == '3' or stri == '4' or stri == '5' or stri == '6' or stri == '7' or stri == '8' or stri == '9'):
        return 1
    return 0
m1 = MatrixSparseDOK()
m1_data = {(6, 3): 6.3, (7, 4): 7.4, (8, 1): 8.1, (8, 2): 8.2, (8, 5): 8.5}
for key, value in m1_data.items():
    m1[Position(key[0], key[1])] = value
write_MatrixDOK_to_txt(m1)
res = read_MatrixDOK_from_txt()
raise ValueError((res==m1))