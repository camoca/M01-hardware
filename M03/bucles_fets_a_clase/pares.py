#coding: utf8

##########################
#  ASIGNAMOS VARIABLES   #
##########################

numero = 1
final = input ('Introduzca un numero: ')
sortir = False 

######################################
#  GENERAMOS BUCLE CON CONDICIONES   #
######################################

while sortir == False:
	if (numero %2 == 0):
		print numero
	if (numero == final):
		sortir = True
	numero = numero + 1
