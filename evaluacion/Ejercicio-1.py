#Se requiere un programa que solicite un nombre de usuario al usuario repetidamente.
#•	Condición: El programa debe seguir pidiendo el nombre mientras el usuario ingrese la palabra 
# "fin" (en cualquier combinación de mayúsculas o minúsculas).
#•	Requisito: Al procesar la entrada, debes eliminar cualquier espacio en blanco accidental 
# que el usuario haya escrito al principio o al final antes de verificar si es igual a "fin".

while True:
 nombre=input("Ingrese su nombre de usuario: ").lower().strip()
 if nombre=="fin":
  print ("Ingreso fin")
 else:
  print("Palabra incorrecta.")
  break
  

  