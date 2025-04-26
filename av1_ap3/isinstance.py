# Verificando tipos com isinstance()

# Exemplo 1: Verificando se x é inteiro
x = 5
print(isinstance(x, int))  # True
print(x)                   # 5

# Exemplo 2: Verificando diretamente ao definir a variável
y = isinstance(9.2, float)
print(y)  # True

# Exemplo 3: Verificando múltiplos tipos
z = "Olá"
print(isinstance(z, (float, int, bool)))         # False
print(isinstance(z, (float, int, bool, str)))    # True

# Exemplo 4: isinstance só aceita uma variável por vez
# Isso aqui daria erro:
# isinstance(var1, var2, var3, int)

# Exemplo 5: Verificando se um objeto é instância de uma classe
class MyObj:
    nome = "Jhon"

obj = MyObj()
print(isinstance(obj, MyObj))  # True
