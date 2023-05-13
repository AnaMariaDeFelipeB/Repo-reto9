# Función matemática para calcular el área y el perimetro de un rectangulo. (Reto 6)

if __name__ == "__main__": # Permite ejecutar la función. 
    lado1: int = int(input("Ingrese lado 1: ")) # Pide al usuario ingresar número. 
    lado2 : int = int(input("Ingrese lado 2: ")) # Pide al usuario ingresar número.  

    area = (lambda x, y: x*y)(lado1, lado2) # Definimos función anónima. 
    perimetro = (lambda x, y: 2*(x+y))(lado1, lado2) # Definimos función anónima.  

    print("El área del rectangulo ingresado es: " + str(area) + " \n Y el perimetro es: " + str(perimetro)) # Imprime