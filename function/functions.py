from configparser import ConfigParser
from log.logger import Log
import requests
import json


# GLOBAL VALUES
config = ConfigParser()
config.read("function/resources/configuration.ini")

API_POKEMON = config["API_POKEMON"]["api_url"]
logger = Log().get_logger(__name__)
time_out = 10


def get_response_by_url(url: str) -> dict:
    """Returned response of the call to the url

    :param url: str
    :return: dict
    """
    try:
        response = requests.get(url=url, timeout=time_out)
        return response.json()

    except Exception as e:
        logger.error(f'Error problem calling: "{url}", error: "{e}"')


def get_results_from_pokemon_API_call() -> list:
    """Returns all pokemons from the API call

    :return: list[dict]
    """
    try:
        response_api = get_response_by_url(url=API_POKEMON)
        pokemons_results = sorted(
            response_api["results"], key=lambda poke: poke["name"], reverse=False
        )
        return pokemons_results

    except Exception as e:
        logger.error(f'Error occurred in the Pokemon API call, error: "{e}"')
