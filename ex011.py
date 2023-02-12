l=float(input('Digite a largura em metros: '))
a=float(input('Digite a altura em metros: '))

area=a*l
t= area/2

print('A área da parede é de {:.2f}m² e serão necessários {:.2f} litros de tinta'.format(area, t))