# coding: utf8

from random import randint

salir = False
salir2 = False

while (salir == False):

	palo1 = randint(1,4) 
	palo2 = randint(1,4)

	if (palo1 == 1):
		palos = "Picas"
		
	if (palo1 == 2):
		palos = "Corazones"
		
	if (palo1 == 3):
		palos = "Diamantes"
		
	if (palo1 == 4):
		palos = "Tréboles"

	J1 = randint(2,14)
	J2 = randint(2,14)
	
	numero1 = J1
	if (J1 == 11):
		numero1 = "J"
		
	if (J1 == 12):
		numero1 = "Q"
		
	if (J1 == 13):
		numero1 = "K"
		
	if (J1 == 14):
		numero1 = "AS"
		
	print "Tienes un", numero1 , "de", palos


	while (salir2 == False):
		
		if ((J1 == J2) and (palo1 == palo2)):
			J2 = randint(2,14)
			palo2 = randint(1,4)
			
		if not((J1 == J2) and (palo1 == palo2)):
			salir2 = True
	
	if (palo2 == 1):
		paloss = "Picas"
		
	if (palo2 == 2):
		paloss = "Corazones"
		
	if (palo2 == 3):
		paloss = "Diamantes"
		
	if (palo2 == 4):
		paloss = "Tréboles"
				
	numero2 = J2
	if (J2 == 11):
		numero2 = "J"
		
	if (J2 == 12):
		numero2 = "Q"
		
	if (J2 == 13):
		numero2 = "K"
		
	if (J2 == 14):
		numero2 = "AS"
			
	print "Tu rival tiene", numero2 , "de" , paloss

	if (J1 == J2):
		print "Hay un empate"
		
	else:
		if ( J1 > J2):
			print "Has ganado"	
		else:
			print "Has perdido"
	
	if not(J1 == J2):
			salir = True
