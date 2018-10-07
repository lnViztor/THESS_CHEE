#!/usr/bin/pyth
import dns.resolver
import whois
import time
import os
#NOTAS: Este script hara los siguiente:
#1 Usara el SO para hacer un nslookup de los objetivos
#2 Con dns.resolver buscara en esos objetivos los registros MX
#3 Para cada registro MX ira haciendo whois de los mismos.

#Creamos la funcion encargada de resolver los registros MX y ir haciendo whois de los obejtivos.
def myWhois(objetivo,numero):
	print 'WHOIS ENTRADAS MX OJETIVO %s' % numero + ' *' * 57
	try:	
		answers = dns.resolver.query(objetivo,'MX')
		#print 'WHOIS ENTRADAS MX OJETIVO 1' + ' *' * 57
		for rdata in answers:
			#Convierto en cada el nombre
			mx_record = str(rdata.exchange)		
			print 'Servidor', rdata.exchange
			#Le quito el ultimo caracter "." ya que sino falla el whois
			w = whois.whois(mx_record[0:-1])
			print  w
			#hay que meter una pausa de 5 segundos para que no rechace la conexion(google.com)
			time.sleep(5)
			print ' *' * 70
	except dns.resolver.NXDOMAIN:
		print "No existe el dominio%s" % address
	except (dns.resolver.NoAnswer):
		print "Sin servidores de correo"	

try:	
	address1 = raw_input("Introduce el Objetivo 1: ")
	address2 = raw_input("Introduce el Objetivo 2: ")
	print 'INFORMACION GENERAL DNS: OBJETIVO 1' + ' *' * 53
	print os.system('nslookup ' + address1)
	print 'INFORMACION GENERAL DNS: OBJETIVO 2' + ' *' * 53
	print os.system('nslookup ' + address2)
	#Con ayuda de dns.resolver vamos a localizar la entradas del dns del tipo mail exchage

	#****Objetivo 1
	print myWhois(address1,1)
	#****Objetivo 2
	print myWhois(address2,2)
# Controlo la excepcion de salida por interrupcion con el teclado Ctrl + c 
except KeyboardInterrupt:
	print "\n Saliendo \n"
	sys.exit()