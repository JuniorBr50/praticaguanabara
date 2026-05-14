import mysql.connector

# Conexão com o seu Laragon
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'graobr'
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n" + "="*30)
    print("   CAIXA RÁPIDO - GRAOBR")
    print("="*30)

    # 1. Entrada de dados
    produto = input("O que o cliente comprou? ")
    quantidade = int(input(f"Quantos sacos de {produto}? "))

    # 2. Verificar se tem no estoque ANTES de vender
    cursor.execute("SELECT quantidade, preco_custo, preco_venda FROM estoque_graobr WHERE nome = %s", (produto,))
    resultado = cursor.fetchone()

    if resultado:
        estoque_atual, custo, venda = resultado

        if estoque_atual >= quantidade:
            # 3. Calcular Lucro da Venda
            lucro_venda = (venda - custo) * quantidade
            novo_estoque = estoque_atual - quantidade

            # 4. Atualizar o Banco de Dados
            sql_update = "UPDATE estoque_graobr SET quantidade = %s WHERE nome = %s"
            cursor.execute(sql_update, (novo_estoque, produto))
            db.commit()

            print(f"\n✅ VENDA CONCLUÍDA!")
            print(f"💰 Lucro nesta operação: R$ {lucro_venda:.2f}")
            print(f"📦 Estoque atual de {produto}: {novo_estoque} unidades.")
        else:
            print(f"\n❌ ESTOQUE INSUFICIENTE! Você só tem {estoque_atual} unidades.")
    else:
        print("\n❌ PRODUTO NÃO ENCONTRADO! Verifique se digitou o nome certo.")

except mysql.connector.Error as err:
    print(f"Erro no banco: {err}")
finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()