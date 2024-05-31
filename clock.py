from vpython import *
import numpy as np
clockR=3
clockT=clockR/15

centreDotR=clockR/25
centreDotT=clockT+(clockT*0.35)

bigFaceR=clockR+(clockR/10)
bigfaceT=clockT/1.1

hourTickLength=clockR/6
hourTickWidth=hourTickLength/6
hourTickThickness=clockT

minuteTickLength=hourTickLength/2
minuteTickWidth=hourTickWidth/1.8
minuteTickThickness=clockT

hourHandLength= clockR-(clockR*0.18)
hourHandThickness=clockR/30

minuteHandLength=clockR-(clockR*0.3)
minuteHandThickness=clockR/30

centreDot=cylinder(radius=centreDotR,length=centreDotT,color=vector(0,0.3,0.543),axis=vector(0,0,1),pos=vector(0.03,0.03,0))
hourHand=arrow(length=hourHandLength,shaftwidth=hourHandThickness,color=color.red,axis=vector(1,0,0),pos=vector(0,0,clockT))
minuteHand=arrow(length=minuteHandLength,shaftwidth=minuteHandThickness,axis=vector(0,1,0),color=color.red,pos=vector(0,0,clockT))
bigClockFace=cylinder(radius=bigFaceR,length=bigfaceT,color=vector(0,0.3,0.543),axis=vector(0,0,1))
clockface=cylinder(radius=clockR,length=clockT,color=vector(0.753,0.753,0.753),axis=vector(0,0,1))
for angle in np.linspace(0,2*np.pi,13):
    box(size=vector(hourTickLength,hourTickWidth,hourTickThickness+(hourTickThickness*0.2)),color=color.black,axis=vector(clockR*np.cos(angle),clockR*np.sin(angle),0),pos=vector((clockR-(hourTickLength/1.5))*np.cos(angle),(clockR-(hourTickLength/1.5))*np.sin(angle),clockT))
for angle in np.linspace(0,2*np.pi,61):
    box(size=vector(minuteTickLength,minuteTickWidth,minuteTickThickness+(minuteTickThickness*0.2)),color=color.black,axis=vector(clockR*np.cos(angle),clockR*np.sin(angle),0),pos=vector((clockR-(hourTickLength/1.5))*np.cos(angle),(clockR-(hourTickLength/1.5))*np.sin(angle),clockT),opacity=0.7)

while True:
    for theta in np.linspace(2*np.pi,0,10000):
        rate(50)
        minuteHand.axis=vector(minuteHandLength*np.cos(theta),minuteHandLength*np.sin(theta),0)
        minuteHand.length=minuteHandLength
        hourHand.axis=vector(hourHandLength*np.cos(theta*60),hourHandLength*np.sin(theta*60),0)
        hourHand.length=hourHandLength