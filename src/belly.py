class Belly:
    def __init__(self):
        self.pepinos_comidos = 0.0
        self.tiempo_esperado = 0.0

    def comer(self, pepinos):
        if pepinos < 0:
            raise ValueError("No es posible comer una cantidad negativa de pepinos")
        self.pepinos_comidos += float(pepinos)

    def esperar(self, tiempo_en_horas):
        self.tiempo_esperado += float(tiempo_en_horas)

    def esta_gruñendo(self):
        # El estómago gruñe si ha esperado al menos 1.5 horas y ha comido más de 10 pepinos
        return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10
