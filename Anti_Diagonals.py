def Anti_Diagonals(array,row):
    res=[[0 for _ in range(row)] for _ in range(row*2)]
    r_pos=0
    for x in range(row):
        i,j=0,x
        c_pos=0
        while j>=0 and i<row:
            res[r_pos][c_pos]=array[i][j]
            i+=1
            j-=1
            c_pos+=1
        r_pos+=1
    print(r_pos,c_pos)
    for x in range(row):
        i,j=x,row-1
        c_pos=0
        while i<row and j>=0:
            res[r_pos][c_pos]=array[i][j]
            i+=1
            j-=1
            c_pos+=1
        r_pos+=1
    return res

if __name__ == '__main__':
    row=int(input())
    array=[]
    for _ in range(row):
        col=list(map(int,input().split()))
        array.append(col)
    print(*Anti_Diagonals(array,row))