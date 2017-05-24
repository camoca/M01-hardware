# coding: utf8

#########################
#  ASIGNAMOS VARIABLES  #
#########################

num = 31

Salir = False

#######################################################
#  EMPEZAMOS EL BUCLE CON WHILE Y PONEMOS CONDICIONES #
#######################################################

while (Salir == False):

 if ( num % 7 == 0) or ( num % 7 == 1):
  J1 = "Tijeras"
  
 if ( num % 7 == 2) or ( num % 7 == 3) or ( num % 7 == 6):
  J1 = "Piedra"
  
 if ( num % 7 == 4) or ( num % 7 == 5):
  J1 = "Papel"
  
 if ( num % 5 == 0) or ( num % 5 == 1) or (num % 5 == 2):
  J2 = "Papel" 
  
 if ( num % 5 == 3):
  J2 = "Tijeras" 
  
 if ( num % 5 == 4):
  J2 = "Piedra"
  
 if (J1 == "Piedra" and J2 == "Tijeras"):
	
####################################################################
#  PONEMOS LOS PRINTS DE QUIEN GANA, QUIEN PIERDE Y SI HAY EMPATE  #
####################################################################
	 
  print num, " J1 saca: ",J1, " J2 saca: ",J2, " J1 WIN"
  
 if (J1 == "Papel" and J2 == "Piedra"):
	 
  print num, " J1 saca: ",J1, "J2 saca: " , J2, " J1 WIN"
  
 if (J1 == "Tijeras" and J2 == "Papel"):
	 
  print num, "J1 saca: ",J1, "J2 saca: ",J2, " J1 WIN"
  
 if (J2 == "Piedra" and J1 == "Tijeras"):
	 
  print num, " J1 saca: ",J1, "J2 saca: ",J2, " J2 WIN"
  
 if (J2 == "Papel" and J1 == "Piedra"):
	 
  print num, " J1 saca: ",J1, " J2 saca: ",J2, " J2 WIN"
  
 if (J2 == "Tijeras" and J1 == "Papel"):
	 
  print num, " J1 saca: ",J1, "J2 saca: ",J2, "J2 WIN"

 if ( J1 == J2):
	 
  print num, " EMPATE "

########################################
#  SE CUMPLE CONDICION DE SALIDA, SALE #
########################################
  
 if ( num == 57 ):
	 
  Salir = True
  
 num = num + 1
