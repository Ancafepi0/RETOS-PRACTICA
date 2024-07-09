class Usuario:
    dias_faltantes = 0
    nombre = 'None'
    def __init__(self) :
        pass
    def get_dias_faltantes (self):
        dias = self.dias_faltantes
        return dias
    def get_nombre (self):
        nombre = self.nombre
        return nombre
    def set_dias_faltantes (self,dias):
        self.dias_faltantes = dias      
    def set_nombre (self,nombre):
        self.nombre = nombre
        