import matplotlib.pyplot as plt

# Datos
productos = ['Terapia familiar', 'Terapia pareja', 'Terapia adolecentes', 'Terapia mayor']
ventas = [150, 220, 320, 180]

# Crear el gráfico
plt.figure(figsize=(8, 6))
plt.bar(productos, ventas, color='teal')

# Personalizar el gráfico
plt.title('Ventas por Producto', fontsize=16)
plt.xlabel('Producto', fontsize=12)
plt.ylabel('Ventas (en unidades)', fontsize=12)

# Mostrar el gráfico
plt.show()
