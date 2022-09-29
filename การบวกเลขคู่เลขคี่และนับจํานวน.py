while True :
    num = int(input("How many number (4-10)"))
    if num>=4 and num<=10 :
        break
    else :
        print ("%d is wrong number please Re-Enter"%num)
count = 1
lst = []
for i in range (0,num) :
    n=int(input("Number[%d]: "%count))
    lst.append(n)
    count +=1
print("All number in the list : ",lst)
sum = 0
even = 0
odd = 0
evenC = 0
oddC = 0
alln = 0
for i in lst :
    sum +=  i
    if i%2==0 :
        even += i
        evenC += 1
    else :
        odd += i
        oddC += 1
    alln += 1

print("Sum of all number is '%d'"%sum)
print("Sum of even number is '%d'"%even)
print("Sum of odd number is '%d'"%odd)
print("Number of all number is '%d'"%alln)
print("Number of even number is'%d'"%evenC)
print("Number of odd number is'%d'"%oddC)
    

