from base_de_datos import *

def caminos():
	for x in experiencias:
		print(x)


def caminos_difurcados(opciones):
	i = 1
	for x in opciones:
		print(str(i) + ': ' +x.nombre)
		i += 1

def actividades():
	i = 1
	total = 0
	for x in cliente:
		print(cliente['actividad' + str(i)].nombre)
		total =  total + cliente['actividad' + str(i)].precio
		i += 1
	print('Total: $' + str(total))

def mensaje_interactivo():
	print(mensajes['generales'])
	caminos()		

def camino( entrada_general, numero):
	mensaje_interactivo()

	if entrada_general == 1:
		caminos_difurcados(acuaticask)
		entrada_secundaria = int(input(mensajes['cuantico']))
		if entrada_secundaria == 1:
			cliente['actividad' + str(numero)] = acuaticask[0] 
		elif entrada_secundaria == 2:
			cliente['actividad' + str(numero)] = acuaticask[1] 
		elif entrada_secundaria == 3:
			cliente['actividad' + str(numero)] = acuaticask[2] 
		else:
			cliente['actividad' + str(numero)] = acuaticask[3]

	elif entrada_general == 2:
		caminos_difurcados(culturalesk)
		entrada_secundaria = int(input(mensajes['cuantico']))
		if entrada_secundaria == 1:
			cliente['actividad' + str(numero)] = culturalesk[0]
		elif entrada_secundaria == 2:
			cliente['actividad' + str(numero)] = culturalesk[1]
		elif entrada_secundaria == 3:
			cliente['actividad' + str(numero)] = culturalesk[2]
		else:
			cliente['actividad' + str(numero)] = culturalesk[3]


	elif entrada_general == 3:
		caminos_difurcados(culinariask)
		entrada_secundaria = int(input(mensajes['cuantico']))
		if entrada_secundaria == 1:
			cliente['actividad' + str(numero)] = culinariask[0]
		elif entrada_secundaria == 2:
			cliente['actividad' + str(numero)] = culinariask[1]
		elif entrada_secundaria == 3:
			cliente['actividad' + str(numero)] = culinariask[2]
		else:
			cliente['actividad' + str(numero)] = culinariask[3]


	else:
		caminos_difurcados(extremask)
		entrada_secundaria = int(input(mensajes['cuantico']))
		if entrada_secundaria == 1:
			cliente['actividad' + str(numero)] = extremask[0]
		elif entrada_secundaria == 2:
			cliente['actividad' + str(numero)] = extremask[1]
		elif entrada_secundaria == 3:
			cliente['actividad' + str(numero)] = extremask[2]
		else:
			cliente['actividad' + str(numero)] = extremask[3]


def interaccion( numero):
	mensaje_interactivo()
	entrada_general = int(input(mensajes['cuantico']))
	camino(entrada_general, numero)


