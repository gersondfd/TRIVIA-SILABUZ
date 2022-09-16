print("Bienvenido a la TRIVIA")
nombre = input("¿Cual es tu nombre?: ")
print("Hola",nombre, "te mostraremos algunas preguntas sobre Cultura General con alternativas de las cuales deberas digitar la letra de la alternativa correcta.  ")
print("\nEl puntaje maximo es de 100ptos, mucha suerte! :) ")

puntaje=0

print("\n1.- ¿Quién es el autor de la frase 'Pienso, luego existo'? ")
print("\na)Platón","\nb)Galileo Galilei","\nc)Descartes","\nd)Sócrates","\ne)Francis Bacon")
respuesta_1= str(input("\nTu respuesta: "))
while respuesta_1 not in ("a","b","c","d","e","x"):
  respuesta_1= input("\nDebes responder a,b,c,d o e. \nIngresa nuevamente tu respuesta: ")
if respuesta_1== "c":
  print("Respuesta Correcta")
  puntaje +=20
elif respuesta_1=="x":
  print("Marcaste la alternativa secreta, tienes un intento mas")
  print("\n1.- ¿Quién es el autor de la frase 'Pienso, luego existo'? ")
  print("\na)Platón","\nb)Galileo Galilei", 
  "\nc)Descartes","\nd)Sócrates","\ne)Francis Bacon")
  respuesta_1= str(input("\nTu respuesta: "))
  if respuesta_1== "c":
    print("Respuesta Correcta")
    puntaje +=20
  else:
    print("Incorrecto, la respuesta correcta es la alternativa  c) Descartes")
    print("Je pense, donc je suis ,es la frase original, escrita en francés, del filósofo René Descartes (1596-1650). Esta frase resume el pensamiento y el método de Descartes, para quien todo se inicia con la duda.")   
else:
  print("Incorrecto, la respuesta correcta es la alternativa  c) Descartes")
  print("Je pense, donc je suis ,es la frase original, escrita en francés, del filósofo René Descartes (1596-1650). Esta frase resume el pensamiento y el método de Descartes, para quien todo se inicia con la duda.")



print("\n2.- ¿Cuál es el libro más vendido en el mundo después de la Biblia? ")
print("\na)El Señor de los Anillos","\nb)Don Quijote de la Mancha","\nc)El Principito","\nd)Cien años de Soledad","\ne)La Odisea")
respuesta_2= str(input("\nTu respuesta: "))
while respuesta_2 not in ("a","b","c","d","e","y"):
  respuesta_2= input("\nDebes responder a,b,c,d o e. \nIngresa nuevamente tu respuesta: ")
if respuesta_2== "b":
  print("Respuesta Correcta")
  puntaje +=20
elif respuesta_2=="y":
  print("Marcaste la alternativa secreta, tienes un intento mas")
  print("\n2.- ¿Cuál es el libro más vendido en el mundo después de la Biblia? ")
  print("\na)El Señor de los Anillos","\nb)Don Quijote de la Mancha","\nc)El Principito","\nd)Cien años de Soledad","\ne)La Odisea")
  if respuesta_2== "b":
    print("Respuesta Correcta")
    puntaje +=20
  else:
    print("Incorrecto, la respuesta correcta es la alternativa b)Don Quijote de la Mancha")
    print("El ingenioso hidalgo don Quijote de la Mancha es un clásico universal de la literatura española, escrito por Miguel de Cervantes Saavedra (1547-1616).")  
else:
  print("Incorrecto, la respuesta correcta es la alternativa b)Don Quijote de la Mancha")
  print("El ingenioso hidalgo don Quijote de la Mancha es un clásico universal de la literatura española, escrito por Miguel de Cervantes Saavedra (1547-1616).")



print("\n3.-¿Cuánto tiempo tarda la luz del Sol en llegar a la Tierra? ")
print("\na)12 minutos","\nb)1 día","\nc)12 horas","\nd)8 minutos","\ne)8 segundos")
respuesta_3= str(input("\nTu respuesta: "))
while respuesta_3 not in ("a","b","c","d","e","z"):
  respuesta_3= input("\nDebes responder a,b,c,d o e. \nIngresa nuevamente tu respuesta: ")
if respuesta_3== "d":
  print("Respuesta Correcta")
  puntaje +=20
