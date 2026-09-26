import json
from pathlib import Path

from models import Usuario, Habito

DATA_FILE = Path(__file__).parent / "data" / "usuarios.json"

def guardar_usuarios(usuarios):
    "Convierte los objetos a diccionario y los escribe en JSON"
    
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    data = {}

    for user_id, usuario in usuarios.items():
        data[user_id] = {
            "nombre": usuario.nombre,
            "habitos": {
                nombre: {
                    "creado": habito.creado,
                    "checks": habito.checks
                }
                for nombre, habito in usuario.habitos.items()
            },
        }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def cargar_usuario():
    """Lee el JSON y reconstruye los ojetos Usuario y Habito"""

    # Si el archivo no existe (primera ejecución), retornamos {} vacio
    if not DATA_FILE.exists():
        return {}

    # Comprobacion del estado del archivo
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Aviso: el archivo de datos está corrupto. Empezando desde cero.")
        return {}

    usuarios = {}

    for usaer_id, info in data.items():
        usuario = Usuario(
            usaer_id = usaer_id,
            nombre = info.get("nombre", "Anonimo")
        )

        for nombre_habito, habito_data in info.get("habitos", {}).items():
            habito = Habito(nombre_habito)

            habito.creado = habito_data["creado"]
            habito.checks = habito_data["checks"]

            usuario.habitos[nombre_habito] = habito
        
        usuarios[usaer_id] = usuario
    
    return usuario