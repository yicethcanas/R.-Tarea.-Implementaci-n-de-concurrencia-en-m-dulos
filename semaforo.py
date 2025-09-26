import threading
import time
import random   

bufferCapacidad= 5 
buffer = []

espaciosBuffer = threading.Semaphore(bufferCapacidad)
elementosDispo = threading.Semaphore(0)
accesoBuffer   = threading.Semaphore(1)

def productor(id):
    while True:
        dato = f"Vehiculo {id} {random.randint(1,100)}"
        espaciosBuffer.acquire()
        accesoBuffer.acquire()
        buffer.append(dato)
        print(f"Sendor identificado con {id} genero dato > {dato} | buffer > {len(buffer)} - {bufferCapacidad}")
        accesoBuffer.release()
        elementosDispo.release()
        time.sleep(random.uniform(0.5, 2))
        
def consumidor(id):
    while True:
        elementosDispo.acquire()
        accesoBuffer.acquire()
        dato = buffer.pop(0)
        print(f"Analizando el id {id} - Proceso dato > {dato} | Buffer: {len(buffer)} - {bufferCapacidad}")
        accesoBuffer.release()
        espaciosBuffer.release()
        time.sleep(random.uniform(1, 3))
        

productores= [threading.Thread(target=productor, args=(i,)) for i in range (1, 3)]
consumidores= [threading.Thread(target=consumidor, args=(i,)) for i in range (1, 3)]

for p in productores : p.start()
for c in consumidores : c.start()
