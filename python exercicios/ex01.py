l=[]
while True:
    numero=int(input("digite o numero: "))
    if numero not in l:
        l.append(numero)
    op=str(input("deseja continuar [S/N] :")).upper()
    while op not in ["S",'N']:
        op = str(input("deseja continuar [S/N] :")).upper()
    if op == "N":
        break
print(sorted(l))