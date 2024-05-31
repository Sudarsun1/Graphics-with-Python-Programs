from vpython import *
import numpy as np
rateConst=100            
outerBulb1 = sphere(radius=1.5,opacity=0.3,pos=vector(0,3,0))
inerBulb1 = sphere(radius=1.2,color=color.red,pos=vector(0,3,0))
outerMercury1=cylinder(radius=0.85,opacity=0.3,length=12,pos=vector(0,3,0))
innerMercury1=cylinder(radius=0.6,color=color.red,length=11.85,pos=vector(0,3,0))
outerBulb2 = sphere(radius=1.5,opacity=0.3,pos=vector(0,-3,0))
inerBulb2 = sphere(radius=1.2,color=color.red,pos=vector(0,-3,0))
outerMercury2=cylinder(radius=0.85,opacity=0.3,length=12,pos=vector(0,-3,0))
innerMercury2=cylinder(radius=0.6,color=color.red,length=11.85,pos=vector(0,-3,0))
while True:
    for length1 in np.linspace(1,11.85,500):
        rate(rateConst)
        if(length1*2<11.85):
            innerMercury1.length=length1*2
        else:
            innerMercury1.length=(11.85-length1)*2
        innerMercury2.length=length1
    for length1reverse in np.linspace(11.85,1,500):
        rate(rateConst)
        if((11.85-length1reverse)*2 < 11.85):
            innerMercury1.length=(11.85-length1reverse)*2
        else:
            innerMercury1.length=length1reverse*2
        innerMercury2.length=length1reverse
    
