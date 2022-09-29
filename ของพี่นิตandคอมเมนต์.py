from itertools import count


n = int(input("How many integer (5-10)"))       #นําเข้าข้อมูลตัวเลขเพื่อใช้ในการกาําหนดรอบทําซํ้า

lst = []                                        #สร้างสิสต์เปล่าขึ้นมา
for i in range (1,n+1) :                        #กําหนดขอบเขตการทําซํ้าโดยเริ่มที่ 1 และ จบที่ n+1 โดยที่ รอบที่ n+1 จะไม่ถูกทํางานเพราะสิ้นสุด จึงทําให้ ทําถึงแค่รอบ n 
    num = int(input("Number %d ="%i))           #รับค่าตัวเลขไปเก็บที่ num
    lst.append(num)                             #เอาค่า num ไปเพิ่มในลิสต์เปล่า ****โดยนี่คือบรรทัดสุดท้ายของลูป ค่า num ที่เก็บเอาไว้จะถูกเครียร์เพื่อไปรับค่าใหม่ในรอบต่อไปมาเก็บเพิ่มในลิสต์ ****
tp = tuple(lst)                                 #สร้างตัวแปร tp โดยมีทูเปิ้ลอยู่ในตัวแปล tp และในทูเปิ้ล มี ลิสต์ lst อยู๋ข้างใน
print ("number =",tp)                           #แสดงผลทูเปิ้ลที่เก็บได้ทั้งหมด ค่าที่แสดง ถูกเปลี่ยนจากลิสต์เป็นทูเปิ้ล ในบรรทัดที่ 10 

tup = ()                                        #สร้าทูเปิ้ล tp ขึ้นมา
for i in range(1,n+1) :                         #เหมือนบรรทัดที่ 7
    num = int(input ("Number %d ="%i))          #รับค่า มาเก็บไว้ที่ num
    tup += (num,)                               #เอาค่ามาบวกเพิ่ม ใน tup โดยที่การ += จะไม่เป็นการทับค่าเดิมแต่เพิ่มค้่ใหม่เข้าไป สังเกตุ (,) การใส่เช่นนี้จะทําให้ string อยู่ในรูทูเปิ้ล
print ("Number =", tup)                         #แสดงผลทูเปิ้ลที่ได้รับมา

count = 1                                        #กําหนดการนับเริ่มที่ 1
for i in lst :                                   #เริ่มลูปโดยการกําหนด i กับ ตัวแปลต่างๆ เช่นลิสต์ เหมือน การแสกน ในลิสต์ทีละ**ชุดข้อความ**เพื่อในการเช็คค่าต่อไป
    print ("Word %d ==> %s"%(count,i))           #แสดง ลําดับของข้อความที่ กรอก และแสดงข้อความ   
    v = 0                                    #กําหนดจุดเริ่มต้นของการนับสระ ที่ 0
    a = 0                                    #กําหนดจุดเริ่มของการนับตัวอักษรที่ไม่ใช่สระ ที่ 0
    for j in i :                                 #ตั้งแต่บรรทัดนี้จะเป็นส่วนย่อยโดยที่ก่อนหน้าเราจะสนในชุดข้อความ เปลี่ยนมาเป็นแสกนแต่ละตัวอักษรในชุดข้อความนั้นๆ
        if j in "aeiouAEIOU" :                   #จากการแสกนข้างต้นใน บรรทัดที่ 22 นํามาเช็ค่า ว่าเป็นสระหรือไม่
            v+=1                                 #ถ้าใช่ จะเพิ่มค่า ใน V ที่ใช้นับสระ
        else :                                   #นอกเหนือจากกรณีที่เป็นสระแสดงว่าเป็นอักษรธรรมดา
            a+=1                                 #จะเพิ่มค่า a ซึ่งใช้นับตัวอักษรที่ไม่ใช่สระ
    print("%s , vowel = %d and alphabet = %d"%(i,v,a))          #แสดงผลค่าที่ได้ในการนับชุดตัวอักษรนั้นๆ หรือสระ เพื่อไปเริ่มในบรรทัด 20 ใหม่อีกครัง    
    count += 1                                   #ใช้ในการนับ เพิ่อเติมในบรรทัด 21 แสดงลําดับของชุดตัวอักษร
