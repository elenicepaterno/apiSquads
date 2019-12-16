import sys
sys.path.append("C:/Users/900217/Desktop/AulasPythonClt2/Aula10/")

from dao.base_dao import BaseDao
from model.linguagem import Linguagem


class LinguagemDao(BaseDao):
    def inserir(self, linguagem:Linguagem):
        comando_sql_insert = f"INSERT INTO LINGUAGEM (ID, NOME) VALUES (DEFAULT '{linguagem.get_nome_ling()}')"
        super().inserir(comando_sql_insert)


    def alterar(self, linguagem:Linguagem):
        comando_sql_alterar = f"UPDATE LINGUAGEM SET NOME = '{linguagem.get_nome_ling()}' WHERE ID = {linguagem.get_id_ling()}"
        super().alterar(comando_sql_alterar)
    

    def deletar(self, id):
        comando_sql_deletar = f"DELETE FROM LINGUAGEM WHERE ID = {id}"
        super().deletar(comando_sql_deletar)


    def listar(self):
        lista_linguagens = []
        comando_sql_listar = "SELECT ID, NOME_LING FROM LINGUAGEM"                                
        lista_linguagens = super().listar(comando_sql_listar)
        return lista_linguagens


    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"SELECT NOME_LING FROM LINGUAGEM WHERE ID = {id}"
        dados = super().buscar_por_id(comando_sql_buscar_id)
        return dados.__dict__