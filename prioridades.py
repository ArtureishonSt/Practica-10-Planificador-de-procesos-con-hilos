import time


# Función para simular la ejecución de un proceso
def ejecutar_proceso(nombre, tiempo):
    print(f"Ejecutando proceso: {nombre} - Tiempo restante: {tiempo}")
    time.sleep(1)  # Simula la ejecución del proceso durante 1 segundo


# Función para administrar procesos con prioridades
def administrar_procesos_prioridades():
    # Leer datos del archivo "procesos.txt" y crear una lista de procesos
    procesos = []
    with open("procesos.txt", "r") as archivo:
        for linea in archivo:
            nombre, tiempo, prioridad = linea.strip().split(", ")
            procesos.append((nombre, int(tiempo), int(prioridad)))

    # Ordenar la lista de procesos por prioridad (de mayor a menor)
    procesos.sort(key=lambda x: x[2], reverse=True)

    # Simular la ejecución de los procesos
    for proceso in procesos:
        nombre, tiempo, prioridad = proceso
        print(f"Iniciando proceso: {nombre} - Tiempo estimado: {tiempo} - Prioridad: {prioridad}")
        while tiempo > 0:
            ejecutar_proceso(nombre, tiempo)
            tiempo -= 1
        print(f"Proceso {nombre} terminado")

    print("Todos los procesos han terminado.")


'''
# Funciónamiento 
Este programa de Python lee datos de un archivo llamado "procesos.txt" 
que contiene información sobre procesos, incluyendo 
su nombre, tiempo de ejecución y prioridad. 
Luego, ordena estos procesos en función de su prioridad (de mayor a menor) 
y simula su ejecución uno por uno, mostrando información sobre el proceso en curso, 
su tiempo restante y su prioridad. 
El programa utiliza la función time.sleep(1) 
para simular la ejecución de cada proceso durante 1 segundo 
antes de pasar al siguiente proceso. 
Una vez que todos los procesos han terminado, 
muestra un mensaje indicando que todos los procesos se han completado.
'''
