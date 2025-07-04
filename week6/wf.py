with open("manoj.txt",'r') as f1, open("rr.txt",'r') as f2, open("result.txt",'w') as f3:
    f3.write(f1.read() + f2.read())
