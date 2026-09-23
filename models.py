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