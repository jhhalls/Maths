def greatest_common_divisor(x,y):
    print "For", x, "and", y,","  
    r=x%y
    while r>0:
        r=x%y
        if r ==0: 
            print "the greatest common divisor is", y,"."
        else:
            q=y
            x=q
            y=r
