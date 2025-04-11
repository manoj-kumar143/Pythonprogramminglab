def credit(amt,bal,trans):
    bal = bal+amt
    print(amt,"added successfully")
    trans.append(amt)
    return bal,trans

def debit(amt,bal,trans):
    if(bal<amt):
        print("insufficient balance")
    else:
        bal = bal-amt
        print(amt,"sucessfully debited")
        trans.append(-amt)
        return bal,trans

def sb(bal):
    print(bal)
    return bal

bal = 0
trans = []
while True:
    print("welcome to our services")
    print("press 1 to credit")
    print("press 2 to debit")
    print("press 3 to show balance")
    print("press 4 to show last 5 transistion")
    print("press 5 to exit the services")
    
    choice = int(input("Enter the choice: "))
    if(choice==1):
        amt=int(input("Enter the amount to credit: "))
        bal,trans=credit(amt,bal,trans)
    
    if(choice==2):
        amt=int(input("Enter the amount to debit: "))
        bal,trans=debit(amt,bal,trans)
    
    if(choice==3):
        bal=sb(bal)
        print(bal)
