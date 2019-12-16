import sys
sys.path.append("C:/Users/900223/Desktop/apiSquads")


from dao.base_dao import BaseDao
from model.squads import Squads
from model.programador import Programador
from model.linguagem import Linguagem
from model.framework import Framework
from model.banco_dados import BancoDados

class SquadsDao(BaseDao):
    def inserir(self, squads:Squads, prog=Programador, ling=Linguagem, frame=Framework, banco=BancoDados):
        comando_sql_insert = f"""INSERT INTO SQUADS 
                                (ID, PROGRAMADOR, LINGUAGEM, FRAMEWORK, BANCO_DADOS ) VALUES (
                                DEFAULT,
                                '{squads.get_id_()}',
                                '{prog.get_id_prog()}',
                                '{ling.get_id_ling()}',
                                '{frame.get_id_frame()}',
                                '{banco.get_id_banco()}')"""

        super().inserir(comando_sql_insert)


    def alterar(self, squads:Squads, prog=Programador, ling=Linguagem, frame=Framework, banco=BancoDados):
        comando_sql_alterar = f"""UPDATE SQUADS SET 
                                PROGRAMADOR = '{prog.get_id_prog()}',
                                LINGUAGEM = '{ling.get_id_ling()}',
                                FRAMEWORK = '{frame.get_id_frame()}',
                                BANCO_DADOS = '{banco.get_id_banco()}'
                                WHERE ID = {squads.get_id_squad()}"""

        super().alterar(comando_sql_alterar)


    def deletar(self, id):
        comando_sql_deletar = f"DELETE FROM SQUADS WHERE ID = {id}"
        super().deletar(comando_sql_deletar)


    def listar(self):
        lista_squads = []
        comando_sql_listar = "SELECT PROGRAMADOR, LINGUAGEM, FRAMEWORK, BANCO_DADOS FROM SQUADS"                                
        lista_squads = super().listar(comando_sql_listar)
        return lista_squads


    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"SELECT PROGRAMADOR, LINGUAGEM, FRAMEWORK, BANCO_DADOS FROM SQUADS WHERE ID = {id}"
        dados = super().buscar_por_id(comando_sql_buscar_id)
        return dados.__dict__