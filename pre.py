from itertools import count
from pickle import LIST


flg = 0


print ("test")

while flg == 0 :
    n = int(input("How many number (5-10): "))
    if n>=5 and n<=10 :
        print (n)
        flg = 1
    else :
        print ("Must be 5 to 10 ")
lst = []
for i in range (1,n+1) :
    num = int(input("Number %d = "%i))
    lst.append(num)
print ("Number =" ,lst) 

count = 1
nsum = 0
for i in lst :
    print ("Number %d ==> %d"%(count,i))
    if i%2==0 :
        print ("\t%d is added." %i)
        nsum += i
    else :
        print ("\t%d is add number and it is not added." %i)
    count += 1
print("Total sum of even number is %d."%nsum)