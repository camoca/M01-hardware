#coding: utf8
numero = 1
final = input ('Introduzca un numero: ')
sortir = False 
while sortir == False:
	if (numero %2 == 0):
		print numero
	if (numero == final):
		sortir = True
	numero = numero + 1
