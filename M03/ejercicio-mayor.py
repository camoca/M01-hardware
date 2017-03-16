#coding: utf8
import os
os.system('clear')

valor1 = input("Escriba un numero: ")
valor2 = input("Escriba otro numero: ")

if valor1 > valor2:
	print "Este numero" , valor1 , "es mas grande que el numero" , valor2
else:
	if valor1 == valor2:
		print "Estos numeros son iguales"
	else:
		print "El numero" , valor2 , "es mas grande que " , valor1
