numero_1 = int(input("Ingrese un numero entero: "))
numero_2 = int(input("Ingrese otro numero entero: "))
division= (numero_1/numero_2)
print("Su division es :", division)
if  numero_1 % numero_2 == 0:
  print("La division es exacta")
else:
  print("La division no es exacta")

  
  
numero_1 = int(input("Ingrese un numero entero: "))
numero_2 = int(input("Ingrese otro numero entero: "))
numero_3 = int(input("Ingrese otro numero entero: "))

if numero_1 == numero_2 == numero_2:
  print("*** Son los tres iguales ***")
elif numero_1 == numero_2 or numero_1 == numero_3 or numero_2 == numero_3:
  print("*** Hoy dos iguales ***")
else:
  print("*** Son los tres distintos ***")