from ast import If, While

while True :
    num = int (input("Please input number (1-5)"))
    if num<=5 and num>=1 :
        break
    else :
        print("Invalid number,try again!!!")
lst= []

count = 1 
for i in range(0,num) :
    nm = str(input("Student %d: "%count))
    lst.append(nm)
    count += 1

count2 = 1
for x in lst:
    print ("Student %d:"%count2 + x.title())
    count2+=1




