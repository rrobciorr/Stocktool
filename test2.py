import sys

d= dir(sys)
for x in range(0,len(d)-3,3):
    print('{0:30s} {1:30s} {2:30s}  '.format(d[0+x], d[1+x], d[2+x]))



t = [ [3,23553,223],[2343,233,11],[993333,1,3322222]]
for x in t:
    print('{0:9d} {1:9d} {2:9d}'.format(x[0], x[1], x[2]))


COMP = (1, 2, 3) < (1, 2, 4)

print( "COMP = " + str(COMP))


