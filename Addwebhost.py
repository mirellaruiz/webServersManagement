#!/usr/bin/python
import subprocess
import sys
import optparse

name = sys.argv[1]

if name is None:
	print("Introduce un dominio")
else:
	subprocess.call("sudo mkdir /var/www/" + name, shell=True)

	f1 = open("/var/www/"+ name +"/index.html", "w")

	f1.write("//Fichero index.html en "+ name)
	f1.write("<html>")
	f1.write("<h1> Servidor" + name + "</h1>")
	f1.write("</html>")

	f1 = open("/etc/apache2/sites-available/dominio1.conf", "r")
	f2 = open("/tmp/fileprueba1.conf", "w")

	for line in f1
		if "DocumentRoot /var/www/html" in line:
			f2.write(line + "\n" + "ServerName "+ name + ".cdps" + "\n" + "ServerAlias www. "+ name + ".cdps", shell=True)
		else:
		f2.write(line)

subprocess.call("mv /tmp/fileprueba1.conf /etc/apache2/sites-available/" + name + ".conf", shell = True)
subprocess.call("sudo a2ensite "+ name + ".conf; service apache reload", shell= True)
