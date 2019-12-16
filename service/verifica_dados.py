
class VerificaDados:
    def verificar_squads(self, lista):
        if lista['ling'] == 'Java' and lista['banco'] != 'PostgreSQL':
            return False        

        if lista['frame'] == 'Vue' and lista['prog'] == 'Nicole':
            return False
        
        if lista['frame'] == 'Angular' and lista['banco'] != 'MongoDb':
            return False

        if lista['prog'] == 'Mateus' and lista['ling'] != 'Python':
            return False
        
        if lista['prog'] == 'Mateus' and lista['banco'] == 'MySqlServer':
            return False

        if lista['prog'] == 'Tiago' and lista['ling'] == 'PHP':
            return False

        return True