from datetime import date, timedelta

class Habito:
    """Representa un habito que el usuario quiere trackear"""

    def __init__(self, nombre):
        self.nombre = nombre.lower().strip()
        self.creado = date.today().isoformat()
        self.checks = []

    def marcar_hoy(self):
        """Marca el hábito como hecho hoy. Retorna False si ya esta marcado"""
        hoy = date.today().isoformat()

        if hoy in self.checks:
            return False

        self.checks.append(hoy)
        return True

    def hecho_hoy(self):
        """Retorna True si el habito esta hecho hoy"""
        return date.today().isoformat() in self.checks

    def racha(self):
        """Calcula los días consecutivos hasta hoy"""
        
        if not self.checks:
            return 0

        fechas = sorted(
            [date.fromisoformat(fecha) for fecha in self.checks],
            reverse=True
        )

        hoy = date.today()
        ayer = hoy - timedelta(days=1)
        mas_reciente = fechas[0]

        if mas_reciente == hoy:
            esperando = hoy
        elif mas_reciente == ayer:
            esperando = ayer
        else:
            return 0

        racha = 0
        for fecha in fechas:
            if fecha == esperando:
                racha += 1
                esperando -= timedelta(days=1)
            else:
                break

        return racha
    

class Usuario:
    """Representa un usuario y la coleccion de hábitos que está trackeando"""

    def __init__(self, user_id, nombre="Anonimo"):
        self.user_id = user_id
        self.nombre = nombre
        self.habitos = dict()


    def agregar_habito(self, nombre):
        """Crear un nuevo hábito y lo agrega al usuario"""
        nombre_limpio = nombre.lower().strip()

        if not nombre_limpio:
            raise ValueError("El nombre del hábito no puede estar vacio")

        if nombre_limpio in self.habitos:
            raise ValueError(f"El hábito [{nombre_limpio}] ya existe")

        habito = Habito(nombre_limpio)

        self.habitos[nombre_limpio] = habito
        return habito


    def eliminar_habito(self, nombre):
        """Eliminar un hábito por nombre. Retorna True/False."""
        nombre_limpio = nombre.lower().strip()

        if nombre_limpio not in self.habitos: # Comprobacion de existencia
            return False

        del self.habitos[nombre_limpio]
        return True


    def marcar_habito(self, nombre):
        """marcar un h´qbito como hecho hoy. Retorna un mensaje."""
        nombre_limpio = nombre.lower().strip()

        if nombre_limpio not in self.habitos:
            raise KeyError(f"No tienes el habito [{nombre_limpio}]")

        habito = self.habitos[nombre_limpio]

        if habito.marcar_hoy():
            return (
                f"marcado [{nombre_limpio}].  "
                f"Racha actual: {habito.racha()} dias" 
            )

        return "Ya habias marcado ["+ nombre_limpio + "] el dia de hoy"