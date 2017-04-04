# coding:utf-8

from random import randint

J1=raw_input ("Elije PI/PA/TI/LA/SP: ")


aleatorio=randint(1,5)

if (aleatorio==1):
	J2="PI"
	
if (aleatorio==2):
	J2="PA"
	
if (aleatorio==3):
	J2="TI"
	
if (aleatorio==4):
	J2="LA"
	
if (aleatorio==5):
	J2="SP"

print "La meva jugada és:" , J2

if (J1==J2):
	print "DRAW"
else:
	
	if ( (J1=="PI" and ( J2=="LA" or J2=="TI") ) or
	     (J1=="PA" and ( J2=="PI" or J2=="SP") ) or
	     (J1=="TI" and ( J2=="PA" or J2=="LA") ) or
	     (J1=="LA" and ( J2=="PA" or J2=="SP") ) or
	     (J1=="SP" and ( J2=="PI" or J2=="TI") )
	   ):
		print "YOU WIN"
		
	else: 
		print "YOU ARE A LOSER!!!!"
