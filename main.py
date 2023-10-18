import queue

def readfile(processos):
    arq = open("entrada.txt")
    linhas = arq.readlines()
    for linha in linhas:
        partes = linha.strip().split()
        fila = queue.Queue()
        for i in range(1,len(partes)):
            fila.put(int(partes[i]))
        processos[partes[0]] = fila

    return processos

def roundRobin(processos, Quantum):

    print("""
-----------------------------------
------- INICIANDO SIMULACAO -------
-----------------------------------
    """)

    tempo = 0

    while(len(processos) > 0):

        print(f"********** TEMPO {tempo} **************")

        remover = []
        QuantumCounter = 0

        for i in processos.keys():
        
            Pn = processos[i][0]
            
            Pn -= 1

            if(Pn <= 0):
                remover.append(i)
            else:
                print(f"CPU: {i}({Pn})")
                processos[i].queue[0] = Pn


        for i in remover:
            processos[i].get()
            if(processos[i].empty):
                processos.pop(i)
        
        remover.clear()
        tempo += 1
        

####  apagar os testes abaixo

processos = {

    "P1": [1, 10, queue.Queue()]
}

processos["P1"][2].put(2)
processos["P1"][2].put(1)

#processos = readfile(processos)

Quantum = 4

#roundRobin(processos, Quantum)
