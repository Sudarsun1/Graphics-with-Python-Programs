from vpython import *

cylinder1 = cylinder(radius=1,color=color.red,length=1,pos=vector(0,3,0))
cylinder2 = cylinder(radius=1,color=color.blue,length=1,pos=vector(0,-3,0))
length1=1
length2=1
delta1=0.02
delta2=0.04
while True:
    rate(150)
    length1=length1+delta1
    length2=length2+delta2
    if(length1>10 or length1<1):
        delta1=delta1*-1
    if(length2>10 or length2<1):
        delta2=delta2*-1
    cylinder1.length=length1
    cylinder2.length=length2