from flask import Flask
from flask.json import jsonify, request
import json

from werkzeug.wrappers import response


app = Flask (__name__)

desenvolvedores = [
    {
    'id':'0',
    'nome':'Cristiano',
    'habilidades':['Python' , 'Django']
    },
    
    {
        'id':'1',
        'nome':'Lima',
        'habilidades':['Python','Django']}
]
# desenvolvedor pelo ID, tabém altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
                mensagem = 'Desenvolvedor de ID {} não existe.'.format(id)
                response = {'satus':'erro', 'mensagem': mensagem}
        except Exception:
                mensagem = 'Erro desconhecido. Procure o administrador da API'
                response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
         dados = json.loads(request.data)
         desenvolvedores[id] = dados
         return jsonify(dados)
    elif request.method =='DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem': 'registro excluido'})

# Lista todos os desnvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method=='POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
    if __name__ == '__name__' :
        app.run (debug=True)
