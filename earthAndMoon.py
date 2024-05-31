from vpython import *
import numpy as np
earthRadius=3
moonRadius=0.5
mred=0.753
mgreen=0.753
mblue=0.753
moonLength=6
earth=sphere(radius=earthRadius,color=color.blue)
moon=sphere(radiu=moonRadius,color=vector(mred,mgreen,mblue),make_trail=True,trail_color=color.white,pos=vector(moonLength,0,0))
while True:
    for angle in np.linspace(0,2*np.pi,5000):
        rate(300)
        moon.pos=vector(moonLength*cos(angle),0,moonLength*sin(angle))
        moon.radius=moonRadius