cadena1 = 'SoyEscuSoy'
cadena2 = 'Soy un máquina'
A = 'print'
#Print es una función.

print(A)

#dir es una función.  Devuelve todos los atributos validos para el objeto

dir(cadena1)

#upper Convierte todo a mayúscula

Resultado = cadena1.upper()

#lower Convierte todo a minúscula

Resultado = cadena1.lower()

#capitalize  Convierte todo a minuscula y la primera letra la pasa a mayúscula

Resultado = cadena1.capitalize()

#Find busca la primera cadena que pueda encontrar dentro de una cadena si no hay coincidencia devuelve -1

busqueda_find = cadena1.find('Soy')

#index igual que find, solo que si no encuentra algo lanza un error

busqueda_index = cadena1.index('S')

#isnumeric si es numérico devuelve True sino False

es_numerico = cadena1.isnumeric()

#isalpha si es alfanumérico devuelve True sino False
#PERO CUIDADO, LOS ESPACIOS NO SON ALFANUMÉRICOS
es_alfa = cadena1.isalpha()

#count buscamos un cadena en otra cadena, devuelve la cantidad de veces que coincida

contar_coincidencias = cadena1.count('Soy')

#len es una función. Cuenta cuantos caractéres tiene una cadena

contar_caracteres = len(cadena1)

#startswith Verifica si una cadena empieza con una cadena dada, si es así devuelve True, else devuelve False

Empieza = cadena1.startswith('Soy')

#endswith Verifica si una cadena acaba con una cadena dada, ...

Acaba = cadena1.endswith('Soy')

# Replace   Reemplaza una cadena 

Remplazada = cadena1.replace('Soy','Eres')

#Separar cadenas por la cadena que la demos en una lista

Spliteada = cadena1.split('s')

print(Spliteada)


