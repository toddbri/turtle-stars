from turtle import *
import math
n = float(math.floor(float(raw_input("How many points on the star?"))))
r2 = float(raw_input("outer diameter?"))/2
r1 = float(raw_input("inner diameter?"))/2
phi2 = float(raw_input("angluar spacing?"))

phi1 = 360/n
phi3 = (phi1-phi2)/2
phi4 = 90-phi3
b = r1*cos(math.radians(phi3))
a = b-r2
e = r1*sin(math.radians(phi3))
c = math.sqrt(a**2 + e**2)
phi5 = acos(a/c)
phi6= 90-phi5
phi7=90-phi3

h = heading()

print "n: " + str(n)
print "r2: " + str(r2)
print "r1: " + str(r1)
print "phi2: " + str(phi2)
print "b: " + str(b)
print "a: " + str(a)
print "e: " + str(e)
print "c: " + str(c)
print "phi1: " + str(phi1)
print "phi2: " + str(phi2)
print "phi3: " + str(phi3)
print "phi4: " + str(phi4)
print "phi5: " + str(phi5)
print "phi6: " + str(phi6)
print "phi7: " + str(phi7)

speed(10)
setheading(0)
fillcolor("#2cc9bb")
begin_fill()
left(90)
pu()
forward(r2)
right(180)
pd()
right(phi5)
for i in range(int(n)):
    forward(c)
    right(phi7)
    circle(r1,phi2)
    forward(c)
    left(180-phi7)
end_fill()

hideturtle()
setheading(c)
mainloop()
