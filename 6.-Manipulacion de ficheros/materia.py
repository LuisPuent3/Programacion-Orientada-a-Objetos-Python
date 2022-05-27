class Materia:
    def __init__(self):
        self.claveMateria=str
        self.nombreMateria=str

    def leerFichero(self):
        try:
            fichero = open("materia.txt", "r")
            self.claveMateria = fichero.readline()
            self.nombreMateria = fichero.readline()
            fichero.close()
            print("Fichero leido")
        except FileNotFoundError:
            print("No se encontro el fichero")
        except ValueError:
            print("Error en el fichero")
        except Exception:
            print("Error desconocido")

    def llenarFichero(self):
        self.claveMateria = str(input("Ingrese su clave: "))
        self.nombreMateria = str(input("Ingrese su nombre: "))
        #creacion del fichero
        fichero = open("materia.txt", "w")
        fichero.write(self.claveMateria + "\n")
        fichero.write(self.nombreMateria + "\n")
        fichero.close()
        print("Fichero creado")

    def modificarFichero(self):
        print("Modificar fichero")
        self.leerFichero()
        self.mostrarDatos()
        print("¿Que dato quiere modificar?")
        print("1. Clave")
        print("2. Nombre")
        fichero = open("materia.txt", "w")
        opcion = int(input("Ingrese su opcion: "))
        if opcion == 1:
            self.claveMateria = str(input("Ingrese su clave: "))
            fichero.write(self.claveMateria + "\n")
        elif opcion == 2:
            self.nombreMateria = str(input("Ingrese su nombre: "))
            fichero.write(self.nombreMateria + "\n")
        else:
            print("Opcion no valida")
        fichero.close()

    def mostrarDatos(self):
        print("Clave: {}\nNombre: {}".format(self.claveMateria, self.nombreMateria))

