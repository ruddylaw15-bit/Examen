#Crea un programa que pida al usuario ingresar un comentario sobre un producto.
#•	Condición: Si el comentario contiene la palabra "malo", el programa debe 
# imprimir: "Tu comentario no cumple con las normas, intenta de nuevo.".
#•	Requisito: La validación debe ignorar si el usuario escribió "MALO", 
# "malo" o "MaLo". Si el comentario es aceptable, el programa debe imprimir: "Comentario publicado con éxito."
comentario=input("Ingrese un comentario: ")
if comentario==len("malo"):
    print("Tu comentario no cumple con las normas, intenta de nuevo.")
else:
    print("Comentario publicado con éxito.")