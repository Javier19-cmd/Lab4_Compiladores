"""
Nombre: Javier Valle
Carnet: 20159
Clase SimuladorTxt: 
    - Se encarga de abrir el archivo de texto y leerlo
    - Va recorrer cada elemento del archivo y va a simular cada cadena dentro del AFD.

"""

class SimuladorTxT:

    def __init__(self, diccionarios, iniciales, finales, archivo):
        self.diccionarios = diccionarios
        self.iniciales = iniciales
        self.finales = finales
        self.archivo = archivo

        self.simular()

    def simular(self): 

        """
        Método que funciona para abrir el archivo.
        """

        print("Diccionarios: ", self.diccionarios)
        print("Iniciales: ", self.iniciales)
        print("Finales: ", self.finales)
        print("Archivo: ", self.archivo)
        