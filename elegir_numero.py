import random

print("\nPiensa un número e intenta no olvidarte, si hace falta apuntalo en una hoja.")

def adivinar_numero():
    while True:
        rango = input("\nAhora dame una pista: ¿entre que rango de números tengo que buscar?\nEscribe los dos números separados por un espacio: ")
        min_max = rango.split()
        minimo = int(min_max[0])
        maximo = int(min_max[1])
        
        if minimo > maximo: minimo, maximo = maximo, minimo
        modo = input("\n¿Prefieres que lo acierto al azar y mediante un algoritmo?\nTecla '1'- Azar\nTecla '2'- Algoritmo\n")
        
        intentos = 1
        acertado = False
        
        while minimo <= maximo and acertado == False:
            if modo == "1": numero = random.randint(minimo, maximo)
            elif modo == "2": numero = int((minimo + maximo)//2)
            else: 
                print("Vamos a empezar de nuevo a ver si esta vez te aclaras")
                break
        
            print("\nTodo me hace pensar que se trata del número:", numero)
            respuesta = input("Tecla '+' si es mayor\nTecla '-' si es menor\no Tecla '0' si he acertado\n")
            if respuesta == "+": minimo = numero + 1
            elif  respuesta == "-": maximo = numero - 1
            elif respuesta == "0":
                if intentos == 1: print("\nSoy un máquina la he acertado a la primera.")
                if intentos > 1: print("\nFantástico. Solo he necesitado", intentos, "intentos.")
                acertado = True
                break
            else: 
                print("No he ententido tu respuesta, repitamoslo")
                intentos -= 1
            intentos += 1

        if minimo > maximo and acertado == False:
            print("\nPero que tramposo eres, se me han quitado las ganas de jugar contigo.")
            break
        elif intentos == 1 and acertado == True: break
        elif intentos >1 and acertado == True:
            opcion = input("Me ha encantado este juego. Te apetece jugar de nuevo? Estoy seguro que puedo hacerlo mejor.\nTecla 'y' para repetir\ncualquier otra tecla para salir\n")
            if opcion != "y": break
            
            
adivinar_numero()