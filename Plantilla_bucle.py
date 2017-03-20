#!/usr/bin/python

import os


salir = False
while salir == False :
	os.system('clear')
	print ("Hola!")
	tecla = raw_input("Pulsa una tecla: ")
	if (tecla == "S" or tecla == "s"):
		print ("Adios!")
		salir = True
