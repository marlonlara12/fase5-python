# Problema 3 - Inventario y reabastecimiento

def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

inventario = [
    ["A01", "Arroz", 10, 20],
    ["A02", "Azúcar", 25, 20],
    ["A03", "Aceite", 5, 15],
    ["A04", "Sal", 8, 10],
    ["A05", "Lentejas", 30, 25]
]

print("INFORME DE REABASTECIMIENTO\n")

for item in inventario:
    codigo = item[0]
    nombre = item[1]
    stock_actual = item[2]
    stock_minimo = item[3]

    pedido = calcular_pedido(stock_actual, stock_minimo)

    print(f"Producto: {nombre} | Cantidad a pedir: {pedido}")
