#List numbers from 0 to 10, divide each by 3,
# print result as 2 decimal places

#round()
#format()
divisor=3
decimal_places=2
for i in range(0,11):
    print("This is my rounded decimal{0:.2f}".format(i/divisor))