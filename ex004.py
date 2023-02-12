x=input('Digite qualquer coisa: ')


print('O dado é Alfanumérico?', x.isalnum())
print('O dado é Alfabético?', x.isalpha())
print('O dado é numérico?', x.isnumeric())
print('O dado possui espaços?', x.isspace())
print('O dado está em maiúsculas?', x.isupper())
print('O dado está em minúsculas?', x.islower())
print('O dado está capitalizada?', x.istitle())
print('Qual o tipo de dado primitivo é?', type(x))