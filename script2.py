import requests
from flask import Flask
# url = "https://swapi.dev/api/people/1"

# payload = {}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

app = Flask(__name__)

# @app.route("/mon_a/<nom>")
# def search_pokemon(nom):
#     api = requests.get('https://swapi.dev/api')
#     if prenom == api:
#         print("pokemon exist")
#     else:
#         print("false")
#         json = v.jso^dv,sponvbv()
        
   
#     return api
# app.run(debug=True)


# from flask import Flask
# import requests

# app = Flask(__name__)
# @app.route("/bonjour/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/aurevoir/")
# def goodbye_world():
#     return "Goodbye, World!"

# @app.route("/pokemon/<name>")
# def pokemon(name):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         pokemon_name = pokemon_data['name']
#         pokemon_id = pokemon_data['id']
#         return f"Name: {pokemon_name}, ID: {pokemon_id}"
#     else:
#         return "Pokemon not found!"
    
# @app.route("/stw/<id>")
# def starwars(id) :
#     response2 = requests.get(f"https://swapi.dev/api/people/{id}")
#     # if response2.status_code == 200:
#     #     stw_data = response2.json()
#     #     stw_name = stw_data['name']
#     #     stw_mass = stw_data['mass']
#     #     return f"Name: {stw_name}, Mass: {stw_mass}"
#     # else :
#     #     return "Character not found!"
#     # Autre faÃ§on de faire (=exeption)
#     try :
#         json =response2.json()
#         p_name = json["name"]
#         return" True"
#     except :
#         return "False"
    
    
    
@app.route("/Find/<univers>/<id>")
    
        
def find(univers, id):
    
    if univers == "pk":
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/"+id)
        
        return response.json()
    if univers == "sw":
        response2 = requests.get(f"https://swapi.dev/api/people/"+id)

        return response2.json()
    else:
        return"univers not founde"
app.run(debug=True)   


