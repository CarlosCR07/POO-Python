#CLASES Y OBJETOS 1

class Persona:#CLASE
	#OBJETOS
	doctor='carlos'

#print(Persona.doctor)


#Segundo ejercicio
class jugadores_A:
	j1='messi'
	j2='cr7'

#print(jugadores_A.j2)

class jugadores_B:
	j3='kawamo'
	j1='nose'

print(jugadores_B.j1)


#Tercer ejercicio
class nombre:
	pass #INDICO QUE SALGO DE LA CLASE 

#CREO EL OBJETO "=" ASIGNO A DONDE PERTENECE A CLASE
carlos = nombre() #LOS´PARENTESIS INDICA QUE LA CLASE NOMBRE ESTÁ VACÍA
juana = nombre()

#CREAR ATRIBUTOS
#objeto.atributo
carlos.edad = 20
carlos.genero = 'masculino'
carlos.pais = 'Mexico'

juana.edad = 21
juana.genero = 'femenino'
juana.pais = 'UA'

print(carlos.edad)

print(juana.pais)