#! /usr/bin/python
# coding: utf8

numero= raw_input("Introduzca un número: ")

if (numero % 2 == 0):
	print "este numero es par"

if (numero >= -10 and numero <= 40):
	print "Este numero esta entre el -10 y el 40"
	
if (numero % -2 == 0 and numero % -1 == 0):
	print "este numero és negativo"
