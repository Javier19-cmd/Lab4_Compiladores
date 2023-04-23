"""
Nombre: Javier Valle
Carnet: 20159
Clase SimuladorTxt: 
    - Se encarga de abrir el archivo de texto y leerlo
    - Va recorrer cada elemento del archivo y va a simular cada cadena dentro del AFD.

"""

class SimuladorTxT:

    def __init__(self, diccionarios, iniciales, finales, archivo, reservadas=[], operadores_reservados=[], tokens=[], tabla={}):
        self.diccionarios = diccionarios
        self.iniciales = iniciales
        self.finales = finales
        self.archivo = archivo
        self.reservadas = reservadas
        self.operadores_reservados = operadores_reservados
        self.tokens = tokens
        self.tabla = tabla
        
        self.diccionario_cadenas = {} # Diccionario para las cadenas.

        self.reservadas = ["IF", "FOR", "WHILE", "ELSE"]

        # Quitando las palabras reservadas de los tokens.
        for palabra in self.reservadas:
            if palabra in self.tokens:
                self.tokens.remove(palabra)

        # Cambiando cosas de la tabla.
        
        # Cambiando el signo negativo.
        new_m = "-"
        for key in self.tabla:
            if "~" in self.tabla[key]:
                value = self.tabla[key].replace("~", new_m)
                self.tabla[key] = value
        
        # Cambiando el signo positivo.
        new_m = "+"
        for key in self.tabla:
            if "@" in self.tabla[key]:
                value = self.tabla[key].replace("@", new_m)
                self.tabla[key] = value
        
        # Cambiando los delimitadores.

        # Espacio en blanco.
        new_m = " "
        for key in self.tabla:
            if "≡" in self.tabla[key]:
                value = self.tabla[key].replace("≡", new_m)
                self.tabla[key] = value
        
        # Tabulador.
        new_m = "\t"
        for key in self.tabla:
            if "¥" in self.tabla[key]:
                value = self.tabla[key].replace("¥", new_m)
                self.tabla[key] = value
        
        # Quiebre de línea.
        new_m = "\n"
        for key in self.tabla:
            if "§" in self.tabla[key]:
                value = self.tabla[key].replace("§", new_m)
                self.tabla[key] = value

        print("Tabla: ", self.tabla)

        # Juntando las listas de reservadas, operadores_reservado y tokens.
        self.lista = []
        self.lista.extend(self.reservadas)
        self.lista.extend(self.operadores_reservados)
        self.lista.extend(self.tokens)

        res_copy = self.reservadas.copy()

        #print("Palabras reservadas: ", self.reservadas)

        
        self.cad_s = [] # Arreglo para las cadenas a simular.                    

        with open(self.archivo, "r") as archivos:
            for linea in archivos:
                # Eliminando saltos de línea y separando las cadenas.
                cadenas = linea.strip().split()

                #print("Cadenas: ", cadenas)

                for cadena in cadenas: # Guardando cada cadena para simular.
                    self.cad_s.append(cadena)

        resultados_txt = self.simular_cadenas(diccionarios, iniciales, finales, resultado=[])

        #self.impresion_txt(resultados_txt) # Imprimiendo los resultados de la simulación de los archivos txt.

        resultados_res = self.simular_res()

        #self.impresion_res(resultados_res)
        
        # Generando el archivo py. 
        self.archivopy = "implmentacion.py"
        
        self.generar_py(self.archivopy, self.diccionarios, self.iniciales, self.finales, self.archivo, res_copy, self.operadores_reservados)

    def simular_cadenas(self, diccionarios, iniciales, finales, resultado=[]): # Simulando las cadenas que vienen en el archivo txt.

        if not diccionarios:
            #print("Resultado: ", resultado)
            return resultado
        
        # # Detectando los operadores.
        # if len(caracter_actual) == 1: # Detectando primero su longitud.
        #     if caracter_actual in self.operadores_reservados: # Detectando si es un operador.
        #         print("Operador detectado")
        #         return True, estado_actual


        if len(self.cad_s) == 0:
            # Si ya no quedan más cadenas por simular, se devuelve el resultado.
            #print("Resultado: ", resultado)
            return resultado
        else:

            #print("Cad_s", self.cad_s)

            # Se toma la primera cadena en la lista de cadenas.
            cadena_actual = self.cad_s.pop(0)

            # Sacando una copia de la cadena.
            self.cadena_copy = cadena_actual

            #print("Cadena actual: ", cadena_actual)

            # Si la cadena empieza y termina con comillas dobes, es porque es una cadena entera la que se debe simular.
            if cadena_actual[0] == '"' and cadena_actual[-1] == '"':
                #print("Cadena: ", cadena_actual)

                # Si la cadena empieza y termina con comiilas, entonces se simula todo de un solo, sin dividirlo.
                # Se quitan las comillas.
                cadena_actual = cadena_actual.replace('"', '')

                #print("Cadena actual: ", cadena_actual)

            # if cadena_actual.count('"') == 2: # Detectando si la cadena actual es una cadena de texto.
                
            #     for caracter in cadena_actual:
            #         if caracter.isalpha():
            #             #print("Caracter")
            #             # Quitar las comillas de la cadena.
            #             cadena_actual = cadena_actual.replace('"', '')
                
            # else: 
            #     # Si no es una cadena de texto, se verifica si es una palabra reservada.
            #     if cadena_actual in self.reservadas:
            #         # Si la cadena actual es una palabra reservada, se agrega a la lista de resultados.
            #         print("Palabra reservada", cadena_actual)
            #         resultado.append(True)
                
            #     # Si la cadena es diferente a un número, entonces no importa.
            #     if cadena_actual.isdigit() == False:
            #         pass

            # # Detectando los operadores.
            # if len(cadena_actual) == 1: # Detectando primero su longitud.
            #     if cadena_actual in self.operadores_reservados: # Detectando si es un operador.
            #         print("Operador detectado")

            #print("Cadena actual: ", cadena_actual)

            # Se simula la cadena en cada diccionario en la lista de diccionarios.
            valores_cadena = []
            for i in range(len(diccionarios)):
                diccionario = diccionarios[i]
                estado_ini = iniciales[i]
                estados_acept = finales[i]
                estado_actual = estado_ini[0]

                # Detectando los operadores.
                if len(cadena_actual) == 1:
                    if cadena_actual in self.operadores_reservados: 

                        #print("Cadena actual: ", cadena_actual)
                        #valores_cadena.append(True)

                        # Verificando que se haya llegado al último diccionario.
                        if i == len(diccionarios) - 1:
                            # Si se llegó al último diccionario, se agrega el valor a la lista de valores de la cadena actual.
                            valores_cadena.append(True)

                    else: 
                        
                        # Verificando que se haya llegado al último diccionario.
                        if i == len(diccionarios) - 1:
                            # Si se llegó al último diccionario, se agrega el valor a la lista de valores de la cadena actual.
                            valores_cadena.append(False)

                # Se simula la cadena en el diccionario actual.
                for j in range(len(cadena_actual) - 1):
                    caracter_actual = cadena_actual[j]
                    caracter_siguiente = cadena_actual[j+1]

                    #print("Estado actual: ", estado_actual)

                    v, estado_actual = self.simular_cadena(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept)

                    # Si hay un estado igual a {}, entonces regresarlo al inicial.
                    if estado_actual == {}:
                        estado_actual = estado_ini[0]
                        
                    if j == len(cadena_actual) - 2:
                        valores_cadena.append(v)

                        
            
            # Verificando si en la tabla está la definición de string.
            if 'string' in self.tabla:
                # Imprimiendo el último valor de valores_cadena.
                #print("Valores cadena: ", valores_cadena[-1])

                # Si la cadena_actual tenía " al prinicipo o al final, entonces es string.
                if self.cadena_copy.startswith('"') or self.cadena_copy.endswith('"'):
                    valores_cadena[-1] = True
                else: 
                    valores_cadena[-1] = False
            
            # Verificando si hay un endline en la tabla.
            if 'endline' in self.tabla:
                # Obteniendo el valor del endline.
                endline = self.tabla['endline']

                #print("Endline: ", endline)
                
                # Quitándole los paréntesis al endline.
                endline = endline.replace('(', '')
                endline = endline.replace(')', '')

                # Imprimiendo los resultados.
                #print("Valores cadena: ", valores_cadena)

                # 8 y 9.
                if valores_cadena[8] == True and valores_cadena[9] == True:
                    pass
                elif valores_cadena[8] == False and valores_cadena[8] == False:
                    pass
                elif valores_cadena[7] == False and valores_cadena[8] == True: 
                    
                    if cadena_actual in self.reservadas:
                        pass
                    else:

                        # Volviendo falso todos los valores de la cadena actual.
                        for i in range(len(valores_cadena)):
                            valores_cadena[i] = False

                        # with open(self.archivo, "r") as arc:
                        #     for i, linea in enumerate(arc):
                        #         if cadena_actual in linea:
                        #             print("Sintax error: " + cadena_actual + " line: ", i+1)

            # Guardando la cadena y sus resultados en un diccionario.
            self.diccionario_cadenas[cadena_actual] = valores_cadena
    

            # Se agrega la lista de valores de la cadena actual al resultado.
            resultado.append(valores_cadena)

            #print("Cadena: ", cadena_actual, "resultados: ", valores_cadena)

            # Verificando si hay un true en la lista de valores cadena.
            if True in valores_cadena:
                pass
            else:
                # Buscando el número de línea en donde se encuentra la cadena actual en el archivo.
                with open(self.archivo, "r") as archivos:
                    for i, linea in enumerate(archivos):
                        if cadena_actual in linea:
                            print("Sintax error: " + cadena_actual + " line: ", i+1)

            # if cadena_actual in self.reservadas:
            #     # Si la cadena actual es una palabra reservada, se agrega a la lista de resultados.
            #     print("Palabra reservada", cadena_actual)
            #     #resultado.append(True)
            #     #print("Cadena: ", cadena_actual, "resultados: ", True)

            # Se llama recursivamente a la función con las listas actualizadas.
            return self.simular_cadenas(diccionarios, iniciales, finales, resultado)
    
    def simular_res(self):
        # Imprime las variables de seguimiento definidas en la clase.
        # print("Tokens: ", self.tokens)
        # print("Operadores reservados: ", self.operadores_reservados)
        # print("Reservadas: ", self.reservadas)
        # print("Diccionario cadenas: ", self.diccionario_cadenas)
        
        # Variables de seguimiento.
        ultima_vez_operador = False
        ultima_vez_reservada = False
        ultima_vez_token = {}

        diccionario = {}

        for clave in self.tokens:
            ultima_vez_token[clave] = False
            
        # Recorre los diccionarios y listas definidos en la clase.
        for clave in self.diccionario_cadenas:
            lista = self.diccionario_cadenas[clave]

            # Detecta los operadores.
            if len(lista) == 1: 
                if lista[0] == True:
                    print("Operador detectado", clave)
                elif lista[0] == False:
                    # Abre el archivo para buscar el caracter.
                    with open(self.archivo, "r") as archivos:
                        for i, linea in enumerate(archivos):
                            if clave in linea:
                                print("Sintax error: " + clave + " line: ", i+1)

            for i, valor in enumerate(lista):

                # Busca el token en la tabla de símbolos definida en la clase.
                for s, (key, value) in enumerate(self.tabla.items()):
                    if valor == True:
                        # Imprime la llave que corresponde al valor de la tabla.
                        if i == s:
                            # En el caso de los tokens encontrados, imprime el último que se encontró de cada uno.
                            if key in self.tokens:
                                if clave in self.reservadas:
                                    # Si la cadena actual es una palabra reservada, se agrega a la lista de resultados.
                                    print("Palabra reservada", clave)
                                    ultima_vez_operador = False
                                    ultima_vez_reservada = True
                                    ultima_vez_token[key] = False

                                elif key in self.operadores_reservados:
                                    # Si la cadena actual es un operador reservado, se agrega a la lista de resultados.
                                    if not ultima_vez_operador:
                                        print("Operador reservado", clave)
                                        ultima_vez_operador = True
                                        ultima_vez_reservada = False
                                        ultima_vez_token[key] = False

                                else:
                                    
                                    ultima_vez_operador = False
                                    ultima_vez_reservada = False
                                    ultima_vez_token[key] = True

                                    #print("Token ", clave, " es ", key)

                                    diccionario[clave] = key
        
        # Imprime los tokens encontrados.
        #print("Tokens encontrados: ", diccionario)

        # Imprimiendo el diccionario llave por llave.
        for keys, value in diccionario.items():
            print("Token: ", keys, "type: ", value)


    def simular_cadena(self, diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept):

        #print("Caracter: ", caracter_actual)

        #print("Estados de aceptación: ", estados_acept)

        transiciones = diccionario[estado_actual]

        #print("Transiciones; ", transiciones)

        # print("Caracter actual: ", caracter_actual)
    
        if caracter_actual in transiciones:
            estado_siguiente = transiciones[caracter_actual]

            #print("Estado siguiente: ", estado_siguiente)

            if estado_siguiente in estados_acept:
                #print("Cadena aceptada.")
                return True, estado_actual
            
            # if estado_actual in estados_acept:
            #     print("Cadena aceptada.")
            #     return True, estado_actual

            if estado_siguiente == {}:

                #print("Falso en caracter actual", estado_siguiente)
                # print("Estado actual: ", estado_actual)
                # print("Estado siguiente: ", estado_siguiente)

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
                
                #print("Falso en caracter siguiente", estado_siguiente)

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
    
    def simular_cadena2(self, diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept):
                #print("Caracter: ", caracter_actual)

        #print("Estados de aceptación: ", estados_acept)

        transiciones = diccionario[estado_actual]

        #print("Transiciones; ", transiciones)

        # print("Caracter actual: ", caracter_actual)
    
        if caracter_actual in transiciones:
            estado_siguiente = transiciones[caracter_actual]

            #print("Estado siguiente: ", estado_siguiente)

            if estado_siguiente in estados_acept:
                #print("Cadena aceptada.")
                return True, estado_actual
            
            # if estado_actual in estados_acept:
            #     print("Cadena aceptada.")
            #     return True, estado_actual

            if estado_siguiente == {}:

                #print("Falso en caracter actual", estado_siguiente)
                # print("Estado actual: ", estado_actual)
                # print("Estado siguiente: ", estado_siguiente)

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
                
                #print("Falso en caracter siguiente", estado_siguiente)

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
    

    # Generando el archivo .py.
    def generar_py(self, nombre, diccionarios, iniciales, finales, archivo, reservadas, operadores_reservados):

        # print(diccionarios)
        # print(iniciales)
        # print(finales)
        # print(archivo)
        # print(reservadas)
        vacio = {}
    

        datas = f"""
# Variables globales a utilizar.
diccionarios = {'{}'}
iniciales = {'{}'}
finales = {'{}'}
archivo = {'{}'}
reservadas = {'{}'}
vacio = {'{}'}
operadores_reservados = {'{}'}

def main():
    
    # Definiendo un arreglo para las cadenas a simular.
    cadenas = []

    with open(archivo, "r") as archivos:
        for linea in archivos: 
            cadena = linea.strip().split()

            for caden in cadena: # Guardando cada cadena para simular.
                cadenas.append(caden)
    
    resultados_txt = simular_cadenas(cadenas, diccionarios, iniciales, finales, resultado=[])

    impresion_txt(resultados_txt) # Imprimiendo los resultados de la simulaci�n de los archivos txt.

    resultados_res = simular_res(diccionarios, iniciales, finales, resultado=[])

    impresion_res(resultados_res)

def simular_cadenas(cad_s, diccionarios, iniciales, finales, resultado=[]):
    if not diccionarios:
        #print("Resultado: ", resultado)
        return resultado


    if len(cad_s) == 0:
        # Si ya no quedan m�s cadenas por simular, se devuelve el resultado.
        #print("Resultado: ", resultado)
        return resultado
    else:

        #print("Cad_s", self.cad_s)

        # Se toma la primera cadena en la lista de cadenas.
        cadena_actual = cad_s.pop(0)

        # Sacando una copia de la cadena.
        cadena_copy = cadena_actual

        # Detectando si la cadena actual es una cadena de texto.
        if cadena_actual.count('"') == 2:

            for caracter in cadena_actual:
                if caracter.isalpha():
                    # Quitar las comillas de la cadena.
                    cadena_actual = cadena_actual.replace('"', '')
        
        else:
            # Si no es una cadena de texto, se verifica si es una palabra reservada.
            if cadena_actual in reservadas:
                # Si la cadena actual es una palabra reservada, se agrega a la lista de resultados.
                resultado.append(True)
            
            # Si la cadena es diferente a un número, entonces no importa.
            if cadena_actual.isdigit() == False:
                pass

        #print("Cadena actual: ", cadena_actual)

        # Se simula la cadena en cada diccionario en la lista de diccionarios.
        valores_cadena = []
        for i in range(len(diccionarios)):
            diccionario = diccionarios[i]
            estado_ini = iniciales[i]
            estados_acept = finales[i]
            estado_actual = estado_ini[0]

            # Detectando los operadores.
            if len(cadena_actual) == 1:
                if cadena_actual in operadores_reservados:

                    # Verificando que se haya llegado al último diccionario.
                    if i == len(diccionarios) - 1:
                        # Si se llegó al último diccionario, se agrega True a la lista de resultados.
                        valores_cadena.append(True)
                    
                    else: 
                        if i == len(diccionarios) - 1:
                            # Si se llegó al último diccionario, se agrega el valor a la lista de valores de la cadena actual.
                            valores_cadena.append(True)

            # Se simula la cadena en el diccionario actual.
            for j in range(len(cadena_actual) - 1):
                caracter_actual = cadena_actual[j]
                caracter_siguiente = cadena_actual[j+1]

                #print("Estado actual: ", estado_actual)

                v, estado_actual = simular_cadena(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept)

                # if v == False:
                #     valores_cadena.append(v)
                #     break

                if j == len(cadena_actual) - 2:
                    valores_cadena.append(v)
        
        # Si la copia de la cadena tenía "", entonces analizar su lista de valores_cadena.
        if cadena_copy.count('"') == 2:
            print("Cadena: ", cadena_actual, "resultados: ", valores_cadena)

            # Verificando si hay un true en la lista de valores cadena en la posición 7.
            if valores_cadena[6] == True:
                pass
            else:
                
                valores_cadena[7] = False
                
                # Buscando el número de línea en donde se encuentra la cadena actual en el archivo.
                with open(archivo, "r") as archivos:
                    for i, linea in enumerate(archivos):
                        if cadena_actual in linea:
                            print("Sintax error: " + cadena_actual + " line: ", i+1)

        # Se agrega la lista de valores de la cadena actual al resultado.
        resultado.append(valores_cadena)

        #print("Cadena: ", cadena_actual, "resultados: ", valores_cadena)

        # Verificando si el �ltimo resultado es True.
        if True in valores_cadena:
            pass
        else:
            # Buscando el n�mero de l�nea en donde se encuentra la cadena actual en el archivo.
            with open(archivo, "r") as archivos:
                for i, linea in enumerate(archivos):
                    if cadena_actual in linea:
                        print("Sintax error: " + cadena_actual + " line: ", i+1)

        if cadena_actual in reservadas:
            # Si la cadena actual es una palabra reservada, se agrega a la lista de resultados.
            print("Palabra reservada", cadena_actual)
            #resultado.append(True)
            #print("Cadena: ", cadena_actual, "resultados: ", True)

        # Se llama recursivamente a la funci�n con las listas actualizadas.
        return simular_cadenas(cad_s, diccionarios, iniciales, finales, resultado)

def impresion_txt(resultados_txt):
    print("Resultados de simular las cadenas del archivo txt: ", resultados_txt)

def simular_cadena(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept):
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

            if estado_siguiente == vacio:

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

            if estado_siguiente == vacio:
                
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

            if len(transiciones) != 0:
                # Si no hay transición para el caracter actual ni para el siguiente.
                return True, estado_actual
            
            else: 
            
                # Si no hay transición para el caracter actual ni para el siguiente.
                return False, estado_actual

def simular_res(diccionarios, iniciales, finales, resultado=[]):
    if not diccionarios:
        #print("Resultado: ", resultado)
        return resultado


    if len(reservadas) == 0:
        # Si ya no quedan más cadenas por simular, se devuelve el resultado.
        #print("Resultado: ", resultado)
        return resultado
    else:

        #print("Cad_s", self.cad_s)

        # Se toma la primera cadena en la lista de cadenas.
        cadena_actual = reservadas.pop(0)

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

                v, estado_actual = simular_cadena2(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept)

                # if v == False:
                #     valores_cadena.append(v)
                #     break

                if j == len(cadena_actual) - 2:
                    valores_cadena.append(v)

        # Se agrega la lista de valores de la cadena actual al resultado.
        resultado.append(valores_cadena)

        #print("Cadena: ", cadena_actual, "resultados: ", valores_cadena)

        if cadena_actual in reservadas:
            # Si la cadena actual es una palabra reservada, se agrega a la lista de resultados.
            print("Palabra reservada", cadena_actual)
            #resultado.append(True)
            #print("Cadena: ", cadena_actual, "resultados: ", True)

        # Se llama recursivamente a la función con las listas actualizadas.
        return simular_res(diccionarios, iniciales, finales, resultado)

def simular_cadena2(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept):
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

            if estado_siguiente == vacio:

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

            if estado_siguiente == vacio:
                
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

            if len(transiciones) != 0:
                # Si no hay transición para el caracter actual ni para el siguiente.
                return True, estado_actual
            
            else: 
            
                # Si no hay transición para el caracter actual ni para el siguiente.
                return False, estado_actual

def impresion_res(resultados_res):
    print("Resultado de simular las palabras reservadas: ", resultados_res)

if __name__ == "__main__":
    main()

""".format(diccionarios, iniciales, finales, str('"{}"'.format(archivo)), reservadas, vacio, operadores_reservados)
        
        with open(nombre, 'w', encoding='utf-8') as f:
            f.write(datas)