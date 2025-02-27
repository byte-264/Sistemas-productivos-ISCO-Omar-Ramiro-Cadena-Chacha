# OMAR RAMIRO CADENA CHACHA

frase = input("Escribe tu frase: ")

palabra = frase.split() # <-- Se separa la frases por palabras

longitud = palabra.__len__() # <-- Se saca el numero de palabras de toda la frase


# ⬇️ En este array se almacenan las longitudes de cada palabra 
# ["pelota", "playa"]  [8, 5]
longitud_palabras = []

#Mediante un ciclo for añado cada longitud al arreglo llamado "longitud_palabras"
for i in palabra:
    longitud_palabras.append(len(i)) # <-- El metodo len el numero de letras

print("Tu frase tiene", longitud, "palabras")

print("El promedio de palabras: ", (sum(longitud_palabras)/longitud))

print("La palabra más larga tiene", max(longitud_palabras), 
"letras y es la palabra", palabra[longitud_palabras.index(max(longitud_palabras))])