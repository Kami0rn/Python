from ast import If, While

while True :
    num = int (input("Please input number (2-9)"))
    if num<=9 and num>=2 :
        break
    else :
        print("Please re-enter the number")
lst= []
lt = []
cnt = 1 
for i in range(0,num) :
    nm = str(input("Please enter name number%d"%cnt))
    lst.append(nm)
    cnt += 1

#j=0
#for i in lst :
    #print (lst[j])
for x in lst:
    print (x.title())

j+=1


