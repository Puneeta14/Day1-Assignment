##   print the following pattern
		        #*
	         #*  *
        #  *  *  *
       #*  *  *  *
    #*  *  *  *  *
space =5
for i in range (0,5):
    for j in range(space):
        print(" ",end=" ")
    space =space-1
    for j in range(i+1):
        print("*",end=" ")
    print()