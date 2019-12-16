from flask_restful import Resource
from flask import request
from model.bebida import Bebida
from dao.bebida_dao import BebidaDao

class BebidaController(Resource):
    def __init__(self):
        self.dao = BebidaDao()

    def get(self, id=None):
        if id:
            return self.dao.buscar_por_id(id)
        else:
            return self.dao.listar()            

    def post(self):
        nome = request.json['nome']
        teor = request.json['teor']
        tipo_bebida = request.json['tipo_bebida']
        bebida = Bebida(nome, teor, tipo_bebida)
        self.dao.inserir(bebida)
        return 'Salvo'
    
    def delete(self, id):        
        self.dao.deletar(id)
        return 'Deletado'
    
    def put(self, id):
        nome = request.json['nome']
        teor = request.json['teor']
        tipo_bebida = request.json['tipo_bebida']
        bebida = Bebida(nome, teor, tipo_bebida, id) 
        self.dao.alterar(bebida)
        return 'Alterado'