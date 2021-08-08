# POKEMON FINDER #

It is requested to develop a web application to search for Pokemons. This should consume the data from
"the API Pokemon"

For more information visit: https://pokeapi.co/

# Pre Requirements 📋
* **Python 3**-**pipenv** / **Docker-compose**

# Setup Python Virtual Environment 🔧 #
```cmd
pip install pipenv
```
**Windows** CMD:
```cmd
python -m venv venv
.\venv\Scripts\activate
pip install -e .
```
**Linux / MAC** command:
```cmd
python -m venv venv
source venv/bin/activate
python -m pip install -e .
```
# Running Python Script 🐼 #
```cmd
python app.py
```
**Unittest:**
```cmd
python test.py -v
```
# Running using Docker
```cmd
docker-compose build
docker-compose up
```
**Unittest:**
```cmd
docker-compose run web python test.py -v
```
# Web Application:

The tests in [**LOCAL**] were made with the browser from the url: http://localhost:5000

**Endpoints:**
1) > POST / GET → **/pokemon_search**

    [POST] input "name pokemon" : **String**

# Author 🖋

* Rodrigo Quispe - Backend Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