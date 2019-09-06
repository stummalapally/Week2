#%-modulo

#print the remainder for dividing each integer frm 0 to 10 by 3

# 0%3=0
#1%3=1
#2%3=2
#3%3=0
#4%3=1

#for
#range
#%
divisor = 4
for number in range(0,11):
    print(str(number)+ "%"+str(divisor)+ "=" +str(number%divisor))

