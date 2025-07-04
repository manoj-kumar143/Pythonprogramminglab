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
        n = int(input("enter the number: "))
        row.append(n)
    matrix2.append(row)
print(matrix2)

matrix3 = []
for i in range(r):
    row=[]
    for j in range(c):
        sum = matrix[i][j] + matrix2[i][j]
        row.append(sum)
    matrix3.append(row)
  print(matrix3)
