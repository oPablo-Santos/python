qtdValores = int(input("Digite a quantidade de valores que serão calculados "))
contador = 0
valor = 0
while contador < qtdValores:
    valor += float(input("Digite um valor "))
    contador += 1
    
media = valor/ contador
print(media)