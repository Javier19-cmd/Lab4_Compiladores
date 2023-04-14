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

        self.simular(diccionarios, iniciales, finales, resultado=[])

    def simular(self, diccionarios, iniciales, finales, resultado=[]): 

        cad_s = [] # Arreglo para las cadenas a simular.                    

        with open(self.archivo, "r") as archivo:
            for linea in archivo:
                # Eliminando saltos de línea y separando las cadenas.
                cadenas = linea.strip().split()

                #print("Cadenas: ", cadenas)

                for cadena in cadenas: # Guardando cada cadena para simular.
                    cad_s.append(cadena)

        if not diccionarios:
            return resultado


        if len(cad_s) == 0:
            # Si ya no quedan más cadenas por simular, se devuelve el resultado.
            return resultado
        else:
            # Se toma la primera cadena en la lista de cadenas.
            cadena_actual = cadenas.pop(0)

            # Se simula la cadena en cada diccionario en la lista de diccionarios.
            valores_cadena = []
            for i in range(len(diccionarios)):
                diccionario = diccionarios[i]
                estado_ini = iniciales[i]
                estados_acept = finales[i]
                estado_actual = estado_ini[0]

                # Se simula la cadena en el diccionario actual.
                for j in range(len(cadena_actual) - 1):
                    caracter_actual = cadena_actual[j]
                    caracter_siguiente = cadena_actual[j+1]
                    v, estado_actual = self.simular_cadena(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept)

                    # if v == False:
                    #     valores_cadena.append(v)
                    #     break

                    if j == len(cadena_actual) - 2:
                        valores_cadena.append(v)

            # Se agrega la lista de valores de la cadena actual al resultado.
            resultado.append(valores_cadena)

            print("Resultado: ", resultado)

            # Se llama recursivamente a la función con las listas actualizadas.
            return self.simular(diccionarios[1:], iniciales[1:], finales[1:], resultado)

    def simular_cadena(self, diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept):

        transiciones = diccionario[estado_actual]

        #print("Transiciones: ", transiciones)

        if caracter_actual in transiciones:
            estado_siguiente = transiciones[caracter_actual]

            #print("Estado siguiente: ", estado_siguiente)

            if estado_actual in estados_acept:
                #print("Cadena aceptada.")
                return True, estado_siguiente

            if estado_siguiente != {}:
                # Si el estado siguiente no es vacío.
                return False, estado_siguiente
        
            else:
                # Si el estado siguiente es vacío.
                return False, estado_actual
            
        elif caracter_siguiente in transiciones:

            # Si no hay transición para el caracter actual, pero sí para el siguiente.
            estado_siguiente = transiciones[caracter_siguiente]

            if estado_siguiente in estados_acept:
                #print("Cadena aceptada.")
                return True, estado_siguiente

            if estado_siguiente != {}:
                # Si el estado siguiente no es vacío.
                return False, estado_siguiente
        
            else:
                # Si el estado siguiente es vacío.
                return False, estado_actual
            
        else:
            # Si no hay transición para el caracter actual ni para el siguiente.
            return False, estado_actual

