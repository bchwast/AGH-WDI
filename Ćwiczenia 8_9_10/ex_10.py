def det2x2(m, c, r):
    return m[r[0]][c]*m[r[1]][c+1] - m[r[0]][c+1]*m[r[1]][c]
#end def


def det(matrix, col, row_tab):
    sum = 0
    sum_r = 0
    for i, elem in enumerate(row_tab):
        next_row = [0]*(len(row_tab)-1)

        count = 0
        for e in row_tab:
            if e != elem:
                next_row[count] = e
                count += 1
        #end for

        if len(next_row) == 2:
            sum += ((-1)**i) * matrix[elem][col] * det2x2(matrix, col+1, next_row)
        else:
            smol_det = det(matrix, col+1, next_row)
            add = ((-1)**i) * matrix[elem][col] * smol_det
            sum += add
    #end for
    return sum
#end def


matrix = [[5,2,6,2,8], [1,7,3,7,2], [56,8,24,62,6], [64,2,6,8,2], [234,653,32,6,3]]
print(det(matrix, 0, [i for i in range(len(matrix))]))

