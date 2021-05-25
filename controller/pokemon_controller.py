from schema.validate import validate_pokemon_for_schema
from configparser import ConfigParser
from model.pokemon_model import Pokemon
import requests
import json


def get_json_response_by_url(url):
    response = requests.get(url, timeout=10)
    return response.json()


def get_results_from_pokemon_API_call():
    config = ConfigParser()
    config.read('config.ini')
    API_POKEMON = config['API_POKEMON']['api_url']

    response_api = get_json_response_by_url(API_POKEMON)

    #  Ordeno los results de la api por nombre
    pokemons_results = sorted(response_api['results'], key=lambda poke: poke['name'], reverse=False)

    return pokemons_results


def search_pokemons_by_name(app, search_pokemon_name):
    """
    Funcion que retorna un lista de pokemones que cumplan con la busqueda hecha por el
    campo 'Nombre' sea parcial o completo en la 'API de POKEMON'.

    Pokemon -> nombre: String, picture: String

    :param app: app_Flask
    :param search_pokemon_name: String
    :return: [Pokemon]
    """
    try:
        pokemons_found = []
        search_pokemon_name = search_pokemon_name.lower()
        pokemons_results = get_results_from_pokemon_API_call()

        app.logger.info('=== Se inicio la busqueda (parcial/completa) ' +
                        'del POKEMON: "' + search_pokemon_name + '" ===')

        for pokemon in pokemons_results:
            try:
                if pokemon['name'].startswith(search_pokemon_name):
                    response_pokemon = get_json_response_by_url(pokemon['url'])

                    name_pokemon = pokemon['name']
                    picture_pokemon = response_pokemon['sprites']['front_default']

                    validate_pokemon_for_schema(
                        {
                            'name': name_pokemon,
                            'picture': picture_pokemon
                        })

                    new_pokemon = Pokemon(name_pokemon, picture_pokemon)

                    pokemons_found.append(new_pokemon)

                    app.logger.info('--> Se encontro ' + new_pokemon.__str__())

            except Exception as e:
                app.logger.error('error en la busqueda del POKEMON: "' +
                                 pokemon['name'] + '" , error typo: ' + str(e))

        return pokemons_found

    except Exception as e:
        app.logger.error('Ocurrio un problema al llamar a la API' +
                         ' de Pokemon, error: ' + str(e))
