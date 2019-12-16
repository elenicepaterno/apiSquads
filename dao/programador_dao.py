import sys
sys.path.append("C:/Users/900217/Desktop/AulasPythonClt2/Aula10/")

from dao.base_dao import BaseDao
from model.programador import Programador


class ProgramadorDao(BaseDao):
    def inserir(self, programador:Programador):
        comando_sql_insert = f"INSERT INTO PROGRAMADOR (ID, NOME) VALUES (DEFAULT '{programador.get_nome_prog()}')"
        super().inserir(comando_sql_insert)


    def alterar(self, programador:Programador):
        comando_sql_alterar = f"UPDATE PROGRAMADOR SET NOME = '{programador.get_nome_prog()}' WHERE ID = {programador.get_id_prog()}"
        super().alterar(comando_sql_alterar)
    

    def deletar(self, id):
        comando_sql_deletar = f"DELETE FROM PROGRAMADOR WHERE ID = {id}"
        super().deletar(comando_sql_deletar)


    def listar(self):
        lista_programadores = []
        comando_sql_listar = "SELECT NOME_PROG FROM PROGRAMADOR"                                
        lista_programadores = super().listar(comando_sql_listar)
        return lista_programadores


    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"SELECT NOME_PROG FROM PROGRAMADOR WHERE ID = {id}"
        dados = super().buscar_por_id(comando_sql_buscar_id)
        return dados