import time
import random

print "Welcome to Russian Roulette!!"
time.sleep(2)
number =  raw_input('Enter a number from 1 to 6 ')
print ('you entered %s !' % number)
q =  raw_input ('ARE you ready  ?! y or n   ' )
if q == 'y':
    x = random.randrange(1,6)
    for i in range(20):
        print "BE READY !!"
    time.sleep(4)
    print ("my number is %x" % x)
    if x != int(number):
        print 'you are lucky'
    else:
        print ' BAAAAAAAAAAAAANGG !!!!!you`re dead! '
