class Proceso:
    def __init__(self, nombre, tiempo_ejecucion, prioridad):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.prioridad = prioridad


def simulacion_FIFO(archivo):
    cola_procesos = []
    with open(archivo, 'r') as f:
        for linea in f:
            datos = linea.strip().split(', ')
            nombre = datos[0]
            tiempo_ejecucion = int(datos[1])
            prioridad = int(datos[2])
            proceso = Proceso(nombre, tiempo_ejecucion, prioridad)
            cola_procesos.append(proceso)

    tiempo_total = 0
    while cola_procesos:
        proceso_actual = cola_procesos.pop(0)
        tiempo_total += proceso_actual.tiempo_ejecucion
        print(
            f"Proceso: {proceso_actual.nombre}, Tiempo de Ejecución: {proceso_actual.tiempo_ejecucion}, Prioridad: {proceso_actual.prioridad}")

    print(f"Tiempo total de ejecución: {tiempo_total}")


'''
El algoritmo FIFO (First-In, First-Out) funciona de la siguiente manera:

    Los procesos son encolados en una cola (queue) en el orden en que llegan, es decir, 
    el primero en llegar es el primero en ser atendido.

    Cuando el sistema operativo necesita elegir un proceso para ejecutar, 
    selecciona el proceso que está en el frente de la cola, que es el proceso que ha estado esperando por más tiempo.

    Una vez que el proceso en el frente de la cola ha sido ejecutado durante un período de tiempo, 
    se elimina de la cola y se da paso al siguiente proceso en la cola.

Este enfoque asegura que los procesos se ejecuten en el orden en que llegaron, 
sin considerar sus características de prioridad o tiempo de ejecución. 
Es simple de implementar pero puede no ser la opción más eficiente en términos 
de utilización de recursos o tiempos de respuesta, especialmente en situaciones 
en las que algunos procesos son muy largos y otros son muy cortos.
'''
