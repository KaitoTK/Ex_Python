from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que vc deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, tangente))
