from vpython import *
disco = sphere(radius=2,color=color.yellow)
redColour=1
greenColour=1
blueColour=0.001
redInc=0.001
greenInc=-0.001
blueInc=0.001
while True:
    rate(500)
    redColour = redColour + redInc
    greenColour = greenColour + greenInc
    blueColour = blueColour + blueInc
    if redColour<=1:
        rapply=redColour
    if greenColour<=1:
        gapply=greenColour
    if blueColour<=1:
        bapply=blueColour
    if (redColour>1):
        rapply=1
    if (greenColour>1):
        gapply=1
    if (blueColour>1):
        bapply=1
    disco.color=vector(rapply,gapply,bapply)
    if(redColour>=1.5 or redColour<0.001):
        redInc=redInc*(-1)
    if(greenColour>=1.5 or greenColour<0.001):
        greenInc=greenInc*(-1)
    if(blueColour>=1.5 or blueColour<0.001):
        blueInc=blueInc*(-1)
    print(rapply+gapply+bapply)
