# -*- coding: iso-8859-1 -*-
import Pyro4
import socket

VERSION = "1.0"

class Serviteur(object):
	def __init__(self,nom,ip):
		self.nom = nom
		self.ip = ip
	def servir(self):
		pass
	def getInfo(self):
		global VERSION
		info = {
			"NAME":self.nom,
			"IP":self.ip,
			"VERSION": VERSION,
			"DEBUG":"No support",
			"NB_CLIENT":"No support"
		}
		return info

        
class Main(object):
	def __init__(self):
		self.port = 9988
		self.ip = socket.gethostbyname(socket.gethostname())
		self.serviteur=Serviteur("Xavier",self.ip)

		
		daemon=Pyro4.Daemon(host=self.ip,port=self.port)

		uri=daemon.register(self.serviteur,"foo")
		print(uri) 

		print("Pret!")
		daemon.requestLoop()

if __name__ == '__main__':
	m=Main()
