
# Variables globales a utilizar.
diccionarios = [{0: {' ': 1, '\t': 1, '\n': 1}, 1: {' ': {}, '\t': {}, '\n': {}}}, {0: {' ': 1, '\t': 1, '\n': 1}, 1: {' ': 1, '\t': 1, '\n': 1}}, {0: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}, 1: {'0': {}, '1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}}}, {0: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}, 1: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}}, {0: {'+': 1, '-': 1}, 1: {'+': {}, '-': {}}}, {0: {'0': 2, '1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, ',': {}, '+': 1, '-': 1}, 1: {'0': {}, '1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}, ',': {}, '+': {}, '-': {}}, 2: {'0': 2, '1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, ',': 3, '+': {}, '-': {}}, 3: {'0': 4, '1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4, ',': {}, '+': {}, '-': {}}, 4: {'0': 4, '1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4, ',': {}, '+': {}, '-': {}}}, {0: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1}, 1: {'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}}}, {0: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1}, 1: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1}}, {0: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}, 1: {'0': {}, '1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}}}, {0: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}, 1: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}}, {0: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, '0': 2, '1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2}, 1: {'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, '0': 3, '1': 3, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3}, 2: {'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4, '0': {}, '1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}}, 3: {'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, '0': {}, '1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}}, 4: {'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, '0': 2, '1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2}}]
iniciales = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
finales = [[1], [1], [1], [1], [1], [1, 4], [1], [1], [1], [1], [0, 3, 4]]
archivo = "ej1.txt"
reservadas = ['IF', 'FOR', 'WHILE', 'ELSE']
vacio = {}
operadores_reservados = ['(', ')', '*', '+', '-', '/', '^']

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

