# Exemplo com int
a = 10
b = a
print("Antes")
print(a)
print(b)
b += 10
print("Depois")
print(a)
print(b)

if a == b:
    print("o valor é igual")
else:
    print("o valor é diferente")

if a is b:
    print("Os objetos sao o mesmo")
else:
    print("Sao objetos diferentes")


# Código problemático
a = {}
b = a
print("Antes")
print(a)
print(b)
b["chave"] = "Valor"
print("Depois")
print(a)
print(b)

if a == b:
    print("o valor é igual")
else:
    print("o valor é diferente")

if a is b:
    print("Os objetos sao o mesmo")
else:
    print("Sao objetos diferentes")
