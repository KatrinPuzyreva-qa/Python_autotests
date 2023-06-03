import requests

host = 'https://pokemonbattle.me:9104'
token = 'fbc63e65730a4c62644f56e3ad9de34d'
answer_pokemons = requests.post(f'{host}/pokemons', json = 
    {
    "name": "Lorin",
    "photo": "https://dolnikov.ru/pokemons/albums/024.png"
}
, headers= {"Content-Type" : "application/json",
            "trainer_token" : token})

print(answer_pokemons.text, answer_pokemons.status_code)

answer_change_of_name = requests.put(f'{host}/pokemons', json = 
    {
    "pokemon_id": "12753",
    "name": "Lilit",
    "photo": "https://dolnikov.ru/pokemons/albums/024.png"
}, headers = {"Content-Type" : "application/json",
            "trainer_token" : token})

print(answer_change_of_name.text, answer_change_of_name.status_code)


answer_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json =
     {
    "pokemon_id": "12753"
}, headers= {"Content-Type" : "application/json",
            "trainer_token" : token})
                                   

print(answer_add_pokeball.text, answer_add_pokeball.status_code)

trainer_info = requests.get(f'{host}/trainers',
                                 params = {'trainer_id': 4637})

print(trainer_info.text, trainer_info.status_code)                                