#coding: utf8

##########################
#  ASIGNAMOS VARIABLES   #
##########################

num = 1
contador = 1
sortir = False

#########################################
#  GENERAMOS EL BUCLE CON CONDICIONES   #
#########################################

while (sortir == False):
	
	print num
	
	if (num %num==2):
	
		sortir = True
	
	contador = contador / num
	num = num + 1
print contador    
