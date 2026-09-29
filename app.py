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
    print("5. Eliminar hábito")
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


