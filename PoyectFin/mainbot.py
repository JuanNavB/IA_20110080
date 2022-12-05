import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow
import tensorflow as tf
import json
import random
import pickle 

##nltk.download('punkt')

with open("contenido.json") as file:
	data = json.load(file)

##print(data)

palabras=[]
tags=[]
aux1=[]
aux2=[]

for contenido in data["contenido"]:
	for patrones in contenido["patrones"]:
		auxPalabra = nltk.word_tokenize(patrones)
		palabras.extend(auxPalabra)
		aux1.append(auxPalabra)
		aux2.append(contenido["tag"])

		if contenido["tag"] not in tags:
			tags.append(contenido["tag"])

palabras = [stemmer.stem(w.lower()) for w in palabras if w!="?"]
palabras = sorted(list(set(palabras)))
tags = sorted(tags)

entrenamiento = []
salida = []

salidaV = [0 for _ in range(len(tags))]

for x, doc in enumerate(aux1):
	cubeta = []
	auxPalabra = [stemmer.stem(w.lower()) for w in doc]
	for w in palabras:
		if w in auxPalabra:
			cubeta.append(1)
		else:
			cubeta.append(0)
	filaSalida = salidaV[:]
	filaSalida[tags.index(aux2[x])] = 1
	entrenamiento.append(cubeta)
	salida.append(filaSalida)

entrenamiento = numpy.array(entrenamiento)
salida = numpy.array(salida)

tf.compat.v1.reset_default_graph()

red = tflearn.input_data(shape=[None,len(entrenamiento[0])])
red = tflearn.fully_connected(red,10)
red = tflearn.fully_connected(red,10)
red = tflearn.fully_connected(red,len(salida[0]), activation="softmax")
red = tflearn.regression(red)

modelo = tflearn.DNN(red)
modelo .fit(entrenamiento,salida,n_epoch = 1000,batch_size = 50,show_metric = True)
modelo.save("modelo.tflearn")

def  mainbot():
	while True:
		entrada = input("Tu: ")
		cubeta = [0 for _ in range(len(palabras))]
		entProces = nltk.word_tokenize(entrada)
		entProces = [stemmer.stem(palabra.lower()) for palabra in entProces]
		for palabraInd in entProces:
			for i, palabra in enumerate(palabras):
				if palabra == palabraInd:
					cubeta[i] = 1 

		result = modelo.predict([numpy.array(cubeta)])
		resultIndices = numpy.argmax(result)
		tag = tags[resultIndices]

		for tagAux in data["contenido"]:
			if tagAux["tag"] == tag:
				respuesta = tagAux["respuestas"]
		print("BOT: ", random.choice(respuesta))

mainbot()