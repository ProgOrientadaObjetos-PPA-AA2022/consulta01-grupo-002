class doctores:
    def __init__(self):
        self.nombre=None
        self.antiguedad=None
        self.cualificacion=None
        self.CI=None

    def sueldo(self):
        return (1000 + self.antiguedad * 25 + self.cualificacion*100)

def main():
        doctores_1 = doctores()
        doctores_1.nombre = "Josue"
        doctores_1.antiguedad = 6
        doctores_1.cualificacion = 3
        print(doctores_1)
        print("El medico",doctores_1.nombre,"lleva trabajando",doctores_1.antiguedad,
              "años en el hospital con un sueldo de",doctores_1.sueldo(),
              "dolares y se encuentra entre los" ,doctores_1.cualificacion, "mejores medicos del hospital")
main()