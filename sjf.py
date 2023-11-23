# Función para leer los datos del archivo "procesos.txt" y devolver una lista de procesos
def leer_procesos():
    procesos = []
    with open("procesos.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split(", ")
            proceso = {
                "nombre": datos[0],
                "tiempo_ejecucion": int(datos[1]),
                "prioridad": int(datos[2])
            }
            procesos.append(proceso)
    return procesos


# Función para ejecutar el algoritmo SJF
def ejecutar_sjf(procesos):  # Cambia el nombre de la función a ejecutar_sjf
    tiempo_total = 0
    proceso_actual = None

    while procesos:
        procesos.sort(key=lambda x: x["tiempo_ejecucion"])
        proceso_actual = procesos[0]
        del procesos[0]

        print(f"Ejecutando {proceso_actual['nombre']} (Tiempo restante: {proceso_actual['tiempo_ejecucion']})")

        tiempo_total += proceso_actual["tiempo_ejecucion"]
        proceso_actual["tiempo_ejecucion"] = 0

        for proceso in procesos:
            proceso["prioridad"] += 1

    print(f"Tiempo total de ejecución: {tiempo_total}")


'''
El algoritmo SJF (Shortest Job First), que significa "El trabajo más corto primero", 
es un algoritmo de planificación de procesos en sistemas operativos. Funciona de la siguiente manera:

    Cuando un proceso llega al sistema o se necesita elegir el próximo proceso a ejecutar, 
    el algoritmo SJF selecciona el proceso con el menor tiempo de ejecución pendiente (el proceso más corto).

    El proceso seleccionado se ejecuta hasta su finalización o hasta que ocurra una interrupción 
    (por ejemplo, si llega un proceso más corto).

    Una vez que el proceso actual se completa, el algoritmo SJF selecciona 
    el siguiente proceso más corto de entre los procesos pendientes.

    Este proceso de selección continúa hasta que se completen todos los procesos en la cola de ejecución.

El algoritmo SJF tiene como objetivo minimizar el tiempo promedio de espera de los procesos, 
lo que puede mejorar la eficiencia y reducir el tiempo total de ejecución en comparación 
con otros algoritmos de planificación. Sin embargo, puede ser sensible a la estimación precisa 
de los tiempos de ejecución y puede causar inanición si hay procesos largos esperando a procesos más cortos.

'''
