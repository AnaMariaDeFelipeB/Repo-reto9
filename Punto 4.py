import time # Llama la función. 

# Tiempo función recursiva. 
start_time = time.time() # Comienza a contar el tiempo. 

# Comienza a funcionar el código. 
def fiboRecursivo(n : int )-> int:
    if n <=1:
        # caso base
        return 1
    else:
        # condicion
        return fiboRecursivo(n-1)+fiboRecursivo(n-2)  
    
if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serieFibo = fiboRecursivo(num)
  print("El último número de la serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))

# termina de funcionar el código. 
end_time = time.time() # Detiene el tiempo
timer = end_time - start_time # El tiempo total es la resta entre el tiempo final, menos el tiempo inicial. 





# Tiempo función normal. 
start_time = time.time()

# Comienza a funcionar el código
def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serieFibo = fibo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
  
# termina de funcionar el código. 
end_time = time.time() # Detiene el tiempo
timer2 = end_time - start_time # El tiempo total es la resta entre el tiempo final, menos el tiempo inicial. 



print("fiboRecursivo se demoró " + str(timer) +  " en correr") # Imprime. (Valor del primer timer)
print("La función normal se demoró " + str(timer2) +  " en correr") # Imprime. (Valor del segundo timer)




# A partir de valores de 34 hacia arriba la diferencia comienza a ser significativa. 