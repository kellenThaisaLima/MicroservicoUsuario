from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

usuarios_db = [
    {'ID':0,'CPF':'98605322063','NOME':'Fabiana Aparecida Brito','DATA_DE_NASCIMENTO':'27/06/1988','DATA_DE_CRIACAO':'21/12/2021','DATA_DE_ATUALIZACAO':'22/12/2021'},
    {'ID':1,'CPF':'70977747972','NOME':'Aparecida Bianca Assis' ,'DATA_DE_NASCIMENTO':'25/04/1967','DATA_DE_CRIACAO':'21/12/2021','DATA_DE_ATUALIZACAO':'22/12/2021'},
    {'ID':2,'CPF':'13737146977','NOME':'Fernanda Gabriela Pinto','DATA_DE_NASCIMENTO':'17/08/1971','DATA_DE_CRIACAO':'21/12/2021','DATA_DE_ATUALIZACAO':'22/12/2021'}     
]

@api.route('/usuarios')
class ListaDeUsuarios(Resource):
    def get(self, ):
        return usuarios_db