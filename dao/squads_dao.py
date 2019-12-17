import sys
sys.path.append("C:/Users/900223/Desktop/apiSquads")


from dao.base_dao import BaseDao
from model.squads import Squads
from model.programador import Programador
from model.linguagem import Linguagem
from model.framework import Framework
from model.banco_dados import BancoDados


class SquadsDao(BaseDao):
    def inserir(self, prog:Programador, ling:Linguagem, frame:Framework, banco:BancoDados):
        comando_sql_insert = f"""INSERT INTO squads 
                                (id, programador, linguagem, framework, banco_dados ) VALUES (
                                DEFAULT,                                
                                '{prog.get_id_prog()}',
                                '{ling.get_id_ling()}',
                                '{frame.get_id_frame()}',
                                '{banco.get_id_banco()}')"""

        super().inserir(comando_sql_insert)


    def alterar(self, squads:Squads, prog=Programador, ling=Linguagem, frame=Framework, banco=BancoDados):
        comando_sql_alterar = f"""UPDATE squads SET 
                                programador = '{prog.get_id_prog()}',
                                linguagem = '{ling.get_id_ling()}',
                                framework = '{frame.get_id_frame()}',
                                banco_dados = '{banco.get_id_banco()}'
                                WHERE id = {squads.get_id_squad()}"""

        super().alterar(comando_sql_alterar)


    def deletar(self, id):
        comando_sql_deletar = f"DELETE FROM squads WHERE id = {id}"
        super().deletar(comando_sql_deletar)


    def listar(self):
        listas_squads = []
        comando_sql_listar = "SELECT programador, linguagem, framework, banco_dados, id FROM squads"                                
        lista_tuplas = super().listar(comando_sql_listar)
        for l in lista_tuplas:
            p = Squads(l[0], l[1], l[2], l[3], l[4])
            listas_squads.append(p.__dict__)
        return listas_squads


    def buscar_por_id(self, id):
        lista_squads = []
        comando_sql_buscar_id = f"SELECT programador, linguagem, framework, banco_dados, id FROM squads where id= {id}"                                
        tupla = super().buscar_por_id(comando_sql_buscar_id)
        p = Squads(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
        lista_squads.append(p.__dict__)
        return lista_squads
