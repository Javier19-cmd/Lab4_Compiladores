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

        
        self.cad_s = [] # Arreglo para las cadenas a simular.                    

        with open(self.archivo, "r") as archivos:
            for linea in archivos:
                # Eliminando saltos de línea y separando las cadenas.
                cadenas = linea.strip().split()

                #print("Cadenas: ", cadenas)

                for cadena in cadenas: # Guardando cada cadena para simular.
                    self.cad_s.append(cadena)

        resultados = self.simular(diccionarios, iniciales, finales, resultado=[])

        self.impresion(resultados)

    def simular(self, diccionarios, iniciales, finales, resultado=[]): 

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

            print("Cadena: ", cadena_actual, "resultados: ", valores_cadena)

            # Se llama recursivamente a la función con las listas actualizadas.
            return self.simular(diccionarios, iniciales, finales, resultado)

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
            
        else:
    
            #print("Estado actual: ", estado_actual, transiciones)

            if transiciones != {}:
                # Si no hay transición para el caracter actual ni para el siguiente.
                return True, estado_actual
            else: 
                # Si no hay transición para el caracter actual ni para el siguiente.
                return False, estado_actual


    
    def impresion(self, resultado):
        
        print("Resultados: ", resultado)
        
        # for i in range(len(resultado)):
        #     print("Cadena ", i+1, ": ", resultado[i])