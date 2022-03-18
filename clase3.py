#METODOS

#Ejercicio 1
class Mates:
	def suma(self):
		self.n1 = 2
		self.n2 = 3

s = Mates()
s.suma()
print(s.n1 + s.n2)

#Ejercicio 2

class Ropa:
	def __init__(self):
		self.marca = 'nike'
		self.talla = 'M'
		self.color = 'rojo'

camisa = Ropa()
print(camisa.talla)
print(camisa.marca) 
print(camisa.color)

#Ejercicio 3
#print("Inserte los valores de la operacion que desea hacer")
#n1=int(input())
#n2=iny(input())

class Calculadora:
	def __init__(self, n1, n2): #Defino variables de mi método
		self.suma = n1+n2
		self.resta= n1-n2
		self.mult= n1*n2
		self.div= n1/n2

operaracion = Calculadora(5, 2)#Asigno valor a variables ya que nbo puede estar vacio.
print(operaracion.mult)