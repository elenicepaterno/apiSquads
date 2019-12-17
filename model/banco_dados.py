class BancoDados:
    def __init__(self, nome_banco=None, id=None):
        self.nome_banco = nome_banco
        self.id = id
    

    def get_nome_banco(self):
        return self.nome_banco


    def get_id_banco(self):
        return self.id
