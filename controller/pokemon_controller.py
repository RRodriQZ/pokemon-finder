from function.functions import get_results_from_pokemon_API_call, get_response_by_url
from schema.validate import validate_pokemon_for_schema
from model.pokemon_model import Pokemon
from log.logger import Log


# GLOBAL VALUES
logger = Log().get_logger(__name__)


def search_pokemons_by_name(search_pokemon_name: str, pokedex: list[dict]) -> list[Pokemon]:
    """The function returns a list of pokemon that meet the search performed by the 'Name' field
    is partial or complete in the 'POKEMON API'

    :param pokedex: list[dict]
    :param search_pokemon_name: str
    :return: list[Pokemon]
    """
    try:
        pokemons_found = []
        search_pokemon_name = search_pokemon_name.lower()

        logger.info(
            f'=== The search (partial/complete) of the POKEMON: "{search_pokemon_name}" ==='
        )

        for pokemon in pokedex:
            try:
                if pokemon["name"].startswith(search_pokemon_name):

                    response_pokemon = get_response_by_url(url=pokemon["url"])
                    name_pokemon = pokemon["name"]
                    picture_pokemon = response_pokemon["sprites"]["front_default"]

                    validate_pokemon_for_schema(
                        {"name": name_pokemon, "picture": picture_pokemon}
                    )

                    new_pokemon = Pokemon(name_pokemon, picture_pokemon)

                    pokemons_found.append(new_pokemon)

                    logger.info(f"--> Found: {new_pokemon.__str__()}")

            except Exception as e:
                logger.error(f'Error POKEMONS search failed, error: "{e}"')

        return pokemons_found

    except Exception as e:
        logger.error(f'Error occurred in the search for pokemon, error: "{e}"')
