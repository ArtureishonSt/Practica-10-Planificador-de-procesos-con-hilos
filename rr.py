class Proceso:
    def __init__(self, nombre, tiempo_ejecucion, prioridad):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.prioridad = prioridad


def cargar_procesos(nombre_archivo):
    procesos = []
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            nombre, tiempo, prioridad = linea.strip().split(', ')
            proceso = Proceso(nombre, int(tiempo), int(prioridad))
            procesos.append(proceso)
    return procesos


def round_robin(procesos):
    quantum = 3
    tiempo_total = 0
    while procesos:
        proceso_actual = procesos.pop(0)
        if proceso_actual.tiempo_ejecucion > quantum:
            print(f"Ejecutando {proceso_actual.nombre} (Tiempo restante: {proceso_actual.tiempo_ejecucion - quantum})")
            proceso_actual.tiempo_ejecucion -= quantum
            procesos.append(proceso_actual)
            tiempo_total += quantum
        else:
            print(f"Ejecutando {proceso_actual.nombre} (Tiempo restante: 0)")
            tiempo_total += proceso_actual.tiempo_ejecucion

    print(f"Tiempo total de ejecución: {tiempo_total}")


'''
El algoritmo Round Robin con un quantum de 3 funciona de la siguiente manera:

    Se ejecutan los procesos en orden de llegada.

    Cada proceso recibe un tiempo de CPU de 3 unidades 
    (esto es el quantum). Si el proceso termina su ejecución en ese tiempo, 
    se completa; de lo contrario, se coloca nuevamente en la cola de procesos listos para futuras ejecuciones.

    El algoritmo continúa asignando el CPU a los procesos en la cola 
    de procesos listos en ciclos de quantum hasta que todos los procesos se completen.

    El Round Robin garantiza que ningún proceso tenga un monopolio prolongado del CPU, 
    lo que permite una ejecución justa y evita que un proceso acapare recursos durante mucho tiempo.

En resumen, el algoritmo Round Robin con un quantum de 3 asigna el CPU a cada proceso 
por un tiempo limitado antes de pasar al siguiente proceso en la cola, 
repitiendo este ciclo hasta que todos los procesos se completen.
'''
