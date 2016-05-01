__author__ = 'mario'



class Team:
    """ Team representation. """
    def __init__(self, team_id, security_key):
        self.name = team_id
        self.security_key = security_key

    def set_current_position(self, vertice_id1, vertice_id2):
        self.vertice_id1 = vertice_id1
        self.vertice_id2 = vertice_id2

    def is_valid_security_key(self, key):
        if self.security_key == key:
            return True
        else:
            return False