class Appointment():

    def __init__(self, nombre, cedula, edad, ciudad):
        self.nombre = nombre
        self.cedula = int(cedula)
        self.edad = int(edad)
        self.ciudad = str(ciudad)

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Cedula: {self.cedula}, Edad: {self.edad}, Cuidad: {self.ciudad}')

    def get_cedula(self):
        return self.cedula
    
    def set_cedula(self, cedula):
        self.cedula = cedula

# appointment = Appointment('David', 123456789, 28, 'Medellin', 'sura')
# appointment.set_cedula(12345)
# appointment.get_cedula()

class Agendar(Appointment):
    def __init__(self, nombre, cedula, edad, ciudad, eps):
        super().__init__(nombre, cedula, edad, ciudad)
        self.eps = eps

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Cedula: {self.cedula}, Edad: {self.edad}, Cuidad: {self.ciudad}, EPS: {self.eps}')

    def get_eps(self):
        return self.eps

    def set_eps(self, eps):
        self.get_eps = eps

    # def app():
    #     ## se crea el archivo.
    #     orden = open('orden.txt', 'w') # Es un archivo de escritura
    #     for i in range(0, 10):
    #         orden.write('Esta es la linea' + str(i) + '\r\n')

    #     orden.close()
    # app()
    def remenber():
        with open('remenber.txt') as archivo:
            for conten in archivo:
                print(conten.strip())
    remenber()

agendar = Agendar('David', 123456789, 28, 'Medellin', 'SI')
agendar.mostrar_informacion()
eps = agendar.get_eps()
print(eps)