elif respuesta_3== "z":
  print("Marcaste la alternativa secreta, tienes un intento mas")
  print("\n3.-¿Cuánto tiempo tarda la luz del Sol en llegar a la Tierra? ")
  print("\na)12 minutos","\nb)1 día","\nc)12 horas","\nd)8 minutos","\ne)8 segundos")
  if respuesta_3== "d":
    print("Respuesta Correcta")
    puntaje +=20
  else:
    print("Incorrecto, la respuesta correcta es la alternativa d)8 minutos")
  print("El tiempo que tarda la luz del Sol en llegar a la Tierra se calcula dividiendo la distancia que hay entre el Sol y la Tierra, aproximadamente 150 000 000 km, entre la velocidad de la luz, que es 300 000 km/s: 150 000 000 km÷300 000 km/s= 500 s; 500 s ÷ 60 s/min = 8,3 minutos.")  
else:
  print("Incorrecto, la respuesta correcta es la alternativa d)8 minutos")
  print("El tiempo que tarda la luz del Sol en llegar a la Tierra se calcula dividiendo la distancia que hay entre el Sol y la Tierra, aproximadamente 150 000 000 km, entre la velocidad de la luz, que es 300 000 km/s: 150 000 000 km÷300 000 km/s= 500 s; 500 s ÷ 60 s/min = 8,3 minutos.")



print("\n4.-¿A quién se le atribuye la frase: Solo sé que no sé nada?")
print("\na)Aristóteles","\nb)Nietszche","\nc)Sófocles","\nd)Salomón","\ne)Sócrates")
respuesta_4= str(input("\nTu respuesta: "))
while respuesta_4 not in ("a","b","c","d","e","p"):
  respuesta_4= input("\nDebes responder a,b,c,d o e. \nIngresa nuevamente tu respuesta: ")
if respuesta_4== "e":
  print("Respuesta Correcta")
  puntaje +=20
elif respuesta_4== "p":
  print("Marcaste la alternativa secreta, tienes un intento mas")
  print("\n4.-¿A quién se le atribuye la frase: Solo sé que no sé nada?")
  print ("\na)Aristóteles","\nb)Nietszche","\nc)Sófocles","\nd)Salomón","\ne)Sócrates")
  if respuesta_4== "e":
    print("Respuesta Correcta")
    puntaje +=20
  else:
    print("Incorrecto, la respuesta correcta es la alternativa e)Sócrates")
    print("Solo sé que no sé nada o solo sé que nada sé es una frase atribuida al filósofo griego Sócrates (470-399 a.de C) que se refiere a reconocer que es un ignorante.") 
else:
  print("Incorrecto, la respuesta correcta es la alternativa e)Sócrates")
  print("Solo sé que no sé nada o solo sé que nada sé es una frase atribuida al filósofo griego Sócrates (470-399 a.de C) que se refiere a reconocer que es un ignorante.")



print("\n5.-¿Cuál de estos países se extiende entre dos continentes?")
print("\na)Tanzania","\nb)Groenlandia","\nc)Egipto","\nd)Filipinas","\ne)Rusia")
respuesta_5= str(input("\nTu respuesta: "))
while respuesta_5 not in ("a","b","c","d","e","w"):
  respuesta_5= input("\nDebes responder a,b,c,d o e. \nIngresa nuevamente tu respuesta: ")
if respuesta_5== "e":
  print("Respuesta Correcta")
  puntaje +=20
elif  respuesta_5== "w":
  print("Marcaste la alternativa secreta, tienes un intento mas")
  print("\n5.-¿Cuál de estos países se extiende entre dos continentes?")
  print("\na)Tanzania","\nb)Groenlandia","\nc)Egipto","\nd)Filipinas","\ne)Rusia")
  respuesta_5= str(input("\nTu respuesta: "))
  if respuesta_5== "e":
    print("Respuesta Correcta")
    puntaje +=20
  else:
    print("Incorrecto, la respuesta correcta es la alternativa e)Rusia")
    print("Rusia, cuya capital es Moscú, es el país más extenso que abarca parte del continente asiático y del continente europeo.")
else:
  print("Incorrecto, la respuesta correcta es la alternativa e)Rusia")
  print("Rusia, cuya capital es Moscú, es el país más extenso que abarca parte del continente asiático y del continente europeo.")

print(" \nTu puntaje final es de ",puntaje,"ptos")

'''Fuente de la preguntas: https://www.todamateria.com/preguntas-de-cultura-general/''' 