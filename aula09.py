pt = int(input('Primeiro termo: '))
qt = int(input('Quantidade de termos: '))
r = int(input('Razão: '))
s = 0
for y in range(pt, qt + 1, r):
  s += y
print(s)
