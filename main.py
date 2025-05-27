# esto es un diccionario llave = valor
# la el tipo de paretesis indica que es diccionario
#corchetes es una lista []

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

