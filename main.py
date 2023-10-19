import queue

def readfile():

    processosLeitura = {}

    arq = open("entrada.txt")
    linhas = arq.readlines()
    for linha in linhas:
        partes = linha.strip().split()
        fila = queue.Queue()
        if len(partes) == 4:
            numeros = partes[3].split(",")
            for i in numeros:
                fila.put(int(i))
        processosLeitura[partes[0]] = [int(partes[1]), int(partes[2]),fila]

    return dict(sorted(processosLeitura.items(), key=lambda item: item[1][1]))


def removerDic(remover, processos):
    for i in remover:
            if(processos[i][0] == 0):
                processos.pop(i)

def getFila(processos):
    Fila = queue.Queue()

    for i in processos:
        Fila.put([i, processos[i][1]])

    return Fila

def roundRobin(processos, Quantum):

    processosFila = getFila(processos) # Fila de processos ainda não chamados

    print("""
-----------------------------------
------- INICIANDO SIMULACAO -------
-----------------------------------
    """)

    tempo = 0
    IO = 0
    
    Fila = queue.Queue() # Fila CPU

    Fila.put(processosFila.get()[0]) # Push primeiro fila de processos

    while(Fila.not_empty): # Enquanto a Fila de CPU não esta vazia

        QuantumCounter = Quantum

        P = Fila.get() # Pegar o primeiro processo da Fila de CPU

        while QuantumCounter > 0:

            print(f"********** TEMPO {tempo} **************")
            if(not len(Fila.queue)):
                print("FILA: Nao ha processos na fila")
            else:
                print("FILA:", end=" ")
                for i in range(len(Fila.queue)):
                    item = Fila.queue[i]
                    print(f"{item}({processos[item][0]})", end=" ")
                print()

            IO += 1

            tempo += 1
            
            processoAtual = processos[P][0]
            
            print(f"CPU: {P}({processoAtual})")

            processoAtual -= 1

            if(processoAtual == 0):
                processos[P][0] = 0
                break
            elif(len(processos[P][2].queue) and processos[P][2].queue[0] == IO):
                processos[P][0] = processoAtual
                
                Fila.put(P)
                IO = 0
                break
            else:
                processos[P][0] = processoAtual

            QuantumCounter -= 1
            
            if(len(processosFila.queue) and tempo == processosFila.queue[0][1]):
                Fila.put(processosFila.get()[0])
        
        if(QuantumCounter == 0):
            Fila.put(P)

processos = readfile()

Quantum = 4

roundRobin(processos, Quantum)

print("ACABOOOO")
