# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí copiar la función "generar_invitados"
# ya elaborada
def generar_invitados(invitados):
    
    for i in range(3):
        nombres = input("ingrese un nombre:")
        invitados.append(nombres)
        print("lista de invitados:",invitados)
    return invitados 
# --------------------------------

# --------------------------------
# Aquí copiar la función "ordenar"
# ya elaborada
def ordenar(invitados):
    lista_ordenadas=sorted(invitados)
    print("Lista ordenadas:",lista_ordenadas)
    return lista_ordenadas
# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: Copiar las funciones "generar_invitados" y "ordenar" 
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bucle "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenala 
    invitados = []
    
    # Luego de copiar las funciones, invocarla en este lugar:
    generar_invitados(invitados)
    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el resultado en "lista_invitados"
    
    # lista_invitados = generar_invitados()
    lista_invitados = generar_invitados(invitados) #    ------- GENERO MAS 3 INVITADOS--------
    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada

    # lista_invidatos_ordenada = ordenar(lista_invitados)
    lista_invidatos_ordenada = ordenar(lista_invitados)
    # Imprimir en pantalla "lista_invidatos_ordenada":
    print("Lista ordenada: {}",format(lista_invidatos_ordenada))
    print("terminamos")
