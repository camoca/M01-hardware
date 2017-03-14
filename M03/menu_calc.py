 
print 'Que operacion desea hacer?'
print '1) Sumar'
print '2) Restar'
print '3) Multiplicar'
print '4) Dividir'
 
 
opcion = raw_input('Elija una opcion ---> ')
numero = int(raw_input('Introduce un numero ---> '))
numero2 = int(raw_input('Introduce otro numero ---> '))

if opcion == '1':
    suma = numero + numero2
    print 'Calculando...'
    print 'El resultado es ', suma
 
if opcion == '2':
    resta = numero - numero2
    print 'Calculando...'
    print 'El resultado es ', resta
 
if opcion == '3':
    multi = numero * numero2
    print 'Calculando...'
    print 'El resultado es ', multi
 
if opcion == '4':
    divi = numero / numero2
    print 'Calculando...'
    print 'El resultado es ', divi
