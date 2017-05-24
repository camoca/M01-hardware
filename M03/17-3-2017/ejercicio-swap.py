#coding: utf8

import os

os.system('clear')

##################################
#     ASIGNAMOS LAS VARIABLES    #
##################################

mano_derecha = "móvil"
mano_izquierda = "bocadillo"

print "El movil esta en la mano Derecha."
print "El bocadillo esta en la mano Izquierda."

mano_extra = mano_derecha
mano_derecha = mano_izquierda
mano_izquierda = mano_extra
