Código Comentado
python
Copiar código
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
Explicación Paso a Paso
Definición de Clases:

Tarea: Clase base con atributos nombre, descripcion, y prioridad.
TareaGeneral: Hereda de Tarea y no añade nuevos atributos.
TareaConFecha: Hereda de Tarea y añade un atributo fecha.
Clase ListaDeTareas:

Maneja una lista de tareas (tareas) y un identificador único (id_actual) para cada tarea.
agregar_tarea: Asigna un ID único a cada tarea antes de agregarla a la lista.
eliminar_tarea: Elimina una tarea basada en su ID.
listar_tareas: Imprime todas las tareas con sus detalles e ID.
Funciones Auxiliares:

mostrar_menu: Muestra las opciones disponibles para el usuario.
obtener_fecha: Solicita y valida una fecha en formato YYYY-MM-DD.
Función main:

Controla el flujo del programa.
Muestra el menú y solicita una opción al usuario.
Permite agregar una nueva tarea solicitando detalles como el nombre, descripción, prioridad y tipo de tarea (General o ConFecha). Si es ConFecha, también solicita la fecha.
Permite eliminar una tarea existente mostrando la lista de tareas con sus IDs y solicitando el ID de la tarea a eliminar.
Permite listar todas las tareas con sus detalles e ID.
Permite salir del programa.
Este programa ahora almacena las tareas con un ID único, lo que facilita la eliminación de tareas al usar este ID en lugar del nombre. También está comentado y estructurado para que sea fácil de entender y mantener.




te hago una consulta, el programa utiliza poo?

ChatGPT
Sí, el programa utiliza Programación Orientada a Objetos (POO). A continuación, te explico cómo se implementa la POO en el programa:

Clases y Objetos: La base de la POO son las clases y los objetos. En este programa, las clases Tarea, TareaGeneral, TareaConFecha, y ListaDeTareas son definiciones de objetos con atributos y métodos.

Herencia:

La clase TareaGeneral hereda de la clase Tarea.
La clase TareaConFecha hereda de la clase Tarea.
La herencia permite que TareaGeneral y TareaConFecha reutilicen y extiendan el comportamiento de Tarea.
Encapsulamiento:

Los atributos y métodos de las clases están encapsulados dentro de las clases. Por ejemplo, los atributos nombre, descripcion, prioridad y fecha están encapsulados dentro de sus respectivas clases.
Los métodos de las clases (como get_detalle) son formas de interactuar con los datos encapsulados.
Polimorfismo:

Aunque no se muestra explícitamente en este código, el polimorfismo se manifiesta cuando diferentes clases heredan de una clase base y pueden ser tratadas como instancias de la clase base. En este caso, TareaGeneral y TareaConFecha pueden ser tratadas como Tarea.
Aquí está el código nuevamente con comentarios que subrayan el uso de POO:

python
Copiar código
from datetime import datetime

