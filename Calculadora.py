
class Calculadora:
    def sumar(self,cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            return int(cadena[0])+int(cadena[1])
        else:
            return int(cadena)