ListaNome = []

while True:
    nome = input("Digite um nome ")
    ListaNome.append(nome)
    
    continuar = input("Deseja continuar? Digite sim ou nao ")
    if(continuar == "não" or continuar == "Não"):
        break
    
print(ListaNome)

for elementos in ListaNome:
    print(elementos)