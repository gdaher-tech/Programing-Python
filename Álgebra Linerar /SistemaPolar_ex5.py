import numpy as np

# Ponto cartesiano
x = -1
y = np.sqrt(3)

# Conversão incorreta usando apenas arctan
theta_errada = np.arctan(y / x)  # Pode estar no quadrante errado

# Conversão correta usando atan2
theta_certa = np.arctan2(y, x)

# Cálculo do raio
r = np.sqrt(x**2 + y**2)

# Exibição
print("=== Conversão de (x = -1, y = √3) para coordenadas polares ===")
print(f"Raio (r): {r:.2f}")
print(f"θ (usando arctan): {theta_errada:.2f} rad  → (pode estar errado)")
print(f"θ (usando atan2):  {theta_certa:.2f} rad  → (correto para o quadrante)")
print(f"θ em graus: {np.degrees(theta_certa):.2f}°")
