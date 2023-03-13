class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

estudiante1 = Estudiante("Virgilio")
estudiante2 = Estudiante("Margarita")

class Vir(Estudiante):
    pass
    def estudiante():
        return'{} es un estudiante de Ingenieria en Desarrollo de Software'.format(estudiante1.nombre)

class Mar(Estudiante):
    pass
    def estudiante():
        return'{} es una estudiante de Ingenieria en Desarrollo de Software'.format(estudiante2.nombre)
    
virgi = Vir
margu = Mar
print(virgi.estudiante())
print(margu.estudiante())