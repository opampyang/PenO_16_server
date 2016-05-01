__author__ = 'mario'



class Team:
    """ Team representation. """
    def __init__(self, team_id, security_key):
        self.team_id = team_id
        self.security_key = security_key
        self.vertice_id1 = 0
        self.vertice_id2 = 0

    def set_current_position(self, vertice_id1, vertice_id2):
        self.vertice_id1 = vertice_id1
        self.vertice_id2 = vertice_id2

    def is_valid_security_key(self, key):
        if self.security_key == key:
            return True
        else:
            return False

    def get_position(self):
        return [self.team_id, self.vertice_id1, self.vertice_id2]