from marshmallow import Schema, fields, post_load
from model.pokemon_model import Pokemon


class PokemonSchema(Schema):
    """Pokemon Schema"""

    name_pokemon = fields.String(attribute="name_pokemon")
    picture_pokemon = fields.String(attribute="picture_pokemon")

    @post_load
    def create_pokemon(self, data, **kwargs):
        return Pokemon(**data)
