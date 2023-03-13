class Taxista:
    def __init__(self, nombre):
        self.nombre = nombre

conductor1 = Taxista("Rene")
conductor2 = Taxista("Virgilio")

class Rene(Taxista):
    pass
    def datosTaxista():
        return'{} es un taxista'.format(conductor1.nombre)
    
class Virgilio(Taxista):
    pass
    def datosTaxista():
        return'{} es un taxista'.format(conductor2.nombre)
    
motorista1 = Rene
motorista2 = Virgilio
print(motorista1.datosTaxista())
print(motorista2.datosTaxista())