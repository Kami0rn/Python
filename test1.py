from traceback import print_tb


while True :
    num = int(input("Please enter number (1-5) : "))
    if num<5 and num>1 :
        break
    else :
        print ("%d is Invalid number please re-enter"%num)
count = 1    
F=[]
L=[]
FN = []
s = 0 
N = "T i as asd"
for i in range (1,num+1) :
    Fname = str(input("Enter Name number %d"%count))
    FN.append(Fname)
    count += 1
    
print(FN.title())
print (*FN ,sep= "\n")
        
'''
    Fname.split()

    f = Fname.split()[0]
    l = Fname.split()[1]
    L.append(l)
    F.append(f)
    print(L)
    print(F)
'''
