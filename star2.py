from turtle import *
import math
n = float(math.floor(float(raw_input("How many points on the star?"))))
# n = float(raw_input("How many points on the star?"))
h = float(raw_input("height of prong?"))
m = float(raw_input("base width?"))
a = m/2.0

g = (m/2)*(1/tan(2*math.pi/(2*n)))
phi1 = 90-(360/(2*n))

if m ==0:
    y = 360/n
    phi2 = (360-2*phi1-y)/2
else:
    phi2 = (math.atan(2*h/m) * 180)/math.pi
    y = 360- 2*phi1 - 2*phi2

if phi2 ==0:
    p = a
else:
    p = h / sin((phi2/180)*math.pi)
phi3 = 90 - phi2
phi4 = 180 - 2 * phi3
print "n: " + str(n)
print "h: " + str(h)
print "m: " + str(m)
print "a: " + str(a)
print "g: " + str(g)
print "phi1: " + str(phi1)
print "phi2: " + str(phi2)
print "phi3: " + str(phi3)
print "phi4: " + str(phi4)
print "y: " + str(y)
print "p: " + str(p)
speed(0)
# left(beta)
fillcolor("#2cc9bb")
begin_fill()
for i in range(int(n)):
    forward(p)
    right(180-y)
    forward(p)
    left(phi4)
end_fill()



mainloop()
