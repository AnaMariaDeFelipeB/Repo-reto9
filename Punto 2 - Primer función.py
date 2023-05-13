# Función para calcular el promedio de 5 números. 

def promedio (*args) -> float: # Definimos la función con argumentos. 
    sum : int = 0 # Establecemos valor variable. (Esta equivaldra a las actualizaciones que se le irán haciendo)

    for numeros in args: # Establecemos un for que itere los datos del argumento.  
        sum += numeros # Actualiza (Va a sumar los datos del argumento). 
    
    media = sum/(len(args)) # Opera. (Saca promedio)

    return media # Devuelve la operación. 

if __name__ == "__main__": # Permite ejecutar la función. 
    a: int = int(input("Ingrese número: "))  # Definimos variable para ingresar en el argumento. 
    b: int = int(input("Ingrese número: "))   
    c: int = int(input("Ingrese número: "))  
    d: int = int(input("Ingrese número: "))  
    e: int = int(input("Ingrese número: "))  
    
    print("El promedio de los dos primeros números es: " + str(promedio(a,b)))  # Imprime la función con los argumentos que definimos. 
    print("El promedio de los tres primeros números es: " + str(promedio(a,b,c)))  
    print("El promedio de los cuatro primeros números es: " + str(promedio(a,b,c,d)))  
    print("El promedio de números es: " + str(promedio(a,b,c,d,e))) 