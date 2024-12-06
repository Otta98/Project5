import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Leer datos del archivo CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Crear un gráfico de dispersión
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Crear la primera línea de mejor ajuste (todos los datos)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)  # Para predecir hasta el año 2050
    sea_levels_extended = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_levels_extended, label='Fit Line (1880-2050)', color='red')

    # Crear la segunda línea de mejor ajuste (desde 2000 hasta el año más reciente)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    sea_levels_recent = [slope_recent * year + intercept_recent for year in years_extended]
    plt.plot(years_extended, sea_levels_recent, label='Fit Line (2000-2050)', color='green')

    # Añadir etiquetas y título
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Añadir leyenda
    plt.legend()

    # Guardar el gráfico como imagen
    plt.savefig('sea_level_plot.png')

    # Mostrar el gráfico (opcional, solo si quieres verlo directamente)
    plt.show()

    # Retornar el gráfico para pruebas
    return plt.gca()

# Ejecutar la función de dibujo
draw_plot()
