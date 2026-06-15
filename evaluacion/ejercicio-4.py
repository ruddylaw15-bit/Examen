#Crea un sistema que pida una contraseña al usuario.
#•	Condición: Mientras la contraseña sea igual a "12345" 
# (o contenga espacios al inicio/final que al quitarlos den "12345"), el programa debe 
# pedir al usuario: "Contraseña insegura, ingresa otra:".
#•	Finalización: Una vez que el usuario ingrese una contraseña diferente,
# el programa debe imprimir: "Acceso concedido".
while True:
    contraseña=input("Ingrese una contraseña: ").strip()
    if contraseña=="12345":
        print("Contraseña insegura, ingresa otra.")
    else:
        print("Acceso concedido")
        break