class Estudiante:
    nombre=""
    edad=0
    inst=""
    def __init__(self,nombre,edad,inst):
        self.nombre=nombre
        self.edad=edad
        self.inst=inst

    def univUno(self):
        print("El estudiante", self.nombre, "tiene una edad de" ,self.edad,
              "y estudio en el colegio",self.inst)

    def univDos(self):
        print("El estudiante", self.nombre, "tiene una edad de" ,self.edad,
              "y estudio en el colegio",self.inst)

persona=Estudiante("Miguel",18,"Tecnico")
personaDos=Estudiante("Daniel",19,"La Dolorosa")

persona.univUno()
personaDos.univDos()

