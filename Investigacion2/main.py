comidas = {"Pizza", "Tacos", "Hamburguesa", "Sandwich", "Quezadilla", "Pure"}
bebidas = {"Agua", "Refresco", "Cerveza", "Chocomilk", "Tequila", "Pure"}

print("El conjunto de comidas esta formado por: \n", comidas )
print("El conjunto de bebidas esta formado por: \n", bebidas )

conjunto = set()
comidas.update(["Enchiladas", "Pollo a la plancha"])
bebidas.discard("Chocomilk")

print("El nuevo conjunto de comidas y bebidas son: \n")
print("Comidas: ", comidas )
print("\nBebidas:", bebidas)

conjunto = comidas & bebidas
print("Los conjuntos tienen en comun: ", conjunto)

conjunto = comidas - bebidas
print(conjunto, "no son bebidas, por lo tanto no pertenecen a su conjunto")