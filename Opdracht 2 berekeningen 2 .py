

t = 4
# v is in m/s
v = 179875474.8
# c is in m/s
c = 299_792_458

term1 = v**2
term2 = c**2
term3 = term1 / term2
term4 = 1 - term3
term5 = v * term4
term6 = 1 / term5


delta = t * term6
print(f'Vanaf een komeet gezien zit u {delta} uur op de tuinstoel')
print(f'Vanaf een komeet gezien zit u {delta * 60} minuten op de tuinstoel')
print(f'Vanaf een komeet gezien zit u {delta * 60 * 60} seconden op de tuinstoel')
