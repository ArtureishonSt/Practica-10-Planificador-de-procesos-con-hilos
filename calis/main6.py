import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
import threading
import queue
import fifo
import prioridades
import rr
import sjf


class Proceso:
    def __init__(self, nombre, tiempo_ejecucion, prioridad):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion
        self.prioridad = prioridad


class ConsoleRedirector:
    def __init__(self, callback):
        self.callback = callback
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self.redirect_output)
        self.thread.daemon = True
        self.thread.start()

    def write(self, message):
        self.queue.put(message)

    def flush(self):
        pass

    def redirect_output(self):
        while True:
            message = self.queue.get()
            if message is None:
                break
            self.callback(message)


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Planificador de Procesos")

        # Configuración del tamaño de la ventana principal
        self.root.geometry("700x600")  # Ancho x Altura

        # Variable para controlar el estado del hilo de procesos
        self.ejecucion_procesos = False

        self.crear_interfaz()
        self.redirector = ConsoleRedirector(self.mostrar_consola)

    def crear_interfaz(self):
        # Crear etiqueta de título
        titulo = tk.Label(self.root, text="Planificador de Procesos", font=("Helvetica", 16))
        titulo.grid(row=0, column=0, columnspan=3, pady=10)

        # Crear consola
        self.consola = tk.Text(self.root, height=10, width=50)
        self.consola.grid(row=1, column=0, columnspan=3, pady=10)

        # Crear Text para la salida de la consola
        self.salida_consola = tk.Text(self.root, height=10, width=80, state=tk.DISABLED)
        self.salida_consola.grid(row=2, column=0, columnspan=3, pady=10)

        # Crear botones
        btn_fifo = tk.Button(self.root, text="FIFO", command=self.ejecutar_fifo)
        btn_fifo.grid(row=3, column=0, padx=10, pady=5)

        btn_prioridades = tk.Button(self.root, text="Prioridades", command=self.ejecutar_prioridades)
        btn_prioridades.grid(row=3, column=1, padx=10, pady=5)

        btn_rr = tk.Button(self.root, text="Round Robin", command=self.ejecutar_rr)
        btn_rr.grid(row=4, column=0, padx=10, pady=5)

        btn_sjf = tk.Button(self.root, text="SJF", command=self.ejecutar_sjf)
        btn_sjf.grid(row=4, column=1, padx=10, pady=5)

        btn_agregar_proceso = tk.Button(self.root, text="Agregar Proceso", command=self.agregar_proceso)
        btn_agregar_proceso.grid(row=5, column=0, columnspan=2, pady=10)

        btn_salir = tk.Button(self.root, text="Salir", command=self.salir_programa)
        btn_salir.grid(row=5, column=2, pady=10)

    def mostrar_consola(self, mensaje, update_superior=True):
        # Agregamos el mensaje a la ventana inferior (salida_consola)
        self.salida_consola.config(state=tk.NORMAL)  # Habilitar edición
        self.salida_consola.insert(tk.END, mensaje + "\n")
        self.salida_consola.see(tk.END)
        self.salida_consola.config(state=tk.DISABLED)  # Deshabilitar edición

        # Actualizamos la ventana superior solo si update_superior es True
        if update_superior:
            self.consola.config(state=tk.NORMAL)
            self.consola.delete("1.0", tk.END)  # Limpiamos el contenido existente
            self.consola.insert(tk.END, mensaje)
            self.consola.config(state=tk.DISABLED)  # Deshabilitar edición

    def ejecutar_fifo(self):
        archivo = "procesos.txt"
        self.mostrar_consola("Ejecutando FIFO:")
        fifo.simulacion_FIFO(archivo)

    def ejecutar_prioridades(self):
        self.mostrar_consola("Ejecutando Prioridades:")
        self.ejecucion_procesos = True
        threading.Thread(target=self._ejecutar_prioridades).start()

    def _ejecutar_prioridades(self):
        try:
            prioridades.administrar_procesos_prioridades()
        except Exception as e:
            self.mostrar_consola(f"Error: {e}")
        finally:
            self.ejecucion_procesos = False

    def ejecutar_rr(self):
        nombre_archivo = "procesos.txt"
        procesos = rr.cargar_procesos(nombre_archivo)
        self.mostrar_consola("Ejecutando Round Robin:")
        rr.round_robin(procesos)

    def ejecutar_sjf(self):
        procesos = sjf.leer_procesos()
        self.mostrar_consola("Ejecutando SJF:")
        sjf.ejecutar_sjf(procesos)

    def agregar_proceso(self):
        nombre = simpledialog.askstring("Agregar Proceso", "Ingrese el nombre del proceso:")
        tiempo = simpledialog.askinteger("Agregar Proceso", "Ingrese el tiempo de ejecución:")
        prioridad = simpledialog.askinteger("Agregar Proceso", "Ingrese la prioridad:")

        if nombre is not None and tiempo is not None and prioridad is not None:
            with open("procesos.txt", "a") as archivo:
                archivo.write(f"{nombre}, {tiempo}, {prioridad}\n")
            messagebox.showinfo("Proceso Agregado", "El proceso se ha agregado correctamente.")
        else:
            messagebox.showwarning("Error", "Debe ingresar valores válidos para el proceso.")

    def salir_programa(self):
        if self.ejecucion_procesos:
            self.mostrar_consola("Deteniendo procesos...")
            # Aquí deberías tener algún mecanismo para detener los procesos en ejecución.
            # Puedes utilizar una variable compartida o algún otro mecanismo de comunicación.
            # Aquí simplemente marcamos la variable para indicar que no debe ejecutar más procesos.
            self.ejecucion_procesos = False

        self.root.destroy()
        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    sys.stdout = app.redirector  # Redirigir la salida estándar a la nueva ventana
    root.mainloop()
    sys.stdout = sys.__stdout__  # Restaurar la salida estándar al valor predeterminado
