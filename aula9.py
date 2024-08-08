a = int(input('Digite um número inteiro: '))
b = int(input('Digite um número inteiro: '))
soma = 0
if a < b:
  for y in range(a, b):
    soma += y
  print(soma)
else:
  print('erro!')
