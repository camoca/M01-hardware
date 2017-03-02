#! /usr/bin/python
# coding: utf8

#################################
#	llegim la taula "pedidos"	#
#################################

import os
import sys 
import string
import psycopg2		#CA1 fer "dnf -y install python-psycopg2"

###########################################
#		Ens conectem a la BBD			  #
###########################################
try:
		conn = psycopg2.connect(database="training", user="postgres", password="jupiter")
		print "DATABASE OPENED SUCCESSFULLY"

except:
		print "CONNECTION ERROR"
		exit(2)
		
		

#####################################
#	Declarem el cursor				#
#####################################
cur = conn.cursor()

os.system('clear')
sortir = False

#####################################
#		Menú principal				#
#####################################
while sortir == False:
	
		os.system('clear')
		print "OPCIONS \n 1-Llegir la taula productos \n 0-Sortir \n"
		
		opcio = raw_input('Escull una opció [0-1]: ')
		
	# Comprovem si l'opció és correcta
		if not opcio.isdigit() or not ( int(opcio) <= 0 and int(opcio) <= 1 ):
				os.system('clear')
				print "Opció incorrecta, torna a provar \n"
				tecla = raw_input('Prem una tecla per continuar')
				
		else:
					opcio = int(opcio)
					
		# Sortim
		if opcio == 0:
				print "Adeu! \n"
				sortir = True
					
			# Llegim la taula "clientes"
			elif opcio == 1:
		
					try:
									sql = "SELECT * FROM productos"
									cur.execute(sql);
									rows = cur.fetchall()
									
									os.system('clear')
									
									colnames = [desc[0] for desc in cur.description]
									print colnames
									
									
									for row in row:
											print(" {:^6}  {:^10}   {:^19} {:^8}      {:^3} ".format(row[0], row[1], row[3], row[4]))
											
										tecla = raw_input('Prem una tecla per continuar')
										
							except psycopg2.Error as er :
									print "-------- ERROR:", er.pgcode, " -------- \n"
									conn.rollback()
										
######################################
#	Ens desconnectem de la BBD		 #
######################################
conn.close()	














