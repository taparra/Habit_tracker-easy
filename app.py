from models import Usuario, Habito
from storage import cargar_usuario, guardar_usuarios

USUARIO_LOCAL = "local"


def mostrar_menu():
    print("")
    print("=======================================")
    print("  HABIT TRACKER")
    print("=======================================")
    print("1. Agregar hábito")
    print("2. Marcar hábito hoy")
    print("3. Ver hábitos del dia")
    print("4. Ver streaks")
    print("5. Listar todos los hábitos")
    print("6. Eliminar hábito")
    print("0. Salir")
    print("")


def obtener_usuario(usuarios):
    """Si es la primera vez, pide el nombre y crea el usuario."""
    if USUARIO_LOCAL not in usuarios:
        nombre = input("Hola ¿Cómo te llamas? ").strip()

        if not nombre:
            nombre = "Anonimo"

        usuarios[USUARIO_LOCAL] = Usuario(USUARIO_LOCAL, nombre)

    return usuarios[USUARIO_LOCAL]


def comando_agregar(usuario):
    nombre = input("Nombre del hábito: ").strip()
    if not nombre:
        print("AVISO: El nombre no puede estar vacio")
        return

    try:
        usuario.agregar_habito(nombre)
        print(f"Hábito '{nombre.lower()}' creado correctamente")
    except ValueError as error:
        print(f"AVISO: {str(error)}")


def comando_marcar(usuario):
    if not usuario.habitos: # Comprobacion de habitos creados
        print(f"AVISO: No tienes hábitos. Agrega uno primero")
        return

    nombre = input("¿Qué habitó marcaste? ").strip()
    if not nombre:
        print("AVISO: nombre vacío")
        return

    try:
        mensaje = usuario.marcar_habito(nombre)
        print(mensaje)
    except KeyError as error:
        print(f"AVISO: {str(error)}")


def comando_hoy(usuario):
    if not usuario.habitos:
        print("No tienes hábitos registrados aún.")
        return

    print("")
    print(f"Hábitos de hoy ({usuario.nombre}):")

    for nombre, habito in usuario.habitos.items():
        if habito.hecho_hoy():
            estado = "[X]"
        else:
            estado = "[ ]"
        print(f"{estado} {nombre}")


def comando_rachas(usuario):
    if not usuario.habitos:
        print("No tienes hábitos registrados aún.")
        return

    print(" ")
    print("Rachas actuales: ")
    for nombre, habito in usuario.habitos.items():
        print(f" {nombre}: {str(habito.racha())} dias")


def comando_listar(usuario):
    if not usuario.habitos:
            print("No tienes hábitos registrados aún.")
            return

    print("")
    print("Todos tus hábitos:")
    for nombre, habito in usuario.habitos.items():
        total = len(habito.checks)
        print(
            f" - {nombre}" +
            f" (creado: {habito.creado}, "+
            f"total checks: {str(total)})"
        )

def comando_eliminar(usuario):
    if not usuario.habitos:
            print("No tienes hábitos registrados aún.")
            return

    nombre = input("¿Cuál eliminar? ").strip()

    if not nombre:
        print("Aviso: nombre vacio")
        return

    if usuario.eliminar_habito(nombre):
        print(f"Listo. Hábito '{nombre.lower()}' eliminado.")
    else:
        print("Aviso: No se encontró ese hábito.")


def main():
    usuarios = cargar_usuario()
    usuario = obtener_usuario(usuarios)

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        match opcion:
            case "1":
                comando_agregar(usuario)
            case "2":
                comando_marcar(usuario)
            case "3":
                comando_hoy(usuario)
            case "4":
                comando_rachas(usuario)
            case "5":
                comando_listar(usuario)
            case "6":
                comando_eliminar(usuario)
            case "0":
                guardar_usuarios(usuarios)
                print("Hasta mañana.")
                break
            case _:
                print("Aviso: opción invalida")

        guardar_usuarios(usuarios)


if __name__ == "__main__":
    main()