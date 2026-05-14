estoque_graobr=[
    ["saco de milho",  65.00,100],["farelo de trigo",54.00,100],["sal branco",15.50,100],["sal fosbovi",125.94,150],["saco de cuim",43.50,65]
]
print("---RELATORIO DA GRAOBR---")
totalsoma=0
for item in estoque_graobr:
    nome=item[0]
    custo=item[1]
    qtd=item[2]

    soma_custo= custo*qtd
    totalsoma+=soma_custo
    print(f"produto {nome} | total investido R$:{soma_custo}")
print("-----------------------------")
print(f"valor total parado no estoque : {totalsoma}")