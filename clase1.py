#CLASES Y OBJETOS 1

#clases(contenedor o modelo)
class Auto: #necesario que sea con mayuscula
	marca = ""
	modelo = 317042711
	placa = ""

#objeto
#		Pertenece a la clase auto
taxi = Auto() #objeto taxi pertenece a clase auto

#MANDAMIOS A llamar al objeto y el atributo que queremos del modelo
print(taxi.modelo)