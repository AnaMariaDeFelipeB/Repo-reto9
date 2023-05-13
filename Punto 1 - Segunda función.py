# Función para calcular el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

if __name__ == "__main__": # Permite ejecutar la función. 
    c : int = int(input("Ingrese población infectada actualmente: ")) # Pide al usuario ingresar número. 
    d : int = int(input("Ingrese días a partir de hoy: ")) # Pide al usuario ingresar número. 

    contagios = (lambda x, z: x+(2**z))(c,d) # Definimos función anónima. 


    print("Partiendo de " + str(c) + " contagiados después de "+ str(d) + " días habrá un total de " + str(contagios) + " contagiados") # Imprime