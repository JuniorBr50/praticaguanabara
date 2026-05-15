l=[]
while True:
    l.append(int(input("digite um numero: ")))
    op=str(input("quer continuar[S/N]: ")).upper().strip()
    while op not in ["S","N"]:
        print("digite apenas s ou n")
        op = str(input("quer continuar[S/N]: ")).upper().strip()
    if op== "N":
        break

print(l)