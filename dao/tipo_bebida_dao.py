import sys
sys.path.append("C:/Users/900217/Desktop/AulasPythonClt2/Aula10/")

from dao.base_dao import BaseDao
from model.bebida import Bebida
from model.tipo_bebida import TipoBebida

class TipoBebidaDao(BaseDao):
    def inserir(self, tipo_bebida:TipoBebida):
        comando_sql_insert = f"""INSERT INTO TIPO_BEBIDA (ID, NOME, DESCRICAO) VALUES
                             (DEFAULT, '{tipo_bebida.get_nome()}',
                             '{tipo_bebida.get_descricao()}')"""

        super().inserir(comando_sql_insert)

    def alterar(self, tipo_bebida: TipoBebida):
        comando_sql_alterar = f"""UPDATE TIPO_BEBIDA SET
                              NOME = '{tipo_bebida.get_nome()}',
                              DESCRICAO = '{tipo_bebida.get_descricao()}'
                              WHERE ID = {tipo_bebida.get_id_tipo_bebida()}"""
    
        super().alterar(comando_sql_alterar)

    def deletar(self, id):
        comando_sql_deletar = f"DELETE FROM TIPO_BEBIDA WHERE ID = {id}"
        super().deletar(comando_sql_deletar)
    
    def listar(self):
        lista_tipo_bebidas = []
        comando_sql_listar = "SELECT ID, NOME, DESCRICAO FROM TIPO_BEBIDA"

        lista_tuplas = super().listar(comando_sql_listar)
        
        for l in lista_tuplas:
            tipo_bebida = TipoBebida(l[1], l[2], l[0])
            lista_tipo_bebidas.append(tipo_bebida.__dict__)
        return lista_tipo_bebidas

    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"SELECT ID, NOME, DESCRICAO FROM TIPO_BEBIDA WHERE ID = {id}"

        dados = super().buscar_por_id(comando_sql_buscar_id)
        tipo_bebida = TipoBebida(dados[1], dados[2], dados[0])
        return tipo_bebida.__dict__   
                         