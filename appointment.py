import os

CARPETA = 'Appointment/'
EXTENSION = '.txt'

class Appointmen():
    def __init__(self, identification, name, age, phone, barium, specialty):
        self.identification = identification
        self.name = name        
        self.age = age
        self.phone = phone
        self.barium = barium
        self.specialty = specialty

def Appointment():

    crar_carpeta()

    crear_menu()

    comfir = True
    while comfir:
        opcion = input('Eliga La Opcion Correcta: \r\n')
        opcion = int(opcion)
        if opcion == 1:
            add_appointment()
            comfir = False
        elif opcion == 2:
            view_appointment()
            comfir = False
        elif opcion ==3:
            search_appointment()
            comfir = False
        elif opcion == 4:
            update_appointment()
            comfir = False
        elif opcion == 5:
            delete_appointment()
            comfir = False
        elif opcion == 6:
            print('Salistes Del Programa!!!')
            break            
        else:
            print('No Entiendo Lo Que Quieres Hacer...!')  

def delete_appointment():
    print('Digite El Paciente A Eliminar: \r\n')
    identification_patient = input('Digita La Cedula Del Paciente: \r\n')

    try:
        os.remove(CARPETA + identification_patient + EXTENSION)
        print('Paciente Eliminado Exitosamente...')
    except:
        print('Paciente No Existe!!!')
    Appointment()

def update_appointment():
    identification_patient_form = input('Digita La Cedula Del Paciente A Actualizar: \r\n')
    existe = existe_patient(identification_patient_form)
    if existe:

        with open(CARPETA + identification_patient_form + EXTENSION, 'w') as quotes:
            identification_patient = input('Digita La Cedula Correcta: \r\n')
            name_patient = input('Digita El Nombre Correcto: \r\n')
            age_patient = input('Digita La Edad Correcta: \r\n')
            phone_patient = input('Digita El Celular Correcto: \r\n')
            barrium_patient = input('Digita El Barrio Correcto: \r\n')
            specialty = input('Digita La Especialidad Correcta: \r\n')

            appointment = Appointmen(identification_patient, name_patient, age_patient, phone_patient, barrium_patient, specialty)

            quotes.write('Identificacion: ' + appointment.identification + '\n')
            quotes.write('Nombre : ' + appointment.name + '\n')
            quotes.write('Edad: ' + appointment.age + '\n')
            quotes.write('Celular: ' + appointment.phone + '\n')
            quotes.write('Barrio: ' + appointment.barium + '\n')
            quotes.write('Especialidad: ' + appointment.specialty + '\n')
            print('Datos Modificados Exitosamente...')
        os.rename(CARPETA + identification_patient_form + EXTENSION, CARPETA + identification_patient + EXTENSION )
    else:
        print('El Paciente no existe...')        
    Appointment()

def search_appointment():
    identification_patient = input('Digite La Cedula Del Paciente A Buscar: \r\n')
    try:
        with open(CARPETA + identification_patient + EXTENSION) as quotes:
            print('Informacion De la Cita \n')
            for linea in quotes:
                print(linea.rsplit())
            print('\r\n')
    except:
        print('El Paciente No Existe...')
    Appointment()

def view_appointment():
    quotes = os.listdir(CARPETA)

    archivo_txt = [i for i in quotes if i.endswith(EXTENSION)]
    for quotes in archivo_txt:
        with open(CARPETA + quotes) as quote:
            for linea in quote:
                print(linea.rsplit())
            print('\r\n')
    Appointment()

def add_appointment():
    print('Digita Los Datos Para Crear La Cita...')
    identification_patient = input('Digita Tu Cedula: \r\n')
    
    existe = existe_patient(identification_patient)
    if not existe:
        with open(CARPETA + identification_patient + EXTENSION, 'w') as quotes:
            name_patient = input('Digita Tu Nombre: \r\n')
            age_patient = input('Digita La Edad: \r\n')
            phone_patient = input('Digita El Celular: \r\n')
            barium_patient = input('Digita El Barrio: \r\n')
            specialty = input('Especialida Cita: \r\n')

            appointment =  Appointmen(identification_patient, name_patient, age_patient, phone_patient, barium_patient, specialty)

            quotes.write(f'Identificacion paciente: ' + appointment.identification + '\n')
            quotes.write(f'Nombre Paciente: ' + appointment.name + '\n')            
            quotes.write(f'Edad Paciente: ' + appointment.age + '\n')
            quotes.write(f'Telefono Paciente: ' + appointment.phone + '\n')
            quotes.write(f'Especialidad: ' + appointment.specialty + '\n')
            print('Si Cita Ha Sido Creada Correctamente...')
    else:
        print('Paciente Ya Existes!!!')
    Appointment()

def crear_menu():
    print(f'Elija La Opcion Que Deseas: \r\n')
    print(f'1) Crear Cita')
    print(f'2) Ver Cita')
    print(f'3) Buscar Cita')
    print(f'4) Editar Cita')
    print(f'5) Eliminar Cita')
    print(f'6) Salir Del Programa')

def crar_carpeta():
    if not os.path.exists('Appointment/'):
        os.makedirs('Appointment/')

def existe_patient(identification):
    return os.path.isfile(CARPETA + identification + EXTENSION)

Appointment()