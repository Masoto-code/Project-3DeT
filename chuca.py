import mysql.connector

# Configurando a conexão com o banco de dados
configuracao = {
    'host': 'localhost',      # ou o endereço IP do seu servidor
    'user': 'seu_usuario',    # ex: root
    'password': 'sua_senha',  # sua senha do MySQL
    'database': 'seu_banco'   # nome do banco de dados que deseja acessar
}

try:
    # Estabelecendo a conexão
    conexao = mysql.connector.connect(**configuracao)
    
    if conexao.is_connected():
        print("Conexão estabelecida com sucesso!")
        
        # Criando o cursor para executar comandos SQL
        cursor = conexao.cursor()
        
        # Exemplo: Executando uma consulta simples
        cursor.execute("SELECT DATABASE()")
        linha = cursor.fetchone()
        print(f"Você está conectado ao banco de dados: {linha[0]}")

except mysql.connector.Error as erro:
    print(f"Erro ao conectar ao MySQL: {erro}")

finally:
    # Fechando a conexão e o cursor
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada.")
