import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

# Asegurarse de que la carpeta "animacion" exista
os.makedirs("animacion", exist_ok=True)

# ============================
# 1. Onda seno desplazada
# ============================
fig1, ax1 = plt.subplots()
ax1.set_xlim(0, 2 * np.pi)
ax1.set_ylim(-1.5, 1.5)
ax1.set_title("Onda Seno Desplazada")
ax1.set_xlabel("x")
ax1.set_ylabel("sin(x + t)")
ax1.grid(True)

line1, = ax1.plot([], [], lw=2, color='blue')
text1 = ax1.text(0.05, 0.9, '', transform=ax1.transAxes)

def init_seno():
    line1.set_data([], [])
    text1.set_text('')
    return line1, text1

def update_seno(frame):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + frame / 10)
    line1.set_data(x, y)
    text1.set_text(f"t = {frame / 10:.1f}")
    return line1, text1

ani1 = FuncAnimation(fig1, update_seno, frames=100, init_func=init_seno, blit=True, interval=50)
ani1.save("animacion/onda_desplazada.gif", writer="pillow", fps=20)
plt.close(fig1)

# ============================
# 2. Partículas aleatorias
# ============================
fig2, ax2 = plt.subplots()
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_title("Partículas Aleatorias")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.grid(True)

num_points = 50
x2 = np.random.rand(num_points) * 10
y2 = np.random.rand(num_points) * 10
scat2 = ax2.scatter(x2, y2, c='red', s=100)

def init_particulas():
    scat2.set_offsets(np.c_[x2, y2])
    return scat2,

def update_particulas(frame):
    global x2, y2
    dx = (np.random.rand(num_points) - 0.5) * 0.2
    dy = (np.random.rand(num_points) - 0.5) * 0.2
    x2 = np.clip(x2 + dx, 0, 10)
    y2 = np.clip(y2 + dy, 0, 10)
    scat2.set_offsets(np.c_[x2, y2])
    return scat2,

ani2 = FuncAnimation(fig2, update_particulas, frames=100, init_func=init_particulas, blit=True, interval=50)
ani2.save("animacion/particulas_aleatorias.gif", writer="pillow", fps=20)
plt.close(fig2)

# ============================
# 3. Círculo girando
# ============================
# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Círculo Girando")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)

# Crear línea y punto
line, = ax.plot([], [], lw=2, color='blue')  # Línea de trayectoria
point, = ax.plot([], [], 'ro')  # Punto rojo

# Variables para almacenar la trayectoria
trayectoria_x = []
trayectoria_y = []

# Inicialización
def init_circulo():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# Actualización por frame
def update_circulo(frame):
    t = frame / 10
    x = np.cos(t)
    y = np.sin(t)
    trayectoria_x.append(x)
    trayectoria_y.append(y)
    line.set_data(trayectoria_x, trayectoria_y)
    point.set_data([x], [y])  # <- convertir escalar a lista
    return line, point

# Crear animación
ani3 = FuncAnimation(fig, update_circulo, frames=100, init_func=init_circulo, blit=True, interval=50)

# Crear carpeta si no existe
import os
os.makedirs("animacion", exist_ok=True)

# Guardar animación
ani3.save("animacion/circulo_girando.gif", writer="pillow", fps=20)

# Mostrar (opcional)
plt.show()