from datetime import datetime
class Calculadora_edad:
    fecha_actual = datetime.now().date()
    fecha_usuario = []
    def __init__(self) :
        pass
    def calcular_year_bisiesto (self,year):
        dias = 0
        if (year & 4 == 0):
            if (year & 100 == 0 and year & 400 == 0):
                dias = 366
        else:
            dias = 365
        return dias
    def calcular_dias (self):
        if (self.fecha_usuario[1] == self.fecha_actual.month):
            if (self.fecha_usuario[2] < self.fecha_actual.day):
                
    def detector_dias_mes (self,mes):
        mes = mes.lower()
        dias = 0
        if (mes == "enero" or mes == 1):
            dias = 31
            return dias
        if (mes == "febrero" or mes == 2):
            year_bisiesto = self.calc.ular_year_bisiesto(self.fecha_usuario[0])
            if (year_bisiesto == 366):
                dias = 29
                return dias
            else:
                dias = 28
                return dias
        if (mes == "marzo" or mes == 3):
            dias = 31
            return dias
        if (mes == "abril" or mes == 4):
            dias = 31
            return dias
        if (mes == "mayo" or mes == 5):
            dias = 31
            return dias
        if (mes == "junio" or mes == 6):
            dias = 30
            return dias
        if (mes == "julio" or mes == 7):
            dias = 31
            return dias
        if (mes == "agosto" or mes == 8):
            dias = 31
            return dias
        if (mes == "septiembre" or mes == 9):
            dias = 30
            return dias
        if (mes == "octubre" or mes == 10):
            dias = 31
            return dias
        if (mes == "noviembre" or mes == 11):
            dias = 30
            return dias
        if (mes == "diciembre" or mes == 12):
            dias = 31
            return dias
    def detector_mes (self,mes):
        if (mes == "enero"):
            dias = 1
            return dias
        if (mes == "febrero"):
            dias = 2
        if (mes == "marzo"):
            dias = 3
            return dias
        if (mes == "abril" ):
            dias = 4
            return dias
        if (mes == "mayo" ):
            dias = 5
            return dias
        if (mes == "junio" ):
            dias = 6
            return dias
        if (mes == "julio" ):
            dias = 7
            return dias
        if (mes == "agosto"):
            dias = 8
            return dias
        if (mes == "septiembre" ):
            dias = 9
            return dias
        if (mes == "octubre" ):
            dias = 10
            return dias
        if (mes == "noviembre" ):
            dias = 11
            return dias
        if (mes == "diciembre" ):
            dias = 12
            return dias