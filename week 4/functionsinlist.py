def create_list(l,n):
    for i in range (n):
        temp = int(input("Enter the elements in the list: "))
        l.append(temp)
    return l
    
n1 = int(input("Enter the size of the list: "))
n2 = int(input("Enter the size of the list: "))
n3 = int(input("Enter the size of the list: "))

l1 = []
l2 = []
l3 = []

l1 = create_list(l1,n1)
print(l1)
l2 = create_list(l2,n2)
print(l2)
l3 = create_list(l3,n3)
print(l3)
