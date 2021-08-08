from setuptools import setup


dependencies = [
    "Flask==2.0.1",
    "requests==2.25.1",
    "marshmallow==3.13.0",
]

package_data = {
    "function.resources": ["configuration.ini"],
    "templates": ["form_pokemon.html"],
}

packages = [
    "controller",
    "function",
    "function.resources",
    "log",
    "model",
    "schema",
    "templates",
]

platform = ["any"]

long_description = (
    "It is requested to develop a web application to search for Pokemons this should consume the data "
    "from the Pokemons API "
)

manifest = dict(
    name="pokemon-finder",
    version="1.0.0",
    author="DobleRR - Rodrigo Quispe",
    author_email="rrquispezabala@gmail.com",
    description="Search pokemon by name",
    url="https://github.com/RRodriQZ",
    license="MIT",
    python_requires=">=3.6, <4",
    keywords="Search Pokemon",
    install_requires=dependencies,
    package_data=package_data,
    packages=packages,
    platforms=platform,
    long_description=long_description,
    long_description_content_type="text/markdown",
)


if __name__ == "__main__":
    setup(**manifest)
