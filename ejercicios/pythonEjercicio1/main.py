class Vehiculo:

    def __init__(self, marca=None, modelo="CBR"):
        self.marca = marca
        self.modelo = modelo
        self.color="Azul"
        self.anio=2020

moto = Vehiculo("Toyota","GXS")
print(moto.marca,moto.modelo,moto.color,moto.anio)




