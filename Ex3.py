def fibonnaci(n):
  sequencia = []
  a, b = 0, 1
while len(sequencia) < n:
  sequencia.append(a)
  a, b = b, a + b
  return sequencia

n = 10

print(fibonnaci(n))
