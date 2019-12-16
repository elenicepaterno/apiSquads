# import sys
# sys.path.append("C:/Users/900217/Desktop/AulasPythonClt2/Aula10/")

# from dao.base_dao import BaseDao
# from model.bebida import Bebida
# from model.tipo_bebida import TipoBebida


# class BebidaDao(BaseDao):
#     def inserir(self, bebida:Bebida):
#         comando_sql_insert = f"""INSERT INTO BEBIDA_FESTA (
#                                  ID, NOME, TEOR, TIPO_BEBIDA_ID
#                                  ) VALUES (
#                                      DEFAULT
#                                     ,'{bebida.get_nome_bebida()}'
#                                     ,{bebida.get_teor_bebida()}
#                                     ,{bebida.get_tipo_bebida()}                                 
#                                  )"""

#         super().inserir(comando_sql_insert)

#     def alterar(self, bebida:Bebida):
#         comando_sql_alterar = f"""UPDATE BEBIDA_FESTA SET
#                                  NOME = '{bebida.get_nome_bebida()}'
#                                , TEOR = {bebida.get_teor_bebida()}
#                                , TIPO_BEBIDA_ID = {bebida.get_tipo_bebida()}
#                                WHERE ID = {bebida.get_id_bebida()}"""

#         super().alterar(comando_sql_alterar)
    
#     def deletar(self, id):
#         comando_sql_deletar = f"DELETE FROM BEBIDA_FESTA WHERE ID = {id}"
#         super().deletar(comando_sql_deletar)

#     def listar(self):
#         lista_bebidas = []
#         comando_sql_listar = """SELECT 
#                                 B.NOME
#                                 ,B.TEOR
#                                 ,TB.NOME
#                                 ,TB.DESCRICAO
#                                 ,TB.ID
#                                 ,B.ID
#                                 FROM BEBIDA_FESTA AS B
#                                 JOIN TIPO_BEBIDA AS TB
#                                 ON B.TIPO_BEBIDA_ID = TB.ID"""
                                
#         lista_tuplas = super().listar(comando_sql_listar)

#         for l in lista_tuplas:
#             tipo_bebida = TipoBebida(l[2], l[3], l[4])
#             bebida = Bebida( l[0], l[1], tipo_bebida.__dict__, l[5] )
#             lista_bebidas.append(bebida.__dict__)
#         return lista_bebidas

#     def buscar_por_id(self, id):
#         comando_sql_buscar_id = f"""SELECT
#                                 B.NOME
#                                 ,B.TEOR
#                                 ,B.NOME
#                                 ,TB.DESCRICAO
#                                 ,TB.ID
#                                 ,B.ID
#                                 FROM BEBIDA_FESTA AS B
#                                 JOIN TIPO_BEBIDA AS TB
#                                 ON B.TIPO_BEBIDA_ID = TB.ID
#                                 WHERE B.ID = {id}"""

#         dados = super().buscar_por_id(comando_sql_buscar_id)

#         tipo_bebida = TipoBebida(dados[2], dados[3], dados[4])
#         bebida = Bebida(dados[0], dados[1], tipo_bebida.__dict__, dados[5])
#         return bebida.__dict__