import database 

# Verificar se Produto existe
def exist_product(id):
    exist: False
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM produto WHERE id = '{id}'"
        cursor.execute()
        list_product = cursor.fetchall()
        if len(list_product) == 0:
            exist = False
        else:
            exist = True
    except Exception as ex:
        print(f'Erro na verificacao do produto: {ex}')
    finally:
        cursor.close()
        conect.close()
    
    return exist

# Criar produto
def create_product(produto):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f"INSERT INTO produto(descricao, unidade, quantidade, preco_real, preco_dolar) VALUES('{produto['descricao']}','{produto['unidade']}', '{produto['quantidade']}', '{produto['preco_real']}','{produto['preco_dolar']}')"
        print(sql)
        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão: {ex}')
    finally:
        cursor.close()
        conect.close()

    return last_id 