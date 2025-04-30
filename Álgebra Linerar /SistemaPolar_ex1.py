#%%
import numpy as np
import matplotlib.pyplot as plt

# Lista de pontos em coordenadas polares: (r, θ)
pontos_polares = [
    (1, 5 * np.pi / 4),        # (1, 5π/4)
    (2, 3 * np.pi),            # (2, 3π)
    (2, 2 * np.pi / 3),        # (2, 2π/3)
    (-3, 3 * np.pi / 4)        # (-3, 3π/4)
]

# Corrigir ponto com raio negativo (-r, θ) → (r, θ + π)
pontos_corrigidos = [
    (r if r >= 0 else -r, theta if r >= 0 else theta + np.pi)
    for r, theta in pontos_polares
]

# Criar figura polar
plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)

# Plotar os pontos
for i, (r, theta) in enumerate(pontos_corrigidos):
    ax.plot(theta, r, 'o', label=f'Ponto {chr(97 + i)})')  # chr(97) = 'a'

# Personalização
ax.set_rmax(4)
ax.set_rticks([1, 2, 3, 4])
ax.set_theta_zero_location("E")
ax.set_theta_direction(-1)
ax.set_title("Pontos em Coordenadas Polares - Exemplo 1", va='bottom')
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=2)

plt.tight_layout()
plt.show()




