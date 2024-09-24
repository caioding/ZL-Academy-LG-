from flask import Flask, make_response, jsonify, request, Response
import sys
import os

modulo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'repository'))
sys.path.append(modulo)

# import usuario 
import produto

# Instanciar 
app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# Implementar a lógica de programação

# -- Inicio: Serviços da api usuário ---------------------
# Serviço: Obter a lista de usuário
# @app_api.route('/usuario', methods=['GET'])
# def get_lista_usuarios():
#     lista_usuario = list()
#     lista_usuario = usuario.lista_usuarios()
#     if len(lista_usuario) == 0:
#         sucesso = False 
#         _mensagem = 'Lista de usuario vazia'
#     else:
#         sucesso = True
#         _mensagem = 'Lista de usuario'

#     # Construir um Response
#     return make_response(
#         # Formata a resposta no formato JSON
#         jsonify(
#                 status = sucesso, 
#                 mensagem = _mensagem,
#                 dados = lista_usuario
#         )
#     )

# # Serviço: Obter a lista de usuário
# @app_api.route('/usuario/<int:id>', methods=['GET'])
# def get_obter_usuario_id(id):
#     usuario_id = list()
#     usuario_id = usuario.obter_usuario_id(id)
#     if len(usuario_id) == 0:
#         sucesso = False
#         _mensagem = 'Usuario nao cadastrado'
#     else:
#         sucesso = True
#         _mensagem = 'Usuario cadastrado'

#     # Construir um Response
#     return make_response(
#         # Formata a resposta no formato JSON
#         jsonify(
#                 status = sucesso, 
#                 mensagem = _mensagem,
#                 dados = usuario_id
#         )
#     )

# @app_api.route('/usuario', methods=['POST'])
# def criar_usuario():
#     # Construir um Request
#     # Captura o JSON com os dados enviado pelo cliente
#     usuario_json = request.json # corpo da requisição
#     try:
#         id_usuario = usuario.criar_usuario(usuario_json)
#         sucesso = True
#         _mensagem = 'Usuario inserido com sucesso'
#     except Exception as ex:
#         sucesso = False
#         _mensagem = f'Erro: Inclusão do usuario: {ex}'
    
#     return make_response(
#         # Formata a resposta no formato JSON
#         jsonify(
#                 status = sucesso,
#                 mensagem = _mensagem ,
#                 id = id_usuario
#         )
#     )

# @app_api.route('/usuario', methods=['PUT'])
# def atualizar_usuario():
#     # Construir um Request
#     # Captura o JSON com os dados enviado pelo cliente
#     usuario_json = request.json # corpo da requisição
#     try:
#         usuario.atualizar_usuario(usuario_json)
#         sucesso = True
#         _mensagem = 'Usuario alterado com sucesso'
#     except Exception as ex:
#         sucesso = False
#         _mensagem = f'Erro: Alteração do usuario: {ex}'
    
#     return make_response(
#         # Formata a resposta no formato JSON
#         jsonify(
#                 status = sucesso,
#                 mensagem = _mensagem
#         )
#     )

# @app_api.route('/usuario/<int:id>', methods=['DELETE'])
# def deletar_usuario(id):
#     try:
#         usuario.deletar_usuario(id)
#         sucesso = True
#         _mensagem = 'Usuario deletado com sucesso'
#     except Exception as ex:
#         sucesso = False
#         _mensagem = f'Erro: Exclusão de usuario: {ex}'
    
#     return make_response(
#         # Formata a resposta no formato JSON
#         jsonify(
#                 status = sucesso,
#                 mensagem = _mensagem
#         )
#     )    

# -- Fim: Serviços da api usuário ---------------------

# -- Inicio : Serviços da api produto ---------------------

@app_api.route('/produto', methods=['POST'])
def criar_produto():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    produto_json = request.json # corpo da requisição
    id_produto=0
    try:
        id_produto = produto.criar_produto(produto_json)
        sucesso = True
        _mensagem = 'Produto inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusao do produto: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem ,
                id = id_produto
        )
    )

@app_api.route('/produto', methods=['PUT'])
def atualizar_produto():
    produto_json = request.json # corpo da requisição
    try:
        produto.atualizar_produto(produto_json)
        sucesso = True
        _mensagem = 'produto alterado com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Alteração do produto: {ex}'
    
    return make_response(
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )

@app_api.route('/produto', methods=['GET'])
def lista_produto():
    lista_produto = list()
    lista_produto = produto.lista_produto()
    if len(lista_produto) == 0:
        sucesso = False
        _mensagem = 'Lista de produto vazia'
    else:
        sucesso = True
        _mensagem = 'Lista de produto'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = lista_produto
        )
    )

@app_api.route('/produto/<int:id>', methods=['GET'])
def get_obter_produto_id(id):
    produto_id = list()
    produto_id = produto.obter_produto_id(id)
    if len(produto_id) == 0:
        sucesso = False
        _mensagem = 'produto nao cadastrado'
    else:
        sucesso = True
        _mensagem = 'produto cadastrado'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = produto_id
        )
    )

@app_api.route('/produto/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    try:
        produto.deletar_produto(id)
        sucesso = True
        _mensagem = 'produto deletado com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Exclusão de produto: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    ) 
   
# -- Fim : Serviços da api produtos ---------------------

# Levantar/Executar API REST: api_database
app_api.run()