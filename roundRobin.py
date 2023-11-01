import queue

def getFila(processos):
    Fila = queue.Queue()

    for i in processos:
        Fila.put([i, processos[i][1]])

    return Fila

class roundRobin:
    
    def __init__(self, process, quantum):
        self.process = process
        self.quantum = quantum
        self.listProcess = [
            
        ]

    def start(self):

        print("""
***********************************
***** ESCALONADOR ROUND ROBIN *****
-----------------------------------
------- INICIANDO SIMULACAO -------
-----------------------------------
    """)

        processQueue = getFila(self.process) # Fila de processos ainda não chamados

        timeProcess = 0 # <int> loop time
        newProcess = False
        IOProcess = False
        endProcess = False
        quitProcess = False
        quantumProcess = False
        item = ""
        novo = ""
        quantumP = ""
        
        Fila = queue.Queue() # Fila CPU

        Fila.put(processQueue.get()[0]) # Push primeiro fila de processos

        while(True): # Enquanto a Fila de CPU não esta vazia

            if(len(Fila.queue) == 0 and len(processQueue.queue) == 0):
                quitProcess = True
            else:
                QuantumCounter = self.quantum

                P = Fila.get() # Pegar o primeiro processo da Fila de CPU

            while QuantumCounter > 0:

                print(f"********** TEMPO {timeProcess} **************")

                
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
                if(endProcess):
                    print(f"#[evento] ENCERRANDO <{item}>")
                    endProcess = False

                if(not len(Fila.queue)):
                    print("FILA: Nao ha processos na fila")
                    if(quitProcess):
                        break
                else:
                    print("FILA:", end=" ")
                    for i in range(len(Fila.queue)):
                        item = Fila.queue[i]
                        print(f"{item}({self.process[item][0]})", end=" ")
                    print()

                self.process[P][3] += 1

                timeProcess += 1
                
                processoAtual = self.process[P][0]
                
                print(f"CPU: {P}({processoAtual})")

                processoAtual -= 1

                if(len(processQueue.queue) and timeProcess == processQueue.queue[0][1]):
                    novo = processQueue.get()[0]
                    newProcess = True

                if(processoAtual == 0):
                    self.process[P][0] = 0
                    endProcess = True
                    item = P
                    break
                elif(len(self.process[P][2].queue) and len(self.process[P][2].queue) and self.process[P][2].queue[0] == self.process[P][3]):
                    self.process[P][2].get()
                    item = P
                    self.process[P][0] = processoAtual
                    Fila.put(P)
                    IOProcess = True
                    break
                else:
                    self.process[P][0] = processoAtual

                QuantumCounter -= 1
            
            if(QuantumCounter == 0):
                quantumP = P
                Fila.put(P)
                quantumProcess = True

            if(quitProcess):
                print("ACABARAM OS PROCESSOS!!!")
                break
