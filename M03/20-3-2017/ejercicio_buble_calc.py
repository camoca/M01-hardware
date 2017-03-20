#coding: utf8

import os

salir = False

while salir == False:
	
	os.system('clear')
	print 'Que desea hacer el amo ? '
	print 'S.- Salir '
	print '1.- Sumar '
	print '2.- Restar '
	print '3.- Multiplicar '
	print '4.- Dividir '
	
	opcion = raw_input('Elija la opcion que desea: ')
	
	if (opcion >= '1' and opcion <= '4'):
		print 'Esta bien'
		tecla = raw_input('Presione cualquier tecla para continuar: ')
		
	if (opcion == 's' or opcion == 'S'):
		print 'Adiós amo'
		salir = True
	else:
		print 'Esta opicion no existe'
		tecla = raw_input('Presione una tecla para continuar: ')
