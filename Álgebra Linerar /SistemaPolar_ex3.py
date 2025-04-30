import numpy as np
import matplotlib.pyplot as plt

# Definição do ponto em coordenadas polares
r = 2
theta = np.pi / 3  # 60 graus

# Conversão para coordenadas cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)

# Criar figura com dois gráficos lado a lado
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# === Gráfico 1: Sistema de Coordenadas Polares ===
polar_ax = fig.add_subplot(121, polar=True)
polar_ax.plot(theta, r, 'ro')  # ponto em vermelho
polar_ax.annotate(f"(r={r}, θ={round(np.degrees(theta))}°)",
                  xy=(theta, r), xytext=(theta + 0.2, r + 0.2),
                  arrowprops=dict(facecolor='black', arrowstyle="->"))
polar_ax.set_title("Sistema de Coordenadas Polares", va='bottom')

# === Gráfico 2: Sistema de Coordenadas Cartesianas ===
ax2 = axs[1]
ax2.set_aspect('equal')
ax2.grid(True)
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)
ax2.axhline(0, color='gray', lw=0.8)
ax2.axvline(0, color='gray', lw=0.8)
ax2.plot(x, y, 'bo')  # ponto em azul
ax2.annotate(f"(x={x:.2f}, y={y:.2f})",
             xy=(x, y), xytext=(x + 0.3, y + 0.3),
             arrowprops=dict(facecolor='black', arrowstyle="->"))
ax2.set_title("Sistema de Coordenadas Cartesianas")

# Layout final
plt.tight_layout()
plt.show()