# Clase base para todas las tareas.
class Tarea:
    def __init__(self, nombre, descripcion, prioridad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __str__(self):
        return f"Nombre: {self.nombre}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}"
    
    def get_detalle(self):
        return str(self)

# Clase para tareas generales, hereda de Tarea.
class TareaGeneral(Tarea):
    def __init__(self, nombre, descripcion, prioridad):
        super().__init__(nombre, descripcion, prioridad)

# Clase para tareas con fecha, hereda de Tarea y añade una fecha.
class TareaConFecha(Tarea):
    def __init__(self, nombre, descripcion, prioridad, fecha):
        super().__init__(nombre, descripcion, prioridad)
        self.fecha = fecha

    def __str__(self):
        return super().__str__() + f", Fecha: {self.fecha.strftime('%Y-%m-%d')}"
    
    def get_detalle(self):
        return str(self)

# Clase que administra una lista de tareas.
class ListaDeTareas:
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
Explicación Detallada
Clases y Objetos:

class Tarea: Clase base con el constructor __init__ que inicializa los atributos nombre, descripcion, y prioridad. También tiene un método __str__ para representar la tarea como una cadena y un método get_detalle que devuelve esa representación.
class TareaGeneral(Tarea): Hereda de Tarea sin agregar nuevos atributos o métodos.
class TareaConFecha(Tarea): Hereda de Tarea y añade el atributo fecha. Sobrescribe el método __str__ para incluir la fecha en la representación de la tarea.
Encapsulamiento:

Los atributos (nombre, descripcion, prioridad, fecha) están encapsulados dentro de las clases y sólo pueden ser accedidos a través de métodos de la clase.
Herencia:

TareaGeneral y TareaConFecha heredan de Tarea, reutilizando y extendiendo su funcionalidad.
Polimorfismo:

Los métodos como __str__ y get_detalle son polimórficos. Aunque diferentes clases pueden tener su propia implementación, se pueden llamar de la misma manera a través de objetos de tipo Tarea.
Interacción con el Usuario:

La función mostrar_menu muestra las opciones disponibles.
La función obtener_fecha solicita y valida una fecha.
La función main controla el flujo del programa, permitiendo agregar, eliminar y listar tareas a través de un bucle interactivo.
Este programa utiliza conceptos fundamentales de la POO, como clases, objetos, herencia y encapsulamiento, para manejar una lista de tareas de manera estructurada y modular.

ahora puedes explicarme el codigo paso a paso para una exposicion oral que tengo que hacer, asumiendo que tengo unos conocimientos muy basicos de programacion

ChatGPT
Claro, te explicaré el código paso a paso de manera que puedas entenderlo bien para tu exposición.

Paso 1: Importar el Módulo datetime
python
Copiar código
from datetime import datetime
Qué hace: Importa la clase datetime del módulo datetime para trabajar con fechas.
Por qué: Necesitamos manejar fechas para las tareas que tienen una fecha asignada.
Paso 2: Definir la Clase Tarea
python
Copiar código
class Tarea:
    def __init__(self, nombre, descripcion, prioridad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __str__(self):
        return f"Nombre: {self.nombre}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}"
    
    def get_detalle(self):
        return str(self)
Qué hace: Define la clase Tarea, que es la clase base para todas las tareas.
Atributos:
nombre: El nombre de la tarea.
descripcion: La descripción de la tarea.
prioridad: La prioridad de la tarea (Alta, Media, Baja).
Métodos:
__init__: Constructor que inicializa los atributos de la tarea.
__str__: Devuelve una cadena con los detalles de la tarea.
get_detalle: Devuelve la representación en cadena de la tarea.
Paso 3: Definir la Clase TareaGeneral
python
Copiar código
class TareaGeneral(Tarea):
    def __init__(self, nombre, descripcion, prioridad):
        super().__init__(nombre, descripcion, prioridad)
Qué hace: Define la clase TareaGeneral, que hereda de Tarea.
Por qué: Es una tarea común sin fecha específica, reutiliza los atributos y métodos de Tarea.
Paso 4: Definir la Clase TareaConFecha
python
Copiar código
class TareaConFecha(Tarea):
    def __init__(self, nombre, descripcion, prioridad, fecha):
        super().__init__(nombre, descripcion, prioridad)
        self.fecha = fecha

    def __str__(self):
        return super().__str__() + f", Fecha: {self.fecha.strftime('%Y-%m-%d')}"
    
    def get_detalle(self):
        return str(self)
Qué hace: Define la clase TareaConFecha, que hereda de Tarea y añade el atributo fecha.
Atributo:
fecha: La fecha asociada con la tarea.
Métodos:
__str__: Sobrescribe el método para incluir la fecha en la cadena.
get_detalle: Devuelve la representación en cadena de la tarea incluyendo la fecha.
Paso 5: Definir la Clase ListaDeTareas
python
Copiar código
class ListaDeTareas:
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
Qué hace: Define la clase ListaDeTareas, que maneja una lista de tareas.
Atributos:
tareas: Una lista para almacenar las tareas.
id_actual: Un contador para asignar IDs únicos a las tareas.
Métodos:
agregar_tarea: Añade una tarea a la lista y le asigna un ID único.
eliminar_tarea: Elimina una tarea de la lista por su ID.
listar_tareas: Imprime todas las tareas con sus detalles y IDs.
Paso 6: Funciones Auxiliares
python
Copiar código
def mostrar_menu():
    print("\nOpciones:")
    print("1. Agregar una nueva tarea")
    print("2. Eliminar una tarea")
    print("3. Listar todas las tareas")
    print("4. Salir")
Qué hace: Muestra el menú de opciones para el usuario.
Por qué: Facilita la interacción con el usuario.
python
Copiar código
def obtener_fecha():
    while True:
        fecha_str = input("Ingrese la fecha (YYYY-MM-DD): ")
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            return fecha
        except ValueError:
            print("Formato de fecha incorrecto. Inténtelo de nuevo.")
Qué hace: Solicita una fecha al usuario y la valida.
Por qué: Asegura que la fecha ingresada sea válida.
Paso 7: Función Principal main
python
Copiar código
def main():
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
Qué hace: Controla el flujo del programa interactivo.
Pasos:
Inicializa una instancia de ListaDeTareas.
Bucle Infinito: Permite al usuario interactuar continuamente hasta que elija salir.
Opciones:
Agregar Tarea: Solicita detalles y tipo de tarea, luego la añade a la lista.
Eliminar Tarea: Muestra las tareas con sus IDs y solicita el ID para eliminar.
Listar Tareas: Imprime todas las tareas con sus detalles.
Salir: Rompe el bucle y finaliza el programa.
Explicación General
Clases y Objetos: Utilizamos clases para definir diferentes tipos de tareas. Cada tarea tiene atributos y métodos.
Herencia: TareaGeneral y TareaConFecha heredan de Tarea, reutilizando su estructura y comportamiento.
Encapsulamiento: Los datos (atributos) están encapsulados dentro de las clases y sólo se acceden mediante métodos.
Interacción con el Usuario: La función main gestiona la interacción con el usuario, permitiendo agregar, eliminar y listar tareas de manera intuitiva.
Espero que esta explicación te sea útil para tu exposición. ¡Buena suerte!
