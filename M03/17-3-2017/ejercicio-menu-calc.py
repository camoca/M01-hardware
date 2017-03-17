#coding: utf8

import os

os.system('clear')

print 'Que desea hacer el amo?'
print 'S.- Salir'
print '1.- Sumar'
print '2.- Restar'
print '3.- Multiplicar'
print '4.- Dividir'

opcion = raw_input("Elije una opcion: ")

	if (opcion >= "1" and opcion <= "4") or opcion == 'S' or opcion == 's':
		print "Esta bien."
	else:
		print " No existe"
