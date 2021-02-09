from flask import request, Blueprint, jsonify
from app.servico.model import Servico
from app.extensions import db

servico_api = Blueprint('servico_api', __name__) # armazena as rotas

@servico_api.route('/servicos', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        servicos = Servico.query.all()   # pega todos os servicos

        return jsonify([servicos.json() for servico in servicos]), 200

    if (request.method == 'POST'):
        dados = request.json
        
        nome = dados.get('nome')
        horario = dados.get('horario')
        descricao = dados.get('descricao')

        if(not True):
            return {'erro' : 'servico, horario ou descrição inválidos'}
        
        servico = Servico(nome = nome, horario = horario, descricao = descricao )
        
        db.session.add(servico) # não salva ainda, apenas 'coloca na fila' para ser salvo

        db.session.commit() # salva no banco oq foi add na 'fila'

        return servico.json(), 200

    

'''
@servico_api.route('/servicos/<int:id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def pagina_servico(id):
    servico = Servico.query.get_or_404(id) #se existir o servico retorna os dados, caso contrário sai da função retornando 404

    if (request.method == 'GET'):
        return servico.json(), 200

    if (request.method == 'PATCH'):
        dados = request.json()

        nome = dados.get('servico', servico.nome) # 2º param -> oq acontece se não encontrar o parametro (nesse caso 'nome')
        horario = dados.get('horario', servico.horario)
        descricao = dados.get('descricao', servico.descricao)

    # verificar se peso e nome estão do jeito certo str//int, em tamanho apropriado...

    servico.nome = nome

    db.session.commit() # executa no banco todas as tarefas que estavam na fila
    return servico.json(), 200
'''