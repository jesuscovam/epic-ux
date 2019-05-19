#--- Información de las actividades.
class Acuaticas:
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio  = precio

class Culturales:
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio  = precio

class Culinarias:
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio  = precio

class Extremas:
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio  = precio

cliente = {	'actividad1': '',
						'actividad2': '',
						'actividad3': '',
						'actividad4': ''}

total = 0
#Encabezado
experiencias = ['1: Acuaticas', '2: Culturales', '3: Culinarias', '4: Extremas']

#Acuaticas
xelha = Acuaticas('Xel-Ha', 60)
ruta = Acuaticas('Ruta de Cenotes', 30)
cozumel = Acuaticas('Cozumel', 70)
kantun = Acuaticas('Cenote Kantun Chi', 40)
acuaticask = [xelha, ruta, cozumel, kantun]

#Culturales
xcaret = Culturales('Xcaret', 120)
quinta = Culturales('5ta Avenida', 0)
museo = Culturales('Museo de Frida Kahlo', 40)
plaza = Culturales('Plaza en la Playa',0)
culturalesk = [xcaret, quinta, museo, plaza]

#Culinarias
fogon = Culinarias('El Fogón', 20)
mu = Culinarias('Mu BurgerHouse', 30)
orange = Culinarias('Café Orange', 20)
parrilla = Culinarias('La Parrilla', 40)
culinariask = [fogon, mu, orange, parrilla]

#Extremas
xplor = Extremas('X-plor', 110)
tiburon = Extremas('Tiburon Ballena', 70)
rio = Extremas('Río Secreto', 100)
xplor_fuego = Extremas('X-plor Fuego', 110)
extremask = [xplor, tiburon, rio, xplor_fuego]


#Mensajes
mensajes = {'desarrollo': 'Siguiente: ',
							'final': 'Por Último: ',
							'gracias': '¡Gracias!',
							'cuantico': 'Escoja una de las siguientes: ',
							'generales': 'Estas son nuestras experiencias generales: ',
							'especificas': 'Estas son nuestras experiencias especificas',
							'una': '¡Tu aventura esta tomando forma!'
							}


# Por hacer
# Agregar una class Clientes con self.actividad1, self.actividad2 .... selft.actividad4

