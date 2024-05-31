from vpython import *
def distance(x1,y1,z1,x2,y2,z2):
    dist = ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**(1/2)
    return dist
wallthickness = 0.1
wallHeight=10
wallWidth=10
marbleRadius=marble1Radius=marble2Radius=marble3Radius=0.5
wallDepth=6
floor = box(pos=vector(0,-wallHeight/2,0),size=vector(wallWidth,wallthickness,wallDepth))
ceiling = box(pos=vector(0,wallHeight/2,0),size=vector(wallWidth,wallthickness,wallDepth))
rightSideWall = box(pos=vector(wallWidth/2,0,0),size=vector(wallthickness,wallHeight,wallDepth))
leftSideWall = box(pos=vector(-wallWidth/2,0,0),size=vector(wallthickness,wallHeight,wallDepth))
backSideWall = box(pos=vector(0,0,-wallDepth/2),size=vector(wallWidth,wallHeight,wallthickness))
marble1 = sphere(color=color.red,pos=vector(0,0,0),radius=marbleRadius)
marble2 = sphere(color=color.red,pos=vector(2,0,0),radius=marbleRadius)
marble3 = sphere(color=color.red,pos=vector(-2,0,0),radius=marbleRadius)
deltax1=.1
deltay1=.1
deltaz1=.1
deltax2=.1
deltay2=.1
deltaz2=.1
deltax3=.1
deltay3=.1
deltaz3=.1

xpos1 = 0
ypos1 = -2
zpos1 = -2
xpos2 = 2
ypos2 = 2
zpos2 = 1
xpos3 = -2
ypos3 = 1
zpos3 = 0
while True:
    rate(35)
    xpos1=xpos1+deltax1
    ypos1=ypos1+deltay1
    zpos1=zpos1+deltaz1
    xpos2=xpos2+deltax2
    ypos2=ypos2+deltay2
    zpos2=zpos2+deltaz2
    xpos3=xpos3+deltax3
    ypos3=ypos3+deltay3
    zpos3=zpos3+deltaz3

    #roomedges
    rightXtreme = (wallWidth/2)-marbleRadius
    leftXtreme = (-wallWidth/2)+marbleRadius
    upperextreme = (wallHeight/2)-marbleRadius
    lowerextreme = (-wallHeight/2)+marbleRadius
    frontextreme = (wallDepth/2)-marbleRadius
    backextreme = (-wallDepth/2)+marbleRadius

    if (xpos1>rightXtreme or xpos1<leftXtreme ):
        deltax1=deltax1*-1
    if(ypos1>upperextreme or ypos1<lowerextreme):
        deltay1=deltay1*-1
    if(zpos1>frontextreme or zpos1<backextreme):
        deltaz1=deltaz1*-1
    if (xpos2>rightXtreme or xpos2<leftXtreme ):
        deltax2=deltax2*-1
    if(ypos2>upperextreme or ypos2<lowerextreme):
        deltay2=deltay2*-1
    if(zpos2>frontextreme or zpos2<backextreme):
        deltaz2=deltaz2*-1
    if (xpos3>rightXtreme or xpos3<leftXtreme ):
        deltax3=deltax3*-1
    if(ypos3>upperextreme or ypos3<lowerextreme):
        deltay3=deltay3*-1
    if(zpos3>frontextreme or zpos3<backextreme):
        deltaz3=deltaz3*-1
    if(abs(distance(xpos1,ypos1,zpos1,xpos2,ypos2,zpos2))<marble1Radius+marble2Radius):
        deltax1 = deltax1*-1
        deltay1 = deltay1*-1
        deltaz1 = deltaz1*-1
        deltax2 = deltax2*-1
        deltay2 = deltay2*-1
        deltaz2 = deltaz2*-1
    if(abs(distance(xpos3,ypos3,zpos3,xpos2,ypos2,zpos2))<marble3Radius+marble2Radius):
        deltax3 = deltax3*-1
        deltay3 = deltay3*-1
        deltaz3 = deltaz3*-1
        deltax2 = deltax2*-1
        deltay2 = deltay2*-1
        deltaz2 = deltaz2*-1
    if(abs(distance(xpos3,ypos3,zpos3,xpos1,ypos1,zpos1))<marble3Radius+marble1Radius):
        deltax3 = deltax3*-1
        deltay3 = deltay3*-1
        deltaz3 = deltaz3*-1
        deltax1 = deltax1*-1
        deltay1 = deltay1*-1
        deltaz1 = deltaz1*-1
    marble1.pos=vector(xpos1,ypos1,zpos1)
    marble2.pos=vector(xpos2,ypos2,zpos2)
    marble3.pos=vector(xpos3,ypos3,zpos3)