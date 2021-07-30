class Pokemon(object):
    def __init__(self, name_pokemon: str, picture_pokemon: str) -> None:
        self._name_pokemon = name_pokemon
        self._picture_pokemon = picture_pokemon

    def get_name_pokemon(self) -> str:
        return self._name_pokemon

    def get_picture_pokemon(self) -> str:
        return self._picture_pokemon

    def __str__(self) -> str:
        return f'[POKEMON]: "{self.get_name_pokemon()}" [IMAGEN]: "{self.get_picture_pokemon()}"'
