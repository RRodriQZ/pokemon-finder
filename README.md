# POKEMON FINDER #

Se pide desarrollar una aplicación web para buscar Pokemones. Esta debera consumir los datos de 
"la API de Pokemones".

Para mas informacion visitar: https://pokeapi.co/

# Pre Requirements 📋

* Python 3 / Docker-compose

# Setup Python Virtual Environment 🔧
Windows cmd/ Linux command:

1) python -m venv venv

2) cd venv\Scripts & .\activate

3) cd .. & cd .. & pip install -r requirements.txt

# Running Script 🐼

4) python app.py

**Unittest:**

* python test.py -v

# Running using Docker

1) docker-compose build
2) docker-compose up

**Unittest:**

* docker-compose run web python test.py -v

# Web application:

Los testeos en [**LOCAL**] se hicieron con el navegador desde la url: http://localhost:5000

**Endpoints:**
1) > POST / GET → **/pokemon_search**

    [POST] input "name pokemon" : **String**

# Author 🖋

* Rodrigo Quispe - Backend Developer - [RRodriQZ]
 
[RRodriQZ]: https://github.com/RRodriQZ
