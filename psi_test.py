def psi_test(tiempo):
    import numpy as np
    from termcolor import colored
    import time

    t_0= time.time() + tiempo
    t_1= 0
    aciertos=0
    intentos=0
    colores=["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

    print("Bienvenido a esta actividad psicométrica.\n")

    while True:
        intentos+=1
        t_1=time.time()
        tiempo_restante=t_0-t_1
        if tiempo_restante<=0:
            print("-"*40)
            print("El ejercicio ha terminado, gracias")
            print("Número de aciertos",aciertos,"/",intentos)
            break
        while True:
            texto=np.random.choice(colores)
            color=np.random.choice(colores)
            if texto!=color:
                break

        texto_coloreado=colored(texto,color)

        print("Quedan",round(tiempo_restante,0),"segundos")
        print(texto_coloreado)
        respuesta=input("¿Color?: ")
        respuesta=respuesta.lower()

        if respuesta==color:
            aciertos+=1
            
            
if __name__=="__main__":
    time=int(input("Indica el tiempo de la prueba: "))
    psi_test(time)
    input("Presiona enter para terminar el programa")