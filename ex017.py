from math import hypot
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
hi = hypot(c1,c2)
print('A hipotenusa mede {:.2f}'.format(hi))



c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
hi = (c1**2 + c2**2) **(1/2)
print('A hipotenusa mede {:.2f}'.format(hi))