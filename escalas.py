from PIL import Image,ImageDraw
import numpy as np
import graflib as gl
import math

def escala(p,fs):
    P=np.array([p[0],p[1]])
    #Matriz de escala
    Scale=np.array([[fs,0],[0,fs]])
    return np.matmul(Scale,P.transpose())
    
def rotateP(p,alpha):
    P=np.array([p[0],p[1]])
    #Matriz de rotacion
    matrixR=np.array([[np.cos(alpha),-np.sin(alpha)],
                      [np.sin(alpha),np.cos(alpha)]])
    return np.matmul(matrixR,P.transpose())
    

def reflexionPx(p,alpha):
     P=np.array([p[0],p[1]])
     #Matriz de rotacion
     reflex=np.array([[-1,0],
                      [0,1]])
     return np.matmul(reflex,P.transpose())
 

#Tamaño de la imagen
width = 800
height =  800

#Definir un lienzo
canvas = Image.new('RGB', (width,height), (255,255,255))

#Puntos iniciales
puntos = [(0,0),(100,0),(100,100),(0,100)]
color1 = (145,128,0)
color2 = (0,128,188)

print(puntos)

fs=2
alpha=-math.pi/4
puntosS=[]
for punto in puntos:
    xS,yS = escala(punto,fs)
    xS,yS = rotateP(punto,alpha)
    puntosS.append((int(xS),int(yS)))
print(puntosS)

i = 0
k = len(puntos)
while i < k-2:
    gl.drawWireframeTriangle(puntos[0],puntos[i+1],puntos[i+2],color1,canvas)
    gl.drawWireframeTriangle(puntosS[0],puntosS[i+1],puntosS[i+2],color2,canvas)
    i = i+1

canvas.show()