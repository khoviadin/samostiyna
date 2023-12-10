rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
#1)
mat = [[int(input()) for i in range(cols)] for j in range(rows)]

#2)
for el in mat:
    print(el)
    
#3)
def mult_mat(mat1,mat2):
    res = [[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            s = 0
            for k in range(len(mat2)):
                s += mat1[i][k] * mat2[k][j]
            res[i][j] = s
    return res
mat1 = [[1,2],[3,4],[5,6]]
mat2 = [[1,2,3],[4,5,6]]

assert mult_mat(mat1,mat2) == [[9, 12, 15], [19, 26, 33], [29, 40, 51]]

#4) 
def mat_vec(mat,vec):
    return [[mat[j][i] * vec[i] for i in range(len(mat[0]))] for j in range(len(mat))]
vec = [2,3]

assert mat_vec(mat1,vec) == [[2, 6], [6, 12], [10, 18]]

#5) Напевно так само як і пункт 4

#6)
def per_row1(mat,n):
    res = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
    for i in range(n,len(mat)+n):
        if i > len(mat)-n-1:
            i -= len(mat)
        res[i+n] = mat[i]
    return res
mat1 = [[1,2,12],[3,4,34],[5,6,56],[7,8,78],[9,10,910]]

assert per_row1(mat1,2) == [[7, 8, 78], [9, 10, 910], [1, 2, 12], [3, 4, 34], [5, 6, 56]]

def per_row2(mat,n,k):
    mat[n], mat[k] = mat[k], mat[n]
    return mat

assert per_row2(mat1,2,3) == [[1, 2, 12], [3, 4, 34], [7, 8, 78], [5, 6, 56], [9, 10, 910]]

#7)
def per_col1(mat,n):
    res = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
    for j in range(len(mat[0])):
        for i in range(len(mat)):
            if j > len(mat[0])-n-1:
                j -= len(mat[0])
            res[i][j+n] = mat[i][j]
    return res

assert per_col1(mat1,2) == [[2, 12, 1], [4, 34, 3], [8, 78, 7], [6, 56, 5], [10, 910, 9]]

def per_col2(mat,n,k):
    res = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
    for j in range(len(mat[0])):
        for i in range(len(mat)):
            if j == n:
                res[i][j] = mat[i][k]
            elif j == k:
                res[i][j] = mat[i][n]
            else:
                res[i][j] = mat[i][j]
    return res

assert per_col2(mat1,1,2) == [[1, 12, 2], [3, 34, 4], [7, 78, 8], [5, 56, 6], [9, 910, 10]] 

#8)
def row_mat(mat,n):
    return mat[n]

assert row_mat(mat1,1) == [3, 4, 34]
#9)
def vec_num(vec,n):
    return [vec[i]*n for i in range(len(vec))]

assert vec_num(vec,20) == [40, 60]

#10)
def sub_vec_mat(vec,mat):
    return [[mat[j][i] - vec[i] for i in range(len(mat[0]))] for j in range(len(mat))]

mat1 = [[1,2],[3,4],[5,6]]

assert sub_vec_mat(vec,mat1) == [[-1, -1], [1, 1], [3, 3]]

#а)
def tri_mat(mat):
    for i in range(min(len(mat), len(mat[0]))):
        max_val = 0
        r_max = i
        for x in range(i, len(mat)):
            val = abs(mat[x][i])
            if val > max_val:
                max_val = val
                r_max = x
        per_row2(mat,i,r_max)
        for j in range(i + 1, len(mat)):
            c = mat[j][i] / mat[i][i]
            for k in range(i, len(mat[0])):
                mat[j][k] -= c * mat[i][k]
    return mat

assert tri_mat([[11,12,13],[21,22,23],[31,32,33]]) == [[31, 32, 33], [0.0, 0.6451612903225801, 1.2903225806451601], [0.0, 0.0, 0.0]]

#b)
def rank_mat(mat):
    new_mat = tri_mat(mat)
    c = 0
    for el in new_mat:
        s = 0
        for x in el:
            s += x
        if s != 0:
            c += 1
    return c

assert rank_mat([[11,12,13],[21,22,23],[31,32,33]]) == 2

#c)
def vizn_mat(mat):
    new_mat = tri_mat(mat)
    res = 1
    for i in range(0,rank_mat(mat)):
        res *= new_mat[i][i]
    return res

assert vizn_mat([[11,12,13],[21,22,23],[31,32,33]]) == 19.999999999999982




