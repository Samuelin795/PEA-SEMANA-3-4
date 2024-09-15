import matplotlib.pyplot as plt
import numpy as np

# Datos
meses = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'])
ventas = np.array([250, 300, 200, 450, 500, 600])

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(meses, ventas, marker='o', color='b', linestyle='--', label='Ventas')

# Personalizar el gráfico
plt.title('Ventas mensuales', fontsize=16)
plt.xlabel('Meses', fontsize=12)
plt.ylabel('Ventas (en unidades)', fontsize=12)
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()
