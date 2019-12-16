import sys
sys.path.append("C:/Users/900217/Desktop/AulasPythonClt2/Aula10/")

from dao.base_dao import BaseDao
from model.framework import Framework

class FrameworkDAO(BaseDao):
    def inserir(self, framework:framework):
        comando_sql_insert = f"INSERT INTO FRAMEWORK (ID, NOME_LING) VALUES (DEFAULT,'{framework.get_nome_ling()}')"
        super().inserir(comando_sql_insert)

    def alterar(self, framework:framework):
        comando_sql_alterar = f"UPDATE FRAMEWORK SET NOME_LING = '{framework.get_nome_ling()}'WHERE ID = {framework.get_nome_ling()}"
        super().alterar(comando_sql_alterar)
    
    def deletar(self, id):
        comando_sql_deletar = f"DELETE FROM FRAMEWORK WHERE ID = {id}"
        super().deletar(comando_sql_deletar)

    def listar(self):
        lista_framework = []
        comando_sql_listar = "SELECT NOME_LING FROM FRAMEWORK"           
        lista_framework = super().listar(comando_sql_listar)
        return lista_framework

    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"SELECT NOME_LING FROM FRAMEWORK WHERE ID = {id}"

        dados = super().buscar_por_id(comando_sql_buscar_id)
        return dados.__dict__