import Num_dias
import Usuario
class Main:
    def __init__(self):
        pass
    def iniciar(self):
        print ("BIENVENIDO A JUNIX TU CALCULADORA DE CUMPLEAÑOS")
        respuesta = int(input(" DIGITE 1 PARA INICIAR EL PROGRAMA\nDIGITE 2 PARA CERRAR EL PROGRAMA"))
        while (respuesta == 1):
            un_usuario = Usuario.Usuario()
            year = int(input("DIGITE EL AÑO EN EL QUE NACIO"))
            mes = int(input("DIGITE EL MES EN EL QUE NACIO"))
            dia= int (input ("DIGITE EL DIA EN EL QUE NACIO"))
            fecha = [year,mes,dia]
            respuesta = int(input (" DIGITE 1 PARA INICIAR EL PROGRAMA\nDIGITE 2 PARA CERRAR EL PROGRAMA\n"))
cualquiera = Main()
cualquiera.iniciar()