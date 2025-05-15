import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar el archivo CSV
df = pd.read_csv("africa.csv")

# Filtrar entidades
df = df[df["Entity"].isin(["Africa", "Colombia", "Asia"])]

# Separar por región (ordenado por año)
df_africa = df[df["Entity"] == "Africa"].sort_values("Year")
df_colombia = df[df["Entity"] == "Colombia"].sort_values("Year")
df_asia = df[df["Entity"] == "Asia"].sort_values("Year")

# Obtener datos
years = df_africa["Year"].values  # Suponiendo que todas las regiones comparten estos años
africa_vals = df_africa["Renewables (% equivalent primary energy)"].values
colombia_vals = df_colombia["Renewables (% equivalent primary energy)"].values
asia_vals = df_asia["Renewables (% equivalent primary energy)"].values

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, max(africa_vals.max(), colombia_vals.max(), asia_vals.max()) + 5)
ax.set_title("Energía Renovable en África, Colombia y Asia (1965+)")
ax.set_xlabel("Año")
ax.set_ylabel("Renovables (% energía primaria)")
ax.grid(True)

# Líneas
line_africa, = ax.plot([], [], lw=2, color='green', label='África')
line_colombia, = ax.plot([], [], lw=2, color='blue', label='Colombia')
line_asia, = ax.plot([], [], lw=2, color='red', label='Asia')
text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
ax.legend()

# Inicialización
def init():
    line_africa.set_data([], [])
    line_colombia.set_data([], [])
    line_asia.set_data([], [])
    text.set_text('')
    return line_africa, line_colombia, line_asia, text

# Actualización por frame
def update(frame):
    x = years[:frame + 1]
    line_africa.set_data(x, africa_vals[:frame + 1])
    line_colombia.set_data(x, colombia_vals[:frame + 1])
    line_asia.set_data(x, asia_vals[:frame + 1])
    text.set_text(f"Año: {x[-1]}")
    return line_africa, line_colombia, line_asia, text

# Crear animación
ani = FuncAnimation(fig, update, frames=len(years), init_func=init, blit=True, interval=150)


ani.save("animacion/ondas.gif", writer="pillow", fps=5)

# Mostrar (opcional)
plt.show()