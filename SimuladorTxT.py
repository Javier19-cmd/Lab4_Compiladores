"""
Nombre: Javier Valle
Carnet: 20159
Clase SimuladorTxt: 
    - Se encarga de abrir el archivo de texto y leerlo
    - Va recorrer cada elemento del archivo y va a simular cada cadena dentro del AFD.

"""

class SimuladorTxT:

    def __init__(self, diccionarios, iniciales, finales, archivo, reservadas=[]):
        self.diccionarios = diccionarios
        self.iniciales = iniciales
        self.finales = finales
        self.archivo = archivo
        self.reservadas = reservadas

        print("Palabras reservadas: ", self.reservadas)

        
        self.cad_s = [] # Arreglo para las cadenas a simular.                    

        with open(self.archivo, "r") as archivos:
            for linea in archivos:
                # Eliminando saltos de línea y separando las cadenas.
                cadenas = linea.strip().split()

                #print("Cadenas: ", cadenas)

                for cadena in cadenas: # Guardando cada cadena para simular.
                    self.cad_s.append(cadena)

        resultados_txt = self.simular_cadenas(diccionarios, iniciales, finales, resultado=[])

        self.impresion_txt(resultados_txt) # Imprimiendo los resultados de la simulación de los archivos txt.

        resultados_res = self.simular_res(diccionarios, iniciales, finales, resultado=[])

        self.impresion_res(resultados_res)

    def simular_cadenas(self, diccionarios, iniciales, finales, resultado=[]): # Simulando las cadenas que vienen en el archivo txt.

        if not diccionarios:
            #print("Resultado: ", resultado)
            return resultado


        if len(self.cad_s) == 0:
            # Si ya no quedan más cadenas por simular, se devuelve el resultado.
            #print("Resultado: ", resultado)
            return resultado
        else:

            #print("Cad_s", self.cad_s)

            # Se toma la primera cadena en la lista de cadenas.
            cadena_actual = self.cad_s.pop(0)

            #print("Cadena actual: ", cadena_actual)

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

                    #print("Estado actual: ", estado_actual)

                    v, estado_actual = self.simular_cadena(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept)

                    # if v == False:
                    #     valores_cadena.append(v)
                    #     break

                    if j == len(cadena_actual) - 2:
                        valores_cadena.append(v)

            # Se agrega la lista de valores de la cadena actual al resultado.
            resultado.append(valores_cadena)

            #print("Cadena: ", cadena_actual, "resultados: ", valores_cadena)

            if cadena_actual in self.reservadas:
                # Si la cadena actual es una palabra reservada, se agrega a la lista de resultados.
                print("Palabra reservada", cadena_actual)
                #resultado.append(True)
                #print("Cadena: ", cadena_actual, "resultados: ", True)

            # Se llama recursivamente a la función con las listas actualizadas.
            return self.simular_cadenas(diccionarios, iniciales, finales, resultado)
    
    def simular_res(self, diccionarios, iniciales, finales, resultado=[]):
        
        if not diccionarios:
            #print("Resultado: ", resultado)
            return resultado


        if len(self.reservadas) == 0:
            # Si ya no quedan más cadenas por simular, se devuelve el resultado.
            #print("Resultado: ", resultado)
            return resultado
        else:

            #print("Cad_s", self.cad_s)

            # Se toma la primera cadena en la lista de cadenas.
            cadena_actual = self.reservadas.pop(0)

            #print("Cadena actual: ", cadena_actual)

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

                    #print("Estado actual: ", estado_actual)

                    v, estado_actual = self.simular_cadena(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept)

                    # if v == False:
                    #     valores_cadena.append(v)
                    #     break

                    if j == len(cadena_actual) - 2:
                        valores_cadena.append(v)

            # Se agrega la lista de valores de la cadena actual al resultado.
            resultado.append(valores_cadena)

            #print("Cadena: ", cadena_actual, "resultados: ", valores_cadena)

            if cadena_actual in self.reservadas:
                # Si la cadena actual es una palabra reservada, se agrega a la lista de resultados.
                print("Palabra reservada", cadena_actual)
                #resultado.append(True)
                #print("Cadena: ", cadena_actual, "resultados: ", True)

            # Se llama recursivamente a la función con las listas actualizadas.
            return self.simular_res(diccionarios, iniciales, finales, resultado)

    def simular_cadena(self, diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept):

        #print("Caracter: ", caracter_actual)

        #print("Estados de aceptación: ", estados_acept)

        transiciones = diccionario[estado_actual]

        #print("Transiciones; ", transiciones)

        #print("Transiciones: ", transiciones)

        if caracter_actual in transiciones:
            estado_siguiente = transiciones[caracter_actual]

            #print("Estado siguiente: ", estado_siguiente)

            if estado_siguiente in estados_acept:
                #print("Cadena aceptada.")
                return True, estado_actual

            if estado_siguiente == {}:

                #print("Falso en caracter actual", estado_siguiente)

                return False, estado_actual
            
            elif estado_siguiente in estados_acept:
                #print("Cadena aceptada.")
                return True, estado_actual
        
            else:

                #print("Estado: ",estado_actual, estado_actual in estados_acept)

                # Si el estado siguiente es vacío.
                return True, estado_siguiente
            
        elif caracter_siguiente in transiciones:

            # Si no hay transición para el caracter actual, pero sí para el siguiente.
            estado_siguiente = transiciones[caracter_siguiente]

            if estado_siguiente in estados_acept:
                #print("Cadena aceptada.")
                return True, estado_siguiente

            if estado_siguiente == {}:
                
                #print("Falso en caracter actual", estado_siguiente)

                # Si el estado siguiente no es vacío.
                return False, estado_siguiente
            
            elif estado_siguiente in estados_acept:
                #print("Cadena aceptada.")
                return True, estado_siguiente
        
            else:
                #print("Estado: ", estado_siguiente)
                #print("Estado: ", estado_siguiente in estados_acept)
                # Si el estado siguiente es vacío.
                return True, estado_siguiente
        
        elif caracter_actual not in transiciones:

            return False, estado_actual
            
        else:
    
            #print("Estado actual: ", estado_actual, transiciones)

            if transiciones != {}:
                # Si no hay transición para el caracter actual ni para el siguiente.
                return True, estado_actual
            
            else: 
            
                # Si no hay transición para el caracter actual ni para el siguiente.
                return False, estado_actual

    
    def impresion_txt(self, resultado): # Método para simular los resultados de la simulada de los archivos txt.
        
        print("Resultados de simular las cadenas del archivo txt: ", resultado)

    def impresion_res(self, resultado): # Método para simular los resultados de la simulada de los archivos txt.
        
        print("Resultados de simular las cadenas de las palabras reservadas: ", resultado)
        