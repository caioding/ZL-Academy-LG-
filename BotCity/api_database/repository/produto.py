import database 

# Verificar se Produto existe
def exist_product(id):
    exist: False
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM product WHERE id = '{id}'"
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
def create_product(product):
    try:
        # Manipular o banco de dados
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"INSERT INTO product(descricao, unidade, quantidade, preco_real, preco_dolar) VALUES('{product['descricao']}','{product['unidade']}', '{product['quantidade']}', '{product['preco_real']}','{product['preco_dolar']}')"
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

# Lista de produtos
def list_products():
    products = list()
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = 'SELECT * FROM product ORDER BY descricao'
        cursor.execut(sql)
        list_product = cursor.fetchall()
        # Tratar dados para uma estrutura JSON
        for product in list_product:
            products.append(
                {
                  'id': product[0],
                  'descricao': product[1],
                  'unidade': product[2],
                  'quantidade': product[3],
                  'preco_real': product[4],
                  'preco_dolar': product[5]
                }
            )
    except Exception as ex:
        print(f'Erro: Listar usuario: {ex}')
    finally:
        cursor.close()
        conect.close()
    
    return products

# Obter produto por id
def get_product_id(id):
    products = list()
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM product WHERE id = '{id}'"
        cursor.execute(sql)
        list_products = cursor.fetchall()
        # Tratar dados para uma estrutura JSON
        for product in list_products:
            product.append(
                {
                  'id': product[0],
                  'descricao': product[1],
                  'unidade': product[2],
                  'quantidade': product[3],
                  'preco_real': product[4],
                  'preco_dolar': product[5]
                }
            )
    except Exception as ex:
        print(f'Erro: obter produto pelo id: {ex}')
    
    return products

# Atualizar produto
def update_product(product):
    try:
        # Manipular Banco de Dados
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"UPDATE product SET descricao = '{product['descricao']}', unidade = '{product['unidade']}', quantidade = '{product['quantidade']}', preco_real = '{product['preco_real']}', preco_dolar = '{product['preco_dolar']}' WHERE id = '{product['id']}' "
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na atualização: {ex}')

# Deletar produto
def delete_product(id):
    try:
        # Manipular o banco de dados
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM product WHERE id = {id}'
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha em deletar produto: {ex}')
        