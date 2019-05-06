from Puntos import *
from Rectangulo import *
from Circulo import *
from Triangulo import *
from Cuadrado import *

p1=Punto()
p2=Punto()
p1.x = input ("Ingrese coordenada x del punto 1")
p1.x = input ("Ingrese coordenada y del punto 1")
p2.y = input ("Ingrese coordenada x del punto 2")
p2.y = input ("Ingrese coordenada y del punto 2")

r = Rectangulo()
r.setPuntos(p1,p2)
r.arearec()
r.perimetrorec()

t = Triangulo()
t.setPuntos(p1,p2)
t.areatri()
t.perimetri()

c = Circulo()
c.setPuntos(p1,p2)
c.areacir()
c.perimetrocir()

s = Cuadrado()
s.setPuntos(p1,p2)
s.areacua()
s.perimetrocua()

print "el area del rectangulo es {resultado1} y el perimetro es {resultado2}".format(resultado1=r.area, resultado2=r.perimetro)
print "el area del triangulo es {resultado1} y el perimetro es {resultado2}".format(resultado1=t.area, resultado2=t.perimetro)
print "el area del circulo es {resultado1} y el perimetro de la circunferencia es {resultado2}".format(resultado1=c.area, resultado2=c.perimetro)
print "el area del cuadrado es {resultado1} y el perimetro es {resultado2}".format(resultado1=s.area, resultado2=s.perimetro)


