#El usuario ingresa una frase y el programa debe procesarla.
#•	Condición: Si la frase contiene la palabra "triste", el programa debe 
# reemplazar automáticamente esa palabra por "feliz" e imprimir la nueva frase resultante.
#•	Condición adicional: Si la frase no contiene la palabra "triste",
#  el programa debe imprimir la frase original en mayúsculas.

frase=input("Ingrese una frase: ").lower()
if frase==len("triste").replace("feliz"):
    print("se remplazo la palabra triste:")
else:
    print("no contiene la plabra triste y tu comentario es:",frase)