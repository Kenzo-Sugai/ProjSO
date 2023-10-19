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
        Fila.put([i, processos[i]])

    return Fila

def roundRobin(processos, Quantum):

    processosFila = getFila(processos)

    print("""
-----------------------------------
------- INICIANDO SIMULACAO -------
-----------------------------------
    """)

    tempo = 0
    IO = 0
    
    Fila = queue.Queue()

    Fila.put(processosFila.get())

    while(Fila.not_empty):

        remover = []
        QuantumCounter = Quantum

        P = Fila.get()[0]

        print(P)

        while QuantumCounter > 0:

            print(f"********** TEMPO {tempo} **************")
            if(Fila.empty):
                print("FILA: Nao ha processos na fila")
            else:
                print("FILA:")
                for i in range(Fila.qsize):
                    item = Fila.queue[i]
                    print("{item}({processos[item][0]})", end=" ")

            IO += 1

            processoAtual = processos[P][0]
            
            print(f"CPU: {P}({processoAtual})")

            processoAtual -= 1

            if(processoAtual == 0):
                processos[P][0] = 0
                remover.append(P)
                break
            elif(processos[P][2].queue[0] == IO):
                processos[P][0] = processoAtual
                Fila.put(P)
                IO = 0
                break
            else:
                processos[P][0] = processoAtual

            QuantumCounter -= 1

            tempo += 1

            if(tempo == processosFila.queue[0]):
                Fila.put(processosFila.get())
        
        if(QuantumCounter == 0):
            Fila.put(P)

        removerDic(remover, processos)
        
        remover.clear()

processos = readfile()

Quantum = 4

roundRobin(processos, Quantum)