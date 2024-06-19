from datetime import datetime

class Tarea:
    """Clase base para todas las tareas."""
    def __init__(self, nombre, descripcion, prioridad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __str__(self):
        return f"Nombre: {self.nombre}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}"
    
    def get_detalle(self):
        return str(self)

class TareaGeneral(Tarea):
    """Clase para tareas generales, hereda de Tarea."""
    def __init__(self, nombre, descripcion, prioridad):
        super().__init__(nombre, descripcion, prioridad)

class TareaConFecha(Tarea):
    """Clase para tareas con fecha, hereda de Tarea y añade una fecha."""
    def __init__(self, nombre, descripcion, prioridad, fecha):
        super().__init__(nombre, descripcion, prioridad)
        self.fecha = fecha

    def __str__(self):
        return super().__str__() + f", Fecha: {self.fecha.strftime('%Y-%m-%d')}"
    
    def get_detalle(self):
        return str(self)

class ListaDeTareas:
    """Clase que administra una lista de tareas."""
    def __init__(self):
        self.tareas = []
        self.id_actual = 1  # Identificador único para cada tarea

    def agregar_tarea(self, tarea):
        tarea.id = self.id_actual  # Asignar un identificador único a la tarea
        self.tareas.append(tarea)
        self.id_actual += 1

    def eliminar_tarea(self, id_tarea):
        self.tareas = [tarea for tarea in self.tareas if tarea.id != id_tarea]

    def listar_tareas(self):
        for tarea in self.tareas:
            print(f"ID: {tarea.id} - {tarea.get_detalle()}")

def mostrar_menu():
    """Función para mostrar el menú de opciones."""
    print("\nOpciones:")
    print("1. Agregar una nueva tarea")
    print("2. Eliminar una tarea")
    print("3. Listar todas las tareas")
    print("4. Salir")

def obtener_fecha():
    """Función para solicitar y validar una fecha al usuario."""
    while True:
        fecha_str = input("Ingrese la fecha (YYYY-MM-DD): ")
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            return fecha
        except ValueError:
            print("Formato de fecha incorrecto. Inténtelo de nuevo.")

def main():
    """Función principal que controla el flujo del programa."""
    lista_de_tareas = ListaDeTareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar una nueva tarea
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            prioridad = input("Prioridad (Alta, Media, Baja): ").capitalize()
            
            tipo_tarea = input("Tipo de tarea (General, ConFecha): ").capitalize()
            if tipo_tarea == "General":
                tarea = TareaGeneral(nombre, descripcion, prioridad)
            elif tipo_tarea == "Confecha":
                fecha = obtener_fecha()
                tarea = TareaConFecha(nombre, descripcion, prioridad, fecha)
            else:
                print("Tipo de tarea no válido.")
                continue

            lista_de_tareas.agregar_tarea(tarea)
            print("Tarea agregada con éxito.")
        
        elif opcion == "2":
            # Eliminar una tarea por ID
            lista_de_tareas.listar_tareas()
            try:
                id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
                lista_de_tareas.eliminar_tarea(id_tarea)
                print("Tarea eliminada con éxito.")
            except ValueError:
                print("ID no válido. Inténtelo de nuevo.")

        elif opcion == "3":
            # Listar todas las tareas
            print("Lista de tareas:")
            lista_de_tareas.listar_tareas()
        
        elif opcion == "4":
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
