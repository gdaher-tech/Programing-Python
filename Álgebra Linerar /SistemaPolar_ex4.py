import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc  # ← IMPORTAÇÃO CORRETA

# Coordenadas polares
r = 2
theta = np.pi / 3  # 60 graus

# Conversão para coordenadas cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)

# Criar gráfico cartesiano com elementos visuais de coordenadas polares
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# Eixos
ax.axhline(0, color='gray', lw=0.8)
ax.axvline(0, color='gray', lw=0.8)

# Plotar o ponto resultante
ax.plot(x, y, 'ro', label=f"Ponto (r=2, θ=π/3)\n→ (x={x:.2f}, y={y:.2f})")

# Linha ligando o ponto à origem (representando o vetor polar)
ax.plot([0, x], [0, y], 'r--', alpha=0.6)

# Arco para representar o ângulo θ
arc = Arc((0, 0), 1, 1, angle=0, theta1=0, theta2=np.degrees(theta),
          color='blue', lw=1.5, linestyle='--')
ax.add_patch(arc)
ax.text(0.6, 0.1, "θ = π/3", color='blue')

# Legenda e título
ax.legend(loc='upper right')
ax.set_title("Representação de um ponto polar\nem um gráfico cartesiano")

plt.tight_layout()
plt.show()
