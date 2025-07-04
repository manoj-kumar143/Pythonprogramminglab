r = int(input("enter the number of rows: "))
c = int(input("enter the number of coloums: "))
matrix = []
for i in range(r):
    row = []
    for j in range(c):
        n = int(input("enter the number: "))
        row.append(n)
    matrix.append(row)
print(matrix)

matrix2 = []
for i in range(r):
    row = []
    for j in range(c):
        n = int(input("enter the number: print(multi)
"))
        row.append(n)
    matrix2.append(row)
print(matrix2)

multi = []
for i in range(r):
    row=[]
    for j in range(c):
        temp=0
        for k in range(r):
            temp += matrix[i][k] * matrix2[k][j]
        row.append(temp)
    multi.append(row)
print(multi)
