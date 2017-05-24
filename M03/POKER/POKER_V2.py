#coding: utf8

##################################
#  GENERAMOS UNA JUGADA ALEATORIA#
##################################

from random import randint
salir =False
while (salir== False):
	palo= randint (1,4)

#####################
#  ASIGNAMOS PALOS  #
#####################
	
	if (palo == 1):
		palos = "PICAS"

	if (palo == 2):
		palos = "ROMBOS"
		
	if (palo == 3):
		palos = "TREBOL"
		
	if (palo == 4):
		palos = "CORAZONES"
		
	palo= randint (1,4)

	if (palo == 1):
		paloss = "PICAS"

	if (palo == 2):
		paloss = "ROMBOS"
		
	if (palo == 3):
		paloss = "TREBOL"
		
	if (palo == 4):
		paloss = "CORAZONES"
		

	J1= randint (2,14)
	J2= randint (2,14)
	
#######################
#  ASIGNAMOS NUMEROS  #
#######################	
	
	if (J1 == J2):
		print "Hay un empate"

	if (J1 == 11):
		J1 = "J"
		
	if (J1 == 12):
		J1 = "Q"
		
	if (J1 == 13):
		J1 = "K"
		
	if (J1 == 14):
		J1 = "A"
		
	if (J2 == 11):
		J2 = "J"
		
	if (J2 == 12):
		J2 = "Q"
		
	if (J2 == 13):
		J2 = "K"
		
	if (J2 == 14):
		J2 = "A"
		
#######################
#  JUGADA DE J1 Y J2  #
#######################
		
	print "J1 tiene", J1, "de", palos
	print "J2 tiene", J2, "de", paloss

		
	if (J1 > J2):
		print "GANA J1"
	else:
		print "GANA J2"
	
	if (J1 <> J2):
		salir = True
