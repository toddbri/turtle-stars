from turtle import *
import math
n = float(math.floor(float(raw_input("How many points on the star?"))))
r2 = float(raw_input("outer diameter?"))/2
r1 = float(raw_input("inner diameter?"))/2
question   = "angular spacing (<%f)?" % (360/n)
phi2 = float(raw_input(question))
# n =5
# r2=300
# r1=100
# phi2=36
phi1 = 360/n
phi3 = (phi1-phi2)/2
phi4 = 90-phi3
b = r1*cos(math.radians(phi3))
a = r2-b
e = r1*sin(math.radians(phi3))
c = math.sqrt(a*a + e*e)
phi5 = math.degrees(acos(a/c))
phi7=90-phi5
phi6= 90-phi5-phi3
phi8 = 180-2*phi5

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
print "phi8: " + str(phi8)

speed(10)
# goto(0,-r1)
# setheading(0)
# circle(r1)
# home()
# setheading(0)
fillcolor("#2cc9bb")
begin_fill()
left(90)
pu()
forward(r2)
right(180)
pd()
# print heading()
right(phi5)
# forward(c)
# right(phi6+7.5)
# pencolor("blue")
# circle(r1,phi2)
for i in range(int(n)):
    forward(c)
    # print heading()
    right(phi6)
    # print heading()
    circle(r1,phi2)
    # print heading()
    right(phi6)
    # print heading()
    forward(c)
    left(phi8)

end_fill()

hideturtle()
setheading(c)
mainloop()
