palabra = input("Ingrese una palabra: ")

letra = "Letras"

print(palabra, len(palabra))

if len(palabra) <4 :
    print("Faltan letras. Intenta de nuevo.")

elif len(palabra) <=8 :
    print("Palabra Corrcta!")

elif len(palabra) >8 :
    print("Sobran letras. Intenta de nuevo.")


x = int(input("Ingrese una coordenanda para el eje X: "))

y = int(input("Ingrese una coordenanda para el eje Y: "))

if ((x > 0) and (y > 0)):
    print("Punto en el Primer Cuadrante")

elif ((x < 0) and (y > 0)):
    print("Punto en el Segundo Cuadrante")

elif ((x < 0) and (y < 0)):
    print("Punto en el Tercer Cuadrante")

elif ((x > 0) and (y < 0)):
    print("Punto en el Cuarto Cuadrante")


 






