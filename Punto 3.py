def potenciaRecursiva (n:int, x:int)-> int: # Definimos la función. 
  if x == 1: # Establecemos condición. (Que x sea igual a 1)
    return n # Si cumple la condición, va a devolver el valor de n. 
  return n*potenciaRecursiva(n, x-1) # Hasta que no cumpla la condición va a repetir la multpiplicación de n entre n. Y de paso va actualizar a x, restandole 1. 

if __name__ == "__main__": # Permite ejecutar la función. 
  n = int(input("Ingrese base: ")) # Definimos variable para ingresar en el argumento. 
  x = int(input("Ingrese exponente: ")) # Definimos variable para ingresar en el argumento. 
  potencia1 = potenciaRecursiva(n,x) # Llamamos la función mediante una variable. 
  print("El número " + str(n) + " a la " + str(x) + " es " + str(potencia1))  # Imprime. 