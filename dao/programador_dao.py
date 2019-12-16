import sys
sys.path.append("C:/Users/900217/Desktop/AulasPythonClt2/Aula10/")

from dao.base_dao import BaseDao
from model.programador import Programador


class ProgramadorDao(BaseDao):
    def inserir(self, programador:Programador):
        comando_sql_insert = f"INSERT INTO programador (id, nome_prog) VALUES (DEFAULT '{programador.get_nome_prog()}')"
        super().inserir(comando_sql_insert)


    def alterar(self, programador:Programador):
        comando_sql_alterar = f"UPDATE programador SET nome_prog = '{programador.get_nome_prog()}' WHERE id = {programador.get_id_prog()}"
        super().alterar(comando_sql_alterar)
    

    def deletar(self, id):
        comando_sql_deletar = f"DELETE FROM programador WHERE id = {id}"
        super().deletar(comando_sql_deletar)


    def listar(self):
        lista_programadores = []
        comando_sql_listar = "SELECT nome_prog, id FROM programador"                                
        lista_tuplas = super().listar(comando_sql_listar)
        for l in lista_tuplas:
            p = Programador(l[0], l[1])
            lista_programadores.append(p.__dict__)
        return lista_programadores


    def buscar_por_id(self, id):
        lista_squads = []
        comando_sql_buscar_id = f"SELECT nome_prog, id FROM programador where id= {id}"                                
        tupla = super().buscar_por_id(comando_sql_buscar_id)
        p = Programador(tupla[0], tupla[1])
        lista_squads.append(p.__dict__)
        return lista_squads

        