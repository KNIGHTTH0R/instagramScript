#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import json

yourusername = "" # username/password de cuenta ig con la loguearas
yourpassword = ""

InstagramAPI = InstagramAPI(yourusername,yourpassword) # username/password de cuenta ig con la loguearas
InstagramAPI.login() # login

otherusername = "" # @usuario al cual se buscara
InstagramAPI.searchUsername(otherusername) 

usuario = InstagramAPI.LastJson # devuelve la respuesta JSON de la funcion anterior
del usuario["status"] # linea que borra status del JSON

print json.dumps(usuario, indent=4) # imprimo el JSON de los datos del @usuario buscado

username = usuario["user"]["username"] 
usernameId = usuario["user"]["pk"] # al parecer "pk" es la "id"
name = usuario["user"]["full_name"]
followerCount = usuario["user"]["follower_count"]

print "\n\n---------------------------------------\n\n"

print "Cantidad de followers de " + str(name) + " (@" + str(username) + ") : " + str(followerCount) 
print 
InstagramAPI.getUserFollowers(usernameId) # obtiene todos los followers de cierto usuario
prueba = InstagramAPI.LastJson

print "Los seguidores de " + str(name) + " (@" + str(username) + ") son : "
for user in prueba["users"]:
	print "\t" + str(user["username"])

# InstagramAPI.getUserFeed(usernameId)
# print json.dumps(InstagramAPI.LastJson["items"][0],indent=4)