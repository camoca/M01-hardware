#coding: utf8
import os
os.system('clear')Ç

###################################
#  PEDIMOS QUE INDIQUE UN NUMERO  #
###################################

valor1 = input("Escriba un numero: ")
valor2 = input("Escriba otro numero: ")

###################################
#  PONEMOS CONDICION Y PRINTAMOS  #
###################################

if valor1 > valor2:
	print "Este numero" , valor1 , "es mas grande que " , valor2
else:
	if valor1 == valor2:
		print "Estos numeros son iguales"
	else:
		print "El numero" , valor2 , "es mas grande que " , valor1
