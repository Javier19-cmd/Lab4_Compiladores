
# Variables globales a utilizar.
diccionarios = [{0: {' ': 1, '\t': 1, '\n': 1}, 1: {' ': {}, '\t': {}, '\n': {}}}, {0: {' ': 1, '\t': 1, '\n': 1}, 1: {' ': 1, '\t': 1, '\n': 1}}, {0: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}, 1: {'0': {}, '1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}}}, {0: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}, 1: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}}]
iniciales = [[0], [0], [0], [0]]
finales = [[1], [1], [1], [1]]
archivo = "ej1.txt"
reservadas = []
vacio = {}

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

                v, estado_actual = simular_cadena(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept)

                # if v == False:
                #     valores_cadena.append(v)
                #     break

                if j == len(cadena_actual) - 2:
                    valores_cadena.append(v)

        # Se agrega la lista de valores de la cadena actual al resultado.
        resultado.append(valores_cadena)

        #print("Cadena: ", cadena_actual, "resultados: ", valores_cadena)

        # Verificando si el �ltimo resultado es True.
        if valores_cadena[-1] == True:
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

            if len(estado_siguiente) == 0:

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

            if len(estado_siguiente) == 0:
                
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

                v, estado_actual = simular_cadena(diccionario, estado_actual, caracter_actual, caracter_siguiente, estados_acept)

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

def impresion_res(resultados_res):
    print("Resultado de simular las palabras reservadas: ", resultados_res)

if __name__ == "__main__":
    main()
