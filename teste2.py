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
except:
    print("Ocorreu erro no banco de dados")
