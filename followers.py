#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import json
import contextlib
import io
import sys
import threading

first = True
# esta funcion hace que no se vea el stdout cuando corro una funcion
@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = io.BytesIO()
    yield
    sys.stdout = save_stdout

def followers():
	from InstagramAPI import InstagramAPI
	global first

	text_file = open("followers", "a")
	time = 60 # segundos
	threading.Timer(time, followers).start() # crea un thread cada "time" tiempo 

	yourusername = "" # username/password de cuenta ig con la loguearas
	yourpassword = ""
	InstagramAPI = InstagramAPI(yourusername,yourpassword) 
	with nostdout():
		InstagramAPI.login() # login
	
	otherusername = "" # @usuario al cual se buscara
	InstagramAPI.searchUsername(otherusername) 
	usuario = InstagramAPI.LastJson # devuelve la respuesta JSON de la funcion anterior

	username = usuario["user"]["username"] 
	usernameId = usuario["user"]["pk"] # al parecer "pk" es la "id"
	name = usuario["user"]["full_name"]
	followerCount = usuario["user"]["follower_count"]
	s = ""
	s += "\n"
	s += "Cantidad de followers de " + str(name) + " (@" + str(username) + ") : " + str(followerCount)
	first = False
	text_file.write("%s" % s)
	text_file.close()

followers()