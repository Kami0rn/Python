n = 0
email2 = [ ]
while ( n > 5 or n < 1 ) :
    n =int ( input ( " How many email ? ( 1-5 ) : " ) )
    if ( n >5 or n < 1 ) :
        print ( " Invalid number , try again " )
for i in range ( 1 , n + 1 ) :
    email = input ( " email % d : " % i )
    email2.append ( email )
for j in email2 :
    c = j.index ( '@' )
    print ( j [c+1:] )