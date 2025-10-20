#Criação de processo zumbi

import os
import time
import sys

print(f"Processo Pai iniciado com PID: {os.getpid()}")

#Criando o primeiro filho
try:
    filho1 = os.fork()
except OSError:
    sys.exit("Erro: não foi possível criar o primeiro filho")

if filho1 == 0:
    print(f"Filho 1: Eu nasci! Meu PID é {os.getpid()}. O PID do meu pai é {os.getppid()}")
    #Filho 1 termina imediatamente
    print("FILHO 1: Terminei meu trabalho!")

    sys.exit(0) #Importante para que o filho 1 não continue executando o código do pai
else:
    #Parte executada pelo pai
    print(f"PAI: Criei meu primeiro filho com PID: {filho1}")

    #Criando o segundo filho
    try:
        filho2 = os.fork()
    except OSError:
        sys.exit("Erro: não foi possível criar o segundo filho")
    
    if filho2 == 0:
        print(f"Filho 2: Eu nasci! Meu PID é {os.getpid()}. O PID do meu pai é {os.getppid()}.")
        #Filho 2 termina imediatamente
        print("FILHO 2: Terminei meu trabalho!")
        sys.exit(0)

    else:
        #Parte executada pelo pai
        print(f"PAI: Criei meu segundo filho com PID: {filho2}")
        print("PAI: Meus filhos já devem ter finalizado, mas não vou chamar os.wait()")
        print("PAI: Vou dormir por 30 segundos. Os filhos ficaram como zumbis durante esse tempo")
        #Analisar em outro terminal, usando "ps aux | grep 'Z+'", os processos zumbis
        time.sleep(30)
        print("PAI: Vou finalizar...")
