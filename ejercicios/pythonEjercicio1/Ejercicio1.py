class Edades:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Edades("David", 12)
print(persona1.nombre)
print(persona1.edad)

persona2 = Edades("Juan", 8)
print(persona2.nombre)
print(persona2.edad)

if persona1.edad > persona2.edad:
    print(persona1.nombre + " es mayor")






