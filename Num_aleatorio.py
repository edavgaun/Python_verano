# El presente programa es un juego para adivinar un número entre 1 y 100

def juego_aleatorio():
  import numpy as np

  aleatorio=np.random.randint(1,100)
  intentos=0

  while True:
    try:
      numero=int(input("Dame un número entero: "))
      intentos+=1
      if numero==aleatorio:
        print("\n\n\n","-"*40)
        print("Felicidades, has adivinado el número")
        print("El número de intentos fué", intentos)
        break
      elif numero>aleatorio:
        print("El número ingresado es mayor")
      else:
        print("El número ingresado es menor")
    except:
      intentos+=1
      print("El valor ingresado no es un número entero")
      
      
if __name__=="__main__":
    juego_aleatorio()
    
    input("Presione enter para finalizar")