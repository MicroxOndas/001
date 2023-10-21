# Creando una lista con list

lista = list(["hola","dalto"])

print(lista)

# Len cuenta la cantidad de elementos de una lista

cantidad_de_elementos = len(lista)

# Agregando un elemeento a la lista

lista.append("JAJAJJA")

# Agregando un elemento en un punto específico de la lista con insert

lista.insert(2,"WEEENAS")

# Agregar varios elementos con extend (hay que darle una lista para que agrege a la lista)

lista.extend([False,"Hola"])

# Eliminando un elemento por su índice con pop (índices negativos funcionan eliminando elementos desde atrás)

lista.pop(1)

lista.pop(-1)

#Eliminando un elemento por su valor ( si no lo encuentra devuelve una excepción)

lista.remove(False)


print(lista)

