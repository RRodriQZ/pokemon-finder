from dataclasses import dataclass


@dataclass
class Pokemon(object):
    """Class represents Pokemon model field: name_pokemon and picture_pokemon"""

    name_pokemon: str
    picture_pokemon: str

    def get_name_pokemon(self) -> str:
        return self.name_pokemon

    def get_picture_pokemon(self) -> str:
        return self.picture_pokemon

    def __str__(self) -> str:
        return f'[POKEMON]: "{self.get_name_pokemon()}" [IMAGEN]: "{self.get_picture_pokemon()}"'
