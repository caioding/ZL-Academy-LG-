from repository import database


# Inserir eleitor
def criar_eleitor(eleitor):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = (
            f"INSERT INTO eleitor(cpf, nome, data_nascimento, nome_mae, nro_titulo, situacao, secao, zona, local_votacao, endereço, bairro, municipio_uf, pais) "
            " VALUES('{eleitor['cpf']}','{eleitor['nome']}', '{eleitor['data_nascimento']}', '{eleitor['nome_mae']}','{eleitor['nro_titulo']}', "
            " '{eleitor['situacao']}', '{eleitor['secao']}','{eleitor['zona']}','{eleitor['local_votacao']}','{eleitor['endereço']}','{eleitor['bairro']}', "
            " '{eleitor['municipio_uf']}','{eleitor['pais']}' )"
        )
        
        print(sql)
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: criar_eleitor(produto)