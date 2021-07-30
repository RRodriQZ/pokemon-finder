# POKEMON FINDER #

Se pide desarrollar una aplicación web para buscar Pokemones. Esta debera consumir los datos de 
"la API de Pokemones".

Para mas informacion visitar: https://pokeapi.co/

# Pre Requirements 📋
* **Python 3** - **pipenv** / **Docker-compose**

# Setup Python Virtual Environment 🔧 #
```cmd
pip install pipenv
```

**Windows** CMD:
```cmd
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
**Linux / MAC** command:
```cmd
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```
# Running Python Script 🐼 #
```cmd
python main.py
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
* docker-compose run web python test.py -v
```
# Web Application:

Los testeos en [**LOCAL**] se hicieron con el navegador desde la url: http://localhost:5000

**Endpoints:**
1) > POST / GET → **/pokemon_search**

    [POST] input "name pokemon" : **String**

# Author 🖋

* Rodrigo Quispe - Backend Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ
