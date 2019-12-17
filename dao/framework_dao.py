import sys
sys.path.append("C:/Users/900217/Desktop/AulasPythonClt2/Aula10/")

from dao.base_dao import BaseDao
from model.framework import Framework


class FrameworkDao(BaseDao):
    def inserir(self, framework:Framework):
        comando_sql_insert = f"INSERT INTO framework (id, nome_frame) VALUES (DEFAULT,'{framework.get_nome_frame()}')"
        super().inserir(comando_sql_insert)


    def alterar(self, framework:Framework):
        comando_sql_alterar = f"UPDATE framework SET nome_frame = '{framework.get_nome_frame()}'WHERE id = {framework.get_id_frame()}"
        super().alterar(comando_sql_alterar)

    
    def deletar(self, id):
        comando_sql_deletar = f"DELETE FROM framework WHERE id = {id}"
        super().deletar(comando_sql_deletar)


    def listar(self):
        lista_frameworks = []
        comando_sql_listar = "SELECT nome_frame, id FROM framework"                                
        lista_tuplas = super().listar(comando_sql_listar)
        for l in lista_tuplas:
            p = Framework(l[0], l[1])
            lista_frameworks.append(p.__dict__)
        return lista_frameworks


    def buscar_por_id(self, id):
        lista_frameworks = []
        comando_sql_buscar_id = f"SELECT nome_frame, id FROM framework where id= {id}"                                
        tupla = super().buscar_por_id(comando_sql_buscar_id)
        p = Framework(tupla[0], tupla[1])
        lista_frameworks.append(p.__dict__)
        return lista_frameworks