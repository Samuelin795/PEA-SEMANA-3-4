import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Crear un DataFrame 
data_corr = {
    'Ansiedad': [3, 2, 5, 6, 8, 7],
    'Depresion': [4, 3, 6, 5, 9, 8],
    'Estres': [2, 3, 5, 6, 7, 9]
}
df_corr = pd.DataFrame(data_corr)

# Crear un heatmap con Seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)

# Personalizar el gráfico
plt.title('Mapa de Calor: Correlación entre Variables Psicológicas', fontsize=16)

# Mostrar el gráfico
plt.show()
