#!/usr/bin/python

import os

os.system('clear')

salir = False
while salir == False :
	

		print 'Que desea hacer amo?'
		print 'S) Salir'
		print '1) Sumar'
		print '2) Restar'
		print '3) Multiplicar'
		print '4) Dividir'

		opcion = raw_input('Elija una opcion ==> ')
		if opcion >= '1' and opcion <= '4':
			print 'Sigue... '
			tecla = raw_input("Presiona una tecla para continuar: ")
			
		if opcion == 'S' or opcion == 's':
			print 'Adios.'
			salir = True
		else :
			print "Esa opcion no existe"
			tecla = raw_input("Presiona una tecla para continuar: ")
