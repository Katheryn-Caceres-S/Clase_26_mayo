# esto es un diccionario llave = valor
# la el tipo de paretesis indica que es diccionario
#corchetes es una lista []
#tuplas con parentesis

colores_rgb = {
    "rojo" : "#ff0000",
    "azul" : "#0000ff",
    "negro" : "#000000",
}

colore_rgb2 = {
    "violeta" :  "#8A2BE2",
    "naranjo" : "#FF7F00",
}

print(colores_rgb)

# colores_rgb["azul"] = "#2AAA8A"

# print(colores_rgb)

# #delete

# retorno = colores_rgb.pop("rojo")

# print(retorno)
# print(colores_rgb)

#unir elementos

colores_rgb.update(colore_rgb2)
print(colores_rgb)

#esto entrega una lista de los parametros
print(colores_rgb.values())

#esto entrega un parametro determinado
print(colores_rgb.get("rojo"))

#entrega una lista de tuplas (clave,valor) del diccionario. es mas facil iterar
print(colores_rgb.items())

#para convertir una lista en diccionario dict 

#cual es la difrencia entre una lista y diccionario? Llave, valor y el otro solo valor. uno es iterable y el otro no.