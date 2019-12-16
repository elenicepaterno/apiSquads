class Linguagem:
    def __init__(self, nome_ling=None, id=None):
        self.nome_ling = nome_ling
        self.id = id
    
    def get_nome_ling(self):
        return self.nome_ling

    def get_id_ling(self):
        return self.id
