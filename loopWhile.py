contador = 0
while (contador < 5):
    contador += 1
    print(contador)
    
nome = ""
while True:
    texto = input("Digite um nome ou '0' para encerrar ")
    
    if(texto == "0"):
        print("programa finalizado ")
        break
    
    else: 
        nome = nome + texto + "\n"
        
print(nome)

nome = ""
continuar = True
while continuar: 
    nome = nome + input("Digite um nome ") + "\n"
    
    x = input("Deseja continuar? Digite 'sim' ou 'não' ")
    
    if(x.upper() == "SIM"):
        continuar = True
    else: 
        continuar = False

print(nome)