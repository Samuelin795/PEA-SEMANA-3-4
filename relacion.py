import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame
data = {
    'Edad': [23, 25, 31, 35, 40, 42, 48, 50, 53, 60],
    'Ingresos': [30000, 32000, 45000, 47000, 50000, 52000, 58000, 60000, 62000, 70000]
}
df = pd.DataFrame(data)

# Crear un gráfico de dispersión
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Edad', y='Ingresos', data=df, color='purple')

# Personalizar el gráfico
plt.title('Relación entre Edad e Ingresos', fontsize=16)
plt.xlabel('Edad', fontsize=12)
plt.ylabel('Ingresos (en USD)', fontsize=12)
plt.grid(True)

# Mostrar el gráfico
plt.show()
