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

        cad_s = []
        

        with open(self.archivo, "r") as archivo:
            for linea in archivo:
                # Eliminando saltos de línea y separando las cadenas.
                cadenas = linea.strip().split()

                for cadena in cadenas: # Guardando cada cadena para simular.
                    cad_s.append(cadena)

        print("Cadenas a simular: ", cad_s)

        cadena_actual = cad_s.pop()

        # Jalando el primer diccionario.
        diccionario = self.diccionarios.pop()

        print("Diccionario de simulación: ", diccionario)

        # Simulando cada cadena.

        # Jalando el arreglo del estado inicial.
        estado_act = self.iniciales.pop()

        estado_actual = estado_act[0] # Estado actual.

        # Jalando los estados de aceptación.
        estados_acept = self.finales.pop()

        print("Estado actual: ", estado_act)
        print("Estados de aceptación: ", estados_acept)

        # Valores de verdad.
        vVerdad = []

        for i in range(len(cadena) - 1):
            caracter_actual = cadena[i]
            caracter_siguiente = cadena[i+1]

            v, estado_actual = self.simular_cadena(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept)

            if v == True:
                print("Cadena aceptada.")
                # Regresando el estado actual al inicio para probar los siguientes caracteres.
                
                #print("Estado actual: ", estado_act)
                estado_actual = estado_act[0]


            if v == False:
                print("Cadena no aceptada.")
                break

            # # Pusheando el último valor de v a la lista de vVerdad. (Esto tiene que ser solo el últmo y los demás no se agregan)
            # vVerdad.append(v)

            # Verficando que i haya llegado al final de la cadena.
            if i == len(cadena) - 2:
                # Si i es igual al último caracter de la cadena.
                vVerdad.append(v)
        
        print("Valores de verdad: ", vVerdad)


        # # Enviando la primera cadena.
        # self.simular_cadena(cadena_actual, estado_act, estados_acept, diccionario)

    def simular_cadena(self, diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept):

        transiciones = diccionario[estado_actual]

        #print("Transiciones: ", transiciones)

        if caracter_actual in transiciones:
            estado_siguiente = transiciones[caracter_actual]

            #print("Estado siguiente: ", estado_siguiente)

            if estado_actual in estados_acept:
                print("Cadena aceptada.")
                return True, estado_siguiente

            if estado_siguiente != {}:
                # Si el estado siguiente no es vacío.
                return estado_siguiente
        
            else:
                # Si el estado siguiente es vacío.
                return False
            
        elif caracter_siguiente in transiciones:

            # Si no hay transición para el caracter actual, pero sí para el siguiente.
            estado_siguiente = transiciones[caracter_siguiente]

            if estado_siguiente in estados_acept:
                print("Cadena aceptada.")
                return True, estado_siguiente

            if estado_siguiente != {}:
                # Si el estado siguiente no es vacío.
                return estado_siguiente
        
            else:
                # Si el estado siguiente es vacío.
                return False
            
        else:
            # Si no hay transición para el caracter actual ni para el siguiente.
            return False

