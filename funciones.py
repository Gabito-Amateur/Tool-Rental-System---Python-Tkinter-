#Librerias
from datetime import datetime

#Clase principal y funciones
class HerramientaAlquiler:
	#Inicializar objeto
	def __init__(data, id_herramienta, hora_salida, tarifa_hora):
		data._id_herramienta = id_herramienta
		data._hora_salida = hora_salida
		data._hora_retorno = None
		data._tarifa_hora = tarifa_hora

	#Funcion que registra la hora de salida (La hora que se alquila)
	def registrar_salida(data, horaS):
		data._hora_salida = horaS

	#Funcion que registra la hora de retorno (La hora que se retorna la herramienta)
	def registrar_retorno(data, horaR):
		data._hora_retorno = horaR

	#Funcion para calcular el costo total a partir de la tarifa, y las horas de salida y retorno
	#En caso de que se introduzca un valor incorrecto en la hora de retorno (Sea letras o menor a la hora de salida)
	#el programa devuelve None y continua
	def calcular_costo(data, horaR):
		try:
			hora_s = datetime.strptime(data._hora_salida, "%H:%M")
			hora_r = datetime.strptime(horaR, "%H:%M")
        
			if hora_r <= hora_s:
				return None

			diferencia = hora_r - hora_s
			horas = diferencia.total_seconds() / 3600
			costo = horas * data._tarifa_hora
			return costo

		except ValueError:
			return None

	#Funcion para obtener el id de la herramienta
	def obtener_id(data):
		return data._id_herramienta




