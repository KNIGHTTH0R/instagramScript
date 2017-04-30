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
import math
import time
import random

# esta funcion hace que no se vea el stdout cuando corro una funcion
@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = io.BytesIO()
    yield
    sys.stdout = save_stdout

def followers(otherusername,fileName="followers",threadtime=60):
	# text_file = open(fileName, "a")

	# threading.Timer(threadtime, followers, [otherusername,fileName,threadtime]).start() # crea un thread cada "time" tiempo 

	InstagramAPI.searchUsername(otherusername) 
	usuario = InstagramAPI.LastJson # devuelve la respuesta JSON de la funcion anterior
	usernameId = usuario["user"]["pk"] # al parecer "pk" es la "id"
	followerCount = usuario["user"]["follower_count"]
	cantIters = int(math.ceil(followerCount/200.0))
	c = 0
	msg = ''
	nextMaxId = ''
	start = time.time()
	sys.stderr.write('\n')
	contador = 1
	while c < followerCount:
		InstagramAPI.getUserFollowers(usernameId,nextMaxId)
		followersJson = InstagramAPI.LastJson
		allUsers = followersJson["users"]	
		# d=0
		for user in allUsers:
			print user["username"]
			error = str(c) + '/' + str(followerCount) + '\r'
			sys.stderr.write(error)
			c = c+1
			# d = d+1
		if c < followerCount : nextMaxId = followersJson["next_max_id"]
		r = random.randint(1,3)
		time.sleep(r)
		# msg += str(d) + " || " 
		contador += 1

	print usuario["user"]["follower_count"]
	print c
	end = time.time()
	print "Tiempo = " + str(end - start)
	print msg
	# text_file.write("%s" % s)
	# text_file.close()

#MAIN:
#Valores a completar
yourusername = "joseduarte7051" # COMPLETAR CON username/password de cuenta ig con la loguearas. Ej: jcwithc
yourpassword = "asd123AA" # Ej: pepe
# otherusername = "exoticos_en_argentina" # COMPLETAR CON usuario al cual se buscara. Ej: jcwithc
otherusername = "nicoo.vacca" # COMPLETAR CON usuario al cual se buscara. Ej: jcwithc
fileName = "followers" # Nombre del archivo donde se guardaran los followers. Ej: followers
threadtime = 5 # Segundos cada cuantos se crea un nuevo thread

InstagramAPI = InstagramAPI(yourusername,yourpassword) 
with nostdout(): # Sirve para borrar el error del stdout de login de la API
	ok = InstagramAPI.login() # login
if ok:
	print "Login success as " + yourusername + "!"
	print "Followers will be written in \"" + fileName + "\" file"
	followers(otherusername,fileName,threadtime)
else:
	print "Login error!"