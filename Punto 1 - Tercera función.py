# Función para calcular el volumen y area superficial de una esfera

import math # Importamos función de matematicas. 
pi = math.pi # Llamamos a la función. 

if __name__ == "__main__": # Permite ejecutar la función. 
    r : int = int(input("Ingrese radio: ")) # Pide al usuario ingresar número. 

    volumen = (lambda x: (4/3)*pi*(x**3)) (r) # Definimos función anónima. 
    superfie = (lambda x: 4*pi*(r**2)) (r) # Definimos función anónima. 

print("El volumen y area de la esfera es " + str(round(volumen, 2)) + " y " + str(round(superfie, 2)) + " respectivamente.") # Imprime