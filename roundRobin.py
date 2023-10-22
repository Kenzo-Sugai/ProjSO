import queue

def getFila(processos):
    Fila = queue.Queue()

    for i in processos:
        Fila.put([i, processos[i][1]])

    return Fila

def startRoundRobin(processos, Quantum):

    processosFila = getFila(processos) # Fila de processos ainda não chamados

    print("""
***********************************
***** ESCALONADOR ROUND ROBIN *****
-----------------------------------
------- INICIANDO SIMULACAO -------
-----------------------------------
    """)

    tempo = 0
    newProcess = False
    IOProcess = False
    EndProcess = False
    quitProcess = False
    quantumProcess = False
    item = ""
    novo = ""
    quantumP = ""
    
    Fila = queue.Queue() # Fila CPU

    Fila.put(processosFila.get()[0]) # Push primeiro fila de processos

    while(True): # Enquanto a Fila de CPU não esta vazia

        if(len(Fila.queue) == 0 and len(processosFila.queue) == 0):
            quitProcess = True
        else:
            QuantumCounter = Quantum

            P = Fila.get() # Pegar o primeiro processo da Fila de CPU

        while QuantumCounter > 0:

            print(f"********** TEMPO {tempo} **************")

            if(IOProcess):
                print(f"#[evento] OPERACAO I/O <{item}>")
                IOProcess = False
            if(quantumProcess):
                print(f"#[evento] FIM QUANTUM <{quantumP}>")
                quantumProcess = False
            if(newProcess):
                print(f"#[evento] CHEGADA <{novo}>")
                Fila.put(novo)
                newProcess = False
            if(EndProcess):
                print(f"#[evento] ENCERRANDO <{item}>")
                EndProcess = False

            if(not len(Fila.queue)):
                print("FILA: Nao ha processos na fila")
                if(quitProcess):
                    break
            else:
                print("FILA:", end=" ")
                for i in range(len(Fila.queue)):
                    item = Fila.queue[i]
                    print(f"{item}({processos[item][0]})", end=" ")
                print()

            processos[P][3] += 1

            tempo += 1
            
            processoAtual = processos[P][0]
            
            print(f"CPU: {P}({processoAtual})")

            processoAtual -= 1

            if(len(processosFila.queue) and tempo == processosFila.queue[0][1]):
                novo = processosFila.get()[0]
                newProcess = True

            if(processoAtual == 0):
                processos[P][0] = 0
                EndProcess = True
                item = P
                break
            elif(len(processos[P][2].queue) and len(processos[P][2].queue) and processos[P][2].queue[0] == processos[P][3]):
                processos[P][2].get()
                item = P
                processos[P][0] = processoAtual
                Fila.put(P)
                IOProcess = True
                break
            else:
                processos[P][0] = processoAtual

            QuantumCounter -= 1
        
        if(QuantumCounter == 0):
            quantumP = P
            Fila.put(P)
            quantumProcess = True

        if(quitProcess):
            print("ACABARAM OS PROCESSOS!!!")
            break