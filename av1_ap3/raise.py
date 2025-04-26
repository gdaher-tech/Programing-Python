# Levantando exceções com raise

# Exemplo 1 – Gerar um erro se x for menor que 0
x = -1
if x < 0:
    raise Exception("Erro: x não pode ser menor que 0")

# Diferença entre TypeError e ValueError

# TypeError – tipo errado (ex: string onde se espera int)
int("abc")  # TypeError

# ValueError – valor inválido (tipo certo, valor errado)
int("12.3")  # ValueError

# Como usar raise com TypeError e ValueError
def validar_x(x):
    if not isinstance(x, int):
        raise TypeError("x deve ser do tipo int")
    if x < 0:
        raise ValueError("x deve ser maior ou igual a 0")
