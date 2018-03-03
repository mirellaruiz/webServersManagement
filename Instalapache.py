#!/usr/bin/python

import subprocess
import sys

subprocess.call("sudo apt-get install apache2; sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/dominio1.conf", shell = true)

f1 = open("/etc/apache2/sites-available/dominio1.conf", "r")

f2 = open("/tmp/fileprueba1.conf","w")

for line in f1
	if "DocumentRoot /var/www/html" in line:
		f2.write( line + "\n" + "ServerName dominio1.cdps" + "\n" + "ServerAlias www.dominio.cdps")
else:
		f2.write(line)

subprocess.call("mv /etc/apache2/sites-available/dominio1.conf /etc/apache2/sites-available/dominio1.conf.old", shell = True)
subprocess.call("mv /tmp/fileprueba1.conf /etc/apache2/sites-available/dominio1.conf", shell = True)
subprocess.call("sudo a2ensite dominio1.conf; service apache2 reload", shell=True)
