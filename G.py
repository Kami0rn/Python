while True :
    num = int(input("How many integer (5-10)"))
    if num>=5 and num<=10 :
        break
    else :
        print("Must be 5 to 10")
lst = []
count = 1

for i in range (0,num) :
    n = int(input("Number %d = "%count))
    lst.append(n)
    count +=1
print(lst)
sum = 0
for x in lst:
    if x%2==0 :
        print("%d is added."%x)
        sum += x
    else :
        print("%d is odd nuber and it is not added"%x)
print("Total sum of even number is %d"%sum)
        
        
        