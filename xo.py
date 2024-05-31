from vpython import *
import numpy as np
selectBoxCount = 0
def outerGrid():
    upperBoxWidth=6
    upperBoxLength=0.1
    upperBoxDepth=2

    lowerBoxWidth=6
    lowerBoxLength=0.1
    lowerBoxDepth=2

    rightBoxWidth=0.1
    rightBoxLength=6
    rightBoxDepth=2

    leftBoxWidth=0.1
    leftBoxLength=6
    leftBoxDepth=2

    upperGrid=box(size=vector(upperBoxWidth,upperBoxLength,upperBoxDepth),pos=vector(0,1,0))
    lowerGrid=box(size=vector(lowerBoxWidth,lowerBoxLength,lowerBoxDepth),pos=vector(0,-1,0))
    rightGrid=box(size=vector(rightBoxWidth,rightBoxLength,rightBoxDepth),pos=vector(1,0,0))
    leftGrid=box(size=vector(leftBoxWidth,leftBoxLength,leftBoxDepth),pos=vector(-1,0,0))

def selectionBox(x,y,z):
    boxWidth=boxLength=boxDepth=2
    selectionBox=box(size=vector(boxWidth,boxLength,boxDepth),color=vector(0,0.2,0.5),pos=vector(x,y,z),opacity=0.3)
    
def xcreation(x,y,z):
    box(size=vector(2,0.3,1.2),color=color.red,axis=vector(2*(np.cos(95)),2*(np.sin(95)),0),pos=vector(x,y,z))
    box(size=vector(2,0.3,1.2),color=color.red,axis=vector(2*np.cos(172),2*np.sin(172),0),pos=vector(x,y,z))

def ocreation(x,y,z):
    sphere(radius=0.8,color=color.red,pos=vector(2,0,0))

boxWidth=boxLength=boxDepth=2

outerGrid()
selectionBox=box(size=vector(boxWidth,boxLength,boxDepth),color=vector(0,0.2,0.5),opacity=0.3)

while True:
    pass