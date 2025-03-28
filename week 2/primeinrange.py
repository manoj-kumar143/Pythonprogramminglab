n = int(input("enter the last number: "))
for i in range(2,n):
    flag = 0
    for j in range(2,i):
        if(i%j==0):
            flag = 1
            
    if (flag==0):
        print(i,end = " ")
