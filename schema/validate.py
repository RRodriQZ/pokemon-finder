from jsonschema import validate
import json
import os


def validate_pokemon_for_schema(json_pokemon: dict) -> None:
    file_path = os.path.join(os.path.dirname(__file__), 'pokemon_schema.json')
    with open(file_path, 'r') as values:
        SCHEMA_POKEMON = json.load(values)

    validate(instance=json_pokemon, schema=SCHEMA_POKEMON)
