# Función que calcuale el factorial

def factorial (*args) -> int: # Definimos la función con argumentos. 


    for numero in args: # Establecemos un for que itere los datos del argumento.  
        sum : int = 1  # Definimos variable. 
        factoriales : int = 1  # Definimos variable. 
        while numero >= sum:   #Establecemos condición. (Mientras que el valor de numero sea mayor o igual a sum)
            factoriales *= sum  # Si cumple lo anterior, va actualizar la variable multiplicando sum al valor de factoriales almacenado. 
            sum +=1 # Actualiza. 


    return factoriales # Devuelve 


if __name__ == "__main__":  # Permite ejecutar la función. 
    a : int = int(input("Ingrese número: ")) # Definimos variable para ingresar en el argumento. 
    print("El factorial del número es: " + str(factorial(a))) # Imprime la función con los argumentos que definimos.