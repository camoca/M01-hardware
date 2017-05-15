#coding: utf8

salir = False

##################################
#  EMPEZAMOS EL BUCLE CON WHILE  #
##################################

while salir == False:
	print 'Hola'
	
###############################################
#  PEDIMOS QUE PRESIONE UNA TECLA PARA SALIR  #
###############################################
	 
	tecla = raw_input ('presione una tecla: ')
	
	if (tecla == 's' or tecla == 'S'):
		print 'Adios muy buenas'
		salir = True
