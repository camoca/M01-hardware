#coding: utf8
###################################
#     Definimos los jugadores     #
###################################
j1 = raw_input ('J1: piedra, papel o tijera ')
j2 = raw_input ('J2: piedra, papel o tijera ')

###################################
#       Creamos las jugadas       #
###################################

if (j1 == "piedra") and (j2 == "piedra"):
	print "Hay un EMPATE"
		
if (j1 == "piedra") and (j2 == "papel"):
	print "Gana J2"
		
if (j1 == "piedra") and (j2 == "tijera"):
	print "Gana J1"
		
if (j1 == "papel") and (j2 == "piedra"):
	print "Gana J1"
		
if (j1 == "papel") and (j2 == "papel"):
	print "Hay un EMPATE"
		
if (j1 == "papel") and (j2 == "tijera"):
	print "Gana J2"
		
if (j1 == "tijera") and (j2 == "piedra"):
	print "Gana J2"
		
if (j1 == "tijera") and (j2 == "papel"):
	print "Gana J1"

if (j1 == "tijera") and (j2 == "tijera"):
	print "Hay un EMPATE"
		
	
	
