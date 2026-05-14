lista=[]
man=men=0
for list in range(0,5):
    lista.append( int(input(f"digite um numero nessa posicao {list}: ")))
    if list==0:
        man=men=lista[list]
    else:
        if lista[list] > man:
            man=lista[list]
        if lista[list]< men:
            men=lista[list]

print(lista)
print(f"o maior numero:{man}")
print(f"o menor numero: {men}")erth

