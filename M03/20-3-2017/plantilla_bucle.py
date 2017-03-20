#coding: utf8

salir = False

while salir == False:
	print 'Hola'
	 
	tecla = raw_input ('presione una tecla: ')
	
	if (tecla == 's' or tecla == 'S'):
		print 'Adios muy buenas'
		salir = True
