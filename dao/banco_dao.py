import sys
sys.path.append("C:/Users/900217/Desktop/AulasPythonClt2/Aula10/")

from dao.base_dao import BaseDao
from model.banco_dados import BancoDados


class BancoDao(BaseDao):
    def inserir(self, banco:BancoDados):
        comando_sql_insert = f"INSERT INTO BANCO_DADOS (ID, NOME_BANCO) VALUES (DEFAULT,'{banco.get_nome_banco()}')"
        super().inserir(comando_sql_insert)


    def alterar(self, banco:BancoDados):
        comando_sql_alterar = f"UPDATE BANCO_DADOS SET NOME_BANCO = '{banco.get_nome_banco()}'WHERE ID = {banco.get_id_banco()}"
        super().alterar(comando_sql_alterar)

    
    def deletar(self, id):
        comando_sql_deletar = f"DELETE FROM BANCO_DADOS WHERE ID = {id}"
        super().deletar(comando_sql_deletar)


    def listar(self):
        lista_bancos_dados = []
        comando_sql_listar = "SELECT nome_banco, id FROM banco_dados"                                
        lista_tuplas = super().listar(comando_sql_listar)
        for l in lista_tuplas:
            p = BancoDados(l[0], l[1])
            lista_bancos_dados.append(p.__dict__)
        return lista_bancos_dados


    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"SELECT NOME_BANCO FROM BANCO_DADOS WHERE ID = {id}"
        dados = super().buscar_por_id(comando_sql_buscar_id)
        return dados.__dict__