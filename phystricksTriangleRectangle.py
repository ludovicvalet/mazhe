from phystricks import *
def TriangleRectangle():
    pspict,fig = SinglePicture("TriangleRectangle")

    B=Point(0,0)
    C=Point(1,0)
    A=Point(0.5,0.5*sqrt(3))

    A.put_mark(0.3,90,"$A$")
    B.put_mark(0.3,180,"$B$")
    C.put_mark(0.3,0,"$C$")

    AB=Segment(A,B)
    AC=Segment(A,C)
    BC=Segment(C,B)

    H=BC.center()
    hauteur=Segment(A,H)
    hauteur.parameters.style="dotted"
    hauteur.parameters.color="blue"
    H.put_mark(0.3,-90,"$H$")

    angleS=Angle(A,C,H)
    angleT=Angle(H,A,C)
    angleS.parameters.color="red"
    angleT.parameters.color="cyan"
    angleS.put_mark(0.3,angleS.advised_mark_angle,"$60$")
    angleT.put_mark(0.3,angleT.advised_mark_angle,"$30$")

    pspict.DrawGraphs(AB,AC,BC,hauteur,angleS,angleT,A,B,C,H)
    pspict.dilatation(4)
    fig.conclude()
    fig.write_the_file()