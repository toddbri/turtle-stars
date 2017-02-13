from turtle import *
import math
n = float(math.floor(float(raw_input("How many points on the star?"))))
r2 = float(raw_input("outer diameter?"))/2
r1 = float(raw_input("inner diameter?"))/2
phi1 = 360/n
phi2 = phi1/2.0
h = r1 * cos(math.radians(phi2))
b = r1 * sin(math.radians(phi2))
l = r2-h
p = math.sqrt(b**2 + l**2)
phi3 = math.degrees(math.asin(b/p))
phi4 = 90-phi2
phi5 = 90-phi3
phi6 = 360-2*phi4 - 2 *phi5
phi7 = 180 - 2 * phi3
c = heading()

print "n: " + str(n)
print "r2: " + str(r2)
print "r1: " + str(r1)
print "h: " + str(h)
print "b: " + str(b)
print "phi1: " + str(phi1)
print "phi2: " + str(phi2)
print "phi3: " + str(phi3)
print "phi4: " + str(phi4)
print "phi5: " + str(phi5)
print "phi6: " + str(phi6)
print "p: " + str(p)
speed(10)
setheading(0)
fillcolor("#2cc9bb")
begin_fill()
left(90)
pu()
forward(r2)
right(180)
pd()
right(phi3)
for i in range(int(n)):
    forward(p)
    right(180-phi6)
    forward(p)
    left(phi7)
end_fill()

hideturtle()
setheading(c)
mainloop()
