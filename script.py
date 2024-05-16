# import requests

# pokemons_data = requests.get("https://pokeapi.co/api/v2/pokemon/2");
# print(pokemons_data.json());
# disct = pokemons_data.json()
# dict["name"]
# dict["ability"]
# dict["id"]

# def pokemon_list(n1,n2):
#     n1 = requests.get("https://pokeapi.co/api/v2/pokemon/2")
#     n2 = requests.get("https://pokeapi.co/api/v2/pokemon/3")
#     dict_id1 = n1.json();
#     dict_id2 = n2.json();
#     print("this are two pokemon",  dict_id1["name"], dict_id2["id"])
    
#     if dict_id1["name"] < dict_id2["id"]:
#         print(dict_id1);
#     else:
#         print(dict_id2);
#     return 0;

import http.client

conn = http.client.HTTPSConnection("swapi.dev")
payload = ''
headers = {}
conn.request("GET", "/api/people/1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
