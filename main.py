class Persona:
    def __init__(self, nombre, db):
        self.nombre = nombre
        self.db = db

    def agregar_habito(self, nombre, frecuencia):
        self.db.agregar_habito(self.nombre, nombre, frecuencia)
        print(f"Hábito '{nombre}' agregado.")

    def eliminar_habito(self, habito_id):
        self.db.eliminar_habito(habito_id)
        print(f"Hábito con ID {habito_id} eliminado.")

    def editar_habito(self, habito_id, nuevo_nombre, nueva_frecuencia):
        self.db.editar_habito(habito_id, nuevo_nombre, nueva_frecuencia)
        print(f"Hábito con ID {habito_id} actualizado.")

    def completar_habito(self, habito_id):
        self.db.completar_habito(habito_id)
        print(f"Hábito con ID {habito_id} marcado como completado hoy.")

    def mostrar_habitos(self):
        habitos = self.db.obtener_habitos(self.nombre)
        if not habitos:
            print("No tienes hábitos registrados.")
            return
        print(f"\nHábitos de {self.nombre}:")
        for h in habitos:
            print(f"ID: {h[0]} | Nombre: {h[2]} | Frecuencia: {h[3]} | Completado: {h[4]}")


#  Interfaz de consola
def main():
    db = HabitTrackerDB()
    nombre = input("Ingresa tu nombre: ")
    persona = Persona(nombre, db)

    while True:
        print("\n--- Habit Tracker ---")
        print("1. Ver hábitos")
        print("2. Agregar hábito")
        print("3. Eliminar hábito")
        print("4. Editar hábito")
        print("5. Marcar hábito como completado")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            persona.mostrar_habitos()
        elif opcion == '2':
            nombre_habito = input("Nombre del hábito: ")
            frecuencia = input("Frecuencia (diaria/semanal): ")
            persona.agregar_habito(nombre_habito, frecuencia)
        elif opcion == '3':
            habito_id = int(input("ID del hábito a eliminar: "))
            persona.eliminar_habito(habito_id)
        elif opcion == '4':
            habito_id = int(input("ID del hábito a editar: "))
            nuevo_nombre = input("Nuevo nombre del hábito: ")
            nueva_frecuencia = input("Nueva frecuencia: ")
            persona.editar_habito(habito_id, nuevo_nombre, nueva_frecuencia)
        elif opcion == '5':
            habito_id = int(input("ID del hábito a completar: "))
            persona.completar_habito(habito_id)
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()