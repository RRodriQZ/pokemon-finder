class Pokemon(object):
    def __init__(self, name_pokemon, picture_pokemon):
        self._name_pokemon = name_pokemon
        self._picture_pokemon = picture_pokemon

    def get_name_pokemon(self):
        return self._name_pokemon

    def get_picture_pokemon(self):
        return self._picture_pokemon

    def __str__(self):
        return '[POKEMON]: "' + self.get_name_pokemon() + \
               '" [IMAGEN]: "' + self.get_picture_pokemon() + '". '
