#Execução normal

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
    time.sleep(4) #Simulando o filho 1 trabalhando por 4 segundos
    print("FILHO 1: Terminei meu trabalho!")

    sys.exit(0) #Importante para que o filho 1 não continue executando o código do pai
else:
    #Parte executada pelo pai
    print(f"PAI: Criei meu primeiro filho com PID: {filho1}")

    #Craindo o segundo filho
    try:
        filho2 = os.fork()
    except OSError:
        sys.exit("Erro: não foi possível criar o segundo filho")
    
    if filho2 == 0:
        print(f"Filho 2: Eu nasci! Meu PID é {os.getpid()}. O PID do meu pai é {os.getppid()}.")
        time.sleep(2) #Simulando o filho 2 trabalhando por 2 segundos
        print("FILHO 2: Terminei meu trabalho!")
        sys.exit(0)

    else:
        #Parte executada pelo pai
        print(f"PAI: Criei meu segundo filho com PID: {filho2}")
        print("PAI: Agora vou esperar meus filhos terminarem...")

        #O pai espera pelo término de algum filho (o que terminar primeiro)
        pid_terminado1, status1 = os.wait()

        if os.WIFEXITED(status1):
            print(f"PAI: Meu filho com PID {pid_terminado1} terminou normalmente.")

        #O pai espera pelo término do outro filho
        pid_terminado2, status2 = os.wait()

        if os.WIFEXITED(status2):
            print(f"PAI: Meu filho com PID {pid_terminado2} terminou normalmente.")

        print("Processo PAI: Todos os filhos terminaram.")


