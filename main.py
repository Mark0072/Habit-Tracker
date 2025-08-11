import random

class Puntos:
    def __init__(self):
        self.total = 0

    def agregar_puntos(self):
        puntos = random.randint(100, 500)
        self.total += puntos
        return puntos

    def gastar_puntos(self, cantidad):
        if self.total >= cantidad:
            self.total -= cantidad
            return True
        return False

    def obtener_puntos(self):
        return self.total


class Recompensa:
    def __init__(self):
        self.recompensas = []
        self.proximo_id = 1

    def agregar_recompensa(self, nombre, costo):
        recompensa = {
            'id': self.proximo_id,
            'nombre': nombre,
            'costo': costo
        }
        self.recompensas.append(recompensa)
        self.proximo_id += 1
        print(f"Recompensa '{nombre}' agregada con un costo de {costo} puntos.")

    def mostrar_recompensas(self):
        if not self.recompensas:
            print("No hay recompensas disponibles.")
            return
        print("\n🎁 Recompensas disponibles:")
        for r in self.recompensas:
            print(f"ID: {r['id']} | Nombre: {r['nombre']} | Costo: {r['costo']} puntos")

    def canjear(self, recompensa_id, puntos: Puntos):
        for r in self.recompensas:
            if r['id'] == recompensa_id:
                if puntos.gastar_puntos(r['costo']):
                    print(f"✅ Has canjeado la recompensa: {r['nombre']}")
                else:
                    print("❌ No tienes suficientes puntos.")
                return
        print("Recompensa no encontrada.")


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitos = []
        self.recompensas = Recompensa()
        self.puntos = Puntos()
        self.proximo_id = 1

    def agregar_habito(self, nombre, frecuencia):
        habito = {
            'id': self.proximo_id,
            'nombre': nombre,
            'frecuencia': frecuencia,
            'completado': False
        }
        self.habitos.append(habito)
        self.proximo_id += 1
        print(f"Hábito '{nombre}' agregado.")

    def eliminar_habito(self, habito_id):
        for h in self.habitos:
            if h['id'] == habito_id:
                self.habitos.remove(h)
                print(f"Hábito con ID {habito_id} eliminado.")
                return
        print("Hábito no encontrado.")

    def editar_habito(self, habito_id, nuevo_nombre, nueva_frecuencia):
        for h in self.habitos:
            if h['id'] == habito_id:
                h['nombre'] = nuevo_nombre
                h['frecuencia'] = nueva_frecuencia
                print(f"Hábito con ID {habito_id} actualizado.")
                return
        print("Hábito no encontrado.")

    def completar_habito(self, habito_id):
        for h in self.habitos:
            if h['id'] == habito_id:
                if h['completado']:
                    print("Este hábito ya fue completado.")
                    return
                h['completado'] = True
                puntos_ganados = self.puntos.agregar_puntos()
                print(f"Hábito con ID {habito_id} marcado como completado.")
                print(f"¡Ganaste {puntos_ganados} puntos!")
                return
        print("Hábito no encontrado.")

    def mostrar_habitos(self):
        if not self.habitos:
            print("No tienes hábitos registrados.")
            return
        print(f"\nHábitos de {self.nombre}:")
        for h in self.habitos:
            estado = "Sí" if h['completado'] else "No"
            print(f"ID: {h['id']} | Nombre: {h['nombre']} | Frecuencia: {h['frecuencia']} | Completado: {estado}")
        print(f"\n🎯 Puntos totales: {self.puntos.obtener_puntos()}")


# Interfaz de consola
def main():
    nombre = input("Ingresa tu nombre: ")
    persona = Persona(nombre)

    while True:
        print("\n--- Habit Tracker ---")
        print("1. Ver hábitos")
        print("2. Agregar hábito")
        print("3. Eliminar hábito")
        print("4. Editar hábito")
        print("5. Marcar hábito como completado")
        print("6. Ver recompensas")
        print("7. Agregar recompensa")
        print("8. Canjear recompensa")
        print("9. Salir")
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
            persona.recompensas.mostrar_recompensas()
        elif opcion == '7':
            nombre_recompensa = input("Nombre de la recompensa: ")
            costo = int(input("Costo en puntos: "))
            persona.recompensas.agregar_recompensa(nombre_recompensa, costo)
        elif opcion == '8':
            persona.recompensas.mostrar_recompensas()
            recompensa_id = int(input("ID de la recompensa a canjear: "))
            persona.recompensas.canjear(recompensa_id, persona.puntos)
        elif opcion == '9':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()
