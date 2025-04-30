#%%
import numpy as np
import matplotlib.pyplot as plt

# Representações polares equivalentes do mesmo ponto
representacoes = [
    (1, 5 * np.pi / 4),
    (1, 13 * np.pi / 4),
    (1, -3 * np.pi / 4),
    (-1, np.pi / 4)
]

# Corrigir representações:
# - Se r < 0, invertemos r e somamos pi ao ângulo
# - Normalizamos os ângulos para o intervalo [0, 2π] para melhor visualização
pontos_corrigidos = []
for r, theta in representacoes:
    if r < 0:
        r = -r
        theta += np.pi
    theta = theta % (2 * np.pi)  # normaliza para entre 0 e 2π
    pontos_corrigidos.append((r, theta))

# Criar gráfico polar
plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)

# Plotar os pontos com marcação visível
for i, (r, theta) in enumerate(pontos_corrigidos):
    ax.plot(theta, r, 'o', label=f'Rep. {chr(97 + i)})')  # a), b), c), d)

# Configurações visuais
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_theta_zero_location("E")
ax.set_theta_direction(-1)
ax.set_title("Múltiplas Representações do Mesmo Ponto", va='bottom')
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=2)

plt.tight_layout()
plt.show()
