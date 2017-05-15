#coding: utf8

##########################
#  ASIGNAMOS VARIABLES   #
##########################

numero = 1
final = input ("Introduce el numero final: ")
salir = False

######################################
#  GENERAMOS BUCLE CON CONDICIONES   #
######################################

while salir == False:
	
	print numero
	
	if (numero == final):
		
		salir = True 
	numero = numero + 1
