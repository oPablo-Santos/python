soma = 0
for i in (0,1,2,3,4,5):
    soma = soma + 3
    print(soma)


for i in range(12):
    print(i)
    
for i in range(0, 15, 2):
    print(i)
    
    
qtdMutiplos = 0
for i in range(1, 31):
    if(i%3==0):
        qtdMutiplos += 1
        print(i)
        
print("A quantidade de numeros divisiveis por 3 é", qtdMutiplos)
        
        
minhaString = 'Pabblos'

for x in minhaString:
    print(x)