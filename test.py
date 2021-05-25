from controller.pokemon_controller import search_pokemons_by_name
from model.pokemon_model import Pokemon
from flask import Flask
import unittest


class PokemonTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False
        self.pokemon_list = []
        self.pokemon_gengar = Pokemon('gengar', 'https://url_test_img')

    def tearDown(self):
        pass

    def testPokemonListIsEmpty(self):
        self.assertEqual(self.pokemon_list, [])

    def testQuantityPokemonsIsZero(self):
        self.assertEqual(len(self.pokemon_list), 0)

    def testCreationPokemon(self):
        self.assertEqual(self.pokemon_gengar.get_name_pokemon(), 'gengar')

    def testQuantityPokemonsIsOne(self):
        self.pokemon_list.append(self.pokemon_gengar)
        self.assertEqual(len(self.pokemon_list), 1)

    def testPokemonSearchFullName(self):
        search_pokemon_full_name = 'gastly'
        found_pokemon = search_pokemons_by_name(self.app, search_pokemon_full_name)

        self.assertEqual(len(found_pokemon), 1)
        self.assertEqual(found_pokemon[0].get_name_pokemon(), 'gastly')

    def testPokemonSearchPartialName(self):
        search_pokemon_partial_name = 'gen'
        found_pokemons = search_pokemons_by_name(self.app,
                                                 search_pokemon_partial_name)

        self.assertEqual(len(found_pokemons), 4)
        self.assertEqual(found_pokemons[0].get_name_pokemon(), 'genesect')
        self.assertEqual(found_pokemons[1].get_name_pokemon(), 'gengar')
        self.assertEqual(found_pokemons[2].get_name_pokemon(), 'gengar-gmax')
        self.assertEqual(found_pokemons[3].get_name_pokemon(), 'gengar-mega')


if __name__ == '__main__':
    unittest.main()
