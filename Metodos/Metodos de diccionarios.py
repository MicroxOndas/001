diccionario = {
    'Nombre' : 'Marcos',
    'Apellido' : 'Escudero',
    'Edad' : 17
}

claves = diccionario.keys() # Nos devuelve las keys del diccionario
print(claves)

Dato = diccionario.get('Edad') # Si no encuentra nada no manda excepción
print(Dato)

print(diccionario['Edad'])

#Eliminar un elemento del diccionario

diccionario.pop('Edad')
print(diccionario)

# Eliminar todos los elementos del diccionario

print(diccionario)
diccionario.clear()
print(diccionario)

#Obtener un diccionario iterable

diccionario = {
    'saludo': 'Hola',
    'numero': 23
}

diccionario_iterable = diccionario.items()
print(diccionario_iterable)
