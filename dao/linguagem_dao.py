import sys
sys.path.append("C:/Users/900217/Desktop/AulasPythonClt2/Aula10/")

from dao.base_dao import BaseDao
from model.linguagem import Linguagem


class LinguagemDao(BaseDao):
    def inserir(self, linguagem:Linguagem):
        comando_sql_insert = f"INSERT INTO linguagem (id, nome_ling) VALUES (DEFAULT '{linguagem.nome_ling}')"
        super().inserir(comando_sql_insert)


    def alterar(self, linguagem:Linguagem):
        comando_sql_alterar = f"UPDATE linguagem SET nome_ling = '{linguagem.nome_ling}' WHERE id = {linguagem.id_ling}"
        super().alterar(comando_sql_alterar)
    

    def deletar(self, id):
        comando_sql_deletar = f"DELETE FROM linguagem WHERE id = {id}"
        super().deletar(comando_sql_deletar)


    def listar(self):
        lista_linguagens = []
        comando_sql_listar = "SELECT nome_ling, id FROM linguagem"                                
        lista_tuplas = super().listar(comando_sql_listar)
        for l in lista_tuplas:
            p = Linguagem(l[0], l[1])
            lista_linguagens.append(p.__dict__)
        return lista_linguagens


    def buscar_por_id(self, id):
        lista_linguagens = []
        comando_sql_buscar_id = f"SELECT nome_ling, id FROM linguagem where id= {id}"                                
        tupla = super().buscar_por_id(comando_sql_buscar_id)
        p = Linguagem(tupla[0], tupla[1])
        lista_linguagens.append(p.__dict__)
        return lista_linguagens