from controller.pokemon_controller import search_pokemons_by_name
from function.functions import get_results_from_pokemon_API_call
from flask import Flask, Response, request, render_template


pokemons_results = get_results_from_pokemon_API_call()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_status():
    """Return API Status"""
    return Response(
        response=f"The API POKEMON works!",
        status=200,
        mimetype="application/json",
    )


@app.route("/pokemon_search", methods=["POST", "GET"])
def pokemon_search():
    """In this view the form to SEARCH a pokemon by name will be completed this will look
    for the 'pokemon API' and return the name full pokemon and its associated pokedex image
    """
    try:
        if request.method == "POST":
            pokemon_name = request.form.get("name_pokemon")
            found_pokemons = search_pokemons_by_name(
                search_pokemon_name=pokemon_name, pokedex=pokemons_results
            )
            app.logger.info("=== Search completed successfully ====")
            return render_template("form_pokemon.html", found_pokemons=found_pokemons)

        elif request.method == "GET":
            return render_template("form_pokemon.html")

    except Exception as e:
        app.logger.error(f'=== Error searching for pokemon, error: "{e}"')


@app.errorhandler(404)
def not_found(error=None):
    """ Error handler for resources that are not covered """
    app.logger.error(f'=== Resource not found: "{request.url}" ===')

    return Response(
        response=f'Resource not found: "{request.url}"',
        status=404,
        mimetype="application/json",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)
