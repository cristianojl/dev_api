from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
    'id':'0',
    'nome':'Cristiano',
    'habilidades':['Python' , 'Django']
    },
    
    {
        'id':'1',
        'nome':'Lima',
        'habilidades':['Python','Django']
    }
]

# desenvolvedor pelo ID, tabém altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
                mensagem = 'Desenvolvedor de ID {} não existe.'.format(id)
                response = {'satus':'erro', 'mensagem': mensagem}
        except Exception:
                mensagem = 'Erro desconhecido. Procure o administrador da API'
                response = {'status':'erro', 'mensagem':mensagem}
        return response

    def put(Self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem': 'registro excluido'}

# Lista todos os desnvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores (Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)