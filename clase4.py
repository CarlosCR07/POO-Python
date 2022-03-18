#FUNCIONES PARA ATRIBUTOS

class Persona:
	edad = 20
	nombre = 'carlos'
	pais= 'mexico'

doctor =  Persona()

#Para eliminar el atributo de la clase
delattr(Persona, 'pais')
#print(doctor.pais)


#Imprimir de ptra forma el atributo
print("la edad es:", doctor.edad)
print("la edad es:", getattr(doctor, 'edad'))

#Para verificar si existe el atribbuto dentro de los atributpos de clase
print("¿el doctor tiene una edad?", hasattr(doctor, 'edad'))
print("¿el doctor tiene un apellido?", hasattr(doctor, 'apellido'))

#Para actualizar o cambiar el valor del atributo.
print(doctor.nombre)
setattr(doctor, 'nombre', 'hector')
print(doctor.nombre)
