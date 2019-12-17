from model.squads import Squads
class VerificaDados:
    def verificar_squads(self, squad:Squads):
        
        if squad.ling == 'Java' and squad.banco != 'PostgreSQL':
            return False        

        if squad.frame == 'Vue' and squad.prog == 'Nicole':
            return False
        
        if squad.frame == 'Angular' and squad.banco != 'MongoDb':
            return False

        if squad.prog == 'Mateus' and squad.ling != 'Python':
            return False
        
        if squad.prog == 'Mateus' and squad.banco == 'MySqlServer':
            return False

        if squad.prog == 'Tiago' and squad.ling == 'PHP':
            return False

        return True