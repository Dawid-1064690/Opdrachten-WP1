import math

x = 9.1
term1 = (3 * x) - 1
term2 = 1 + x
term3 = (term2)**2

y = math.sqrt(term1) + (term3)

print(f'De waarde van y={y} als x = {x}')


a = 0.87
b = 22.7
c = 5.03
term4 = (b ** 2) - (4 * a * c)
term5 = 2 * a
term6 = -b
term7 = -b + (math.sqrt(term4))

y1 = term7 / term5
print(f'De waarde van y1 = {y1} als a = {a}, b = {b} en c = {c}')