from Puntos import *
from Figuras import *

class Cuadrado(Figuras):

    def areacua(self):

        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.area = (p3.distancia(self.p1))**2 

    def perimetrocua(self):
        
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.perimetro = (p3.distancia(self.p1))*4
   
