import random

cantidad_turnos = int(input("ingrese la cantidad de turnos : "))
resultado2=0
resultado1=0
centinela = 0
acumuladoturno1=0
acumuladoturno2=0
while centinela < cantidad_turnos :
    centinela +=1
    numero1 = random.randint(1,6)
    numero2 = random.randint(1,6)
    
 

    if numero1 > numero2:
        print(f"jugador1 saco {numero1} ")
        print(f"jugador2 saco {numero2} ")
        print(f"gano el jugador1 en turno {centinela}")
        acumuladoturno1 = numero1+numero2   
        resultado1 += acumuladoturno1
        print(f"puntos: {acumuladoturno1}")
        print("###########################################################")
    elif numero2 > numero1:
        print(f"jugador1 saco {numero1} ")
        print(f"jugador2 saco {numero2}")
        print(f"gano el jugador2 en turno {centinela}")
        acumuladoturno2 = numero2 + numero1 
        print(f"puntos: {acumuladoturno2}")
        resultado2 += acumuladoturno2
        print("###########################################################")
        
    elif numero1 == numero2:
        print(f"fue un empate el jugador1 saco {numero1} jugador2 saco {numero2}")
        print("###########################################################")
    
    
    print(resultado1)
    print(resultado2)

if resultado1 > resultado2:
    print(f"gano el juagdor 1 con {resultado1} de puntos ")
else:
    print(f"gano el juagdor 2 con {resultado2} de puntos")

   


