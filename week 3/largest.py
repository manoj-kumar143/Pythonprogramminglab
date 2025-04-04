def Largest(elements):
    largest = 0
    for i in elements:
        largest = max(largest,i)
    return largest
    
elements = []
limit = int(input("enter the length: "))
for i in range(limit):
    temp=int(input("Enter the list: "))
    elements.append(temp)

largest = Largest(elements)
print(largest)
    
