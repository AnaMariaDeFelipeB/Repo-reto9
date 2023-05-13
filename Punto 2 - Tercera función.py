# Función que eleve al cuadrado. 

def elevarNúmerosAlCuadrado (*args) -> int: #Definimos la función con argumentos. 

    lista = [] # Generamos una lista vacia. 
    for numeros in range(*args): # Usando "for" va a iterar los números de 0 hasta el valor dado en el argumento. 
        num = int(input("Ingresar número: "))  # Por cada iteración va a pedir ingresar un número. 
        lista.append(num)  # Va agregar el número a la lista. 

    for datos in lista: # Va iterar todos los números de la lista. 
        elevar = datos**2 # Por cada iteración va a elevar valor al cuadrado. 
        print("El cuadrado del número es " + str(elevar))  # Imprime el valor.


if __name__ == "__main__": # Permite ejecutar la función. 
    a = int(input("Ingrese cantidad de números")) # Definimos variable para ingresar en el argumento. 
    print(elevarNúmerosAlCuadrado(a)) # Imprime la función con los argumentos que definimos.
