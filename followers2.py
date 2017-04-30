#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
from InstagramAPI import InstagramAPI	
import json
import contextlib
import io
import sys
import threading

# esta funcion hace que no se vea el stdout cuando corro una funcion
@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = io.BytesIO()
    yield
    sys.stdout = save_stdout

def followers(otherusername,fileName="followers",time=60):
	text_file = open(fileName, "a")

	threading.Timer(time, followers, [otherusername,fileName,time]).start() # crea un thread cada "time" tiempo 

	InstagramAPI.searchUsername(otherusername) 
	usuario = InstagramAPI.LastJson # devuelve la respuesta JSON de la funcion anterior

	username = usuario["user"]["username"] 
	usernameId = usuario["user"]["pk"] # al parecer "pk" es la "id"
	name = usuario["user"]["full_name"]
	followerCount = usuario["user"]["follower_count"]
	s = ""
	s += "\n"
	s += "Cantidad de followers de " + str(name) + " (@" + str(username) + ") : " + str(followerCount)
	text_file.write("%s" % s)
	text_file.close()

#MAIN:
#Valores a completar
yourusername = "jcwithc" # COMPLETAR CON username/password de cuenta ig con la loguearas. Ej: jcwithc
yourpassword = "papalo" # Ej: pepe
otherusername = "pero" # COMPLETAR CON usuario al cual se buscara. Ej: jcwithc
fileName = "followers" # Nombre del archivo donde se guardaran los followers. Ej: followers
time = 5 # Segundos cada cuantos se crea un nuevo thread

InstagramAPI = InstagramAPI(yourusername,yourpassword) 
with nostdout(): # Sirve para borrar el error del stdout de login de la API
	ok = InstagramAPI.login() # login
if ok:
	print "Login success as " + yourusername + "!"
	print "Followers will be written in \"" + fileName + "\" file"
	followers(otherusername,fileName,time)
else:
	print "Login error!"