from flask import Flask, Response, request, render_template
from controller.pokemon_controller import search_pokemons_by_name
from log.logger import Log

app = Flask(__name__)
log = Log()


@app.route('/pokemon_search', methods=['POST', 'GET'])
def pokemon_search():
    """
    En esta vista se completara el formulario para BUSCAR un pokemon
    por su nombre.

    Esto buscara en la 'API de pokemon' y nos retornara el nombre
    completo del pokemon y su imagen del pokedex asociada.
    """
    try:
        if request.method == 'POST':
            _search_pokemon_name = request.form.get("name_pokemon")
            found_pokemons = search_pokemons_by_name(app, _search_pokemon_name)
            app.logger.info('=== Se completo la busqueda correctamente ====')
            return render_template("form_pokemon.html",
                                   found_pokemons=found_pokemons)

        elif request.method == 'GET':
            return render_template("form_pokemon.html")

    except Exception as e:
        app.logger.error('=== Ocurrio un error en la busqueda del pokemon: ' +
                         str(e))


@app.errorhandler(404)
def not_found(error=None):
    """
    Manejador de errores para los recursos que no estan contemplados.
    """
    app.logger.error('=== Recurso no encontrado: "' + request.url + '" ===')
    return Response(response='Recurso no encontrado: "' + request.url + '".',
                    status=404, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
