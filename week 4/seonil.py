def create_list(l,n):
    for i in range (n):
        temp = int(input("Enter the elements in the list: "))
        l.append(temp)
    return l
    
n1 = int(input("Enter the size of the list 1: "))
n2 = int(input("Enter the size of the list 2: "))
n3 = int(input("Enter the size of the list 3: "))

l1 = []
l2 = []
l3 = []

l1 = create_list(l1,n1)
print(l1)
l2 = create_list(l2,n2)
print(l2)
l3 = create_list(l3,n3)
print(l3)

def s_ein(l):
    sen = 0
    for i in range (len(l)):
        if(i%2==0):
            sen = sen+l[i]
    return sen
    
se1 = s_ein(l1)
se2 = s_ein(l2)
se3 = s_ein(l3)

sein = se1+se2+se3
print(sein)
    
def s_oil(l):
    son = 0
    for i in range (len(l)):
        if(i%2!=0):
            son = son+l[i]
    return son
    
so1 = s_oil(l1)
so2 = s_oil(l2)
so3 = s_oil(l3)

soil = so1+so2+so3
print(soil)

result = sein*soil
print(result)
