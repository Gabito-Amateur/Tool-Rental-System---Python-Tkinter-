#Clase usuario
class Usuario:
	#Inicializar los datos de login para su comparacion
	def __init__(data):
		data._usuario = "programacion"
		data._password = "programacion"

	#FUncion que valida los datos del login necesarios con los datos ingresados por el cliente
	#si son iguales, retorna un True, de lo contrario, un False (Utilizado luego para la validacion visual del login)
	def validar(data, usuario_ingresado, password_ingresado):
		if(usuario_ingresado == data._usuario and password_ingresado == data._password):
			return True
		else:
			return False

