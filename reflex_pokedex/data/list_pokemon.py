import requests

class Pokemon:
    def __init__(self, nombre=None, id=None, tipos=None, habilidades=None, imagen_url=None, url=None):
        self.nombre = nombre
        self.id = id
        self.tipos = tipos
        self.habilidades = habilidades
        self.imagen_url = imagen_url,
        self.url=url

    def obtener_datos_de_pokeapi(self, nombre_pokemon):
        # URL de la PokeAPI para obtener información de un Pokémon por nombre
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}/"

        # Realizar la solicitud a la PokeAPI
        respuesta = requests.get(url)

        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 200:
            datos_pokemon = respuesta.json()

            # Extraer información relevante y almacenarla en la instancia de la clase
            self.nombre = datos_pokemon["name"]
            self.id = datos_pokemon["id"]
            self.tipos = [tipo["type"]["name"] for tipo in datos_pokemon["types"]]
            self.habilidades = [habilidad["ability"]["name"] for habilidad in datos_pokemon["abilities"]]
            self.imagen_url = datos_pokemon["sprites"]["other"]["official-artwork"]["front_default"]
            self.url = url
        else:
            print(f"Error al obtener datos de la PokeAPI. Código de estado: {respuesta.status_code}")

    def __str__(self):
        return f"Pokemon: {self.nombre} (ID: {self.id})\nTipos: {', '.join(self.tipos)}\nHabilidades: {', '.join(self.habilidades)}\nImagen URL: {self.imagen_url}"

# Obtener los primeros 251 Pokémon
def obtener_pokemon(limit=251):
    # URL de la PokeAPI para obtener la lista de Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"

    # Realizar la solicitud a la PokeAPI
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa (código 200)
    if respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        resultados = datos_pokemon.get("results", [])

        # Crear instancias de la clase Pokemon con los datos obtenidos
        lista_pokemon = []
        for pokemon_info in resultados:
            nombre_pokemon = pokemon_info["name"]
            nuevo_pokemon = Pokemon()
            nuevo_pokemon.obtener_datos_de_pokeapi(nombre_pokemon)
            lista_pokemon.append(nuevo_pokemon)

        return lista_pokemon
    else:
        print(f"Error al obtener la lista de Pokémon. Código de estado: {respuesta.status_code}")
        return []

lista_pokemon = obtener_pokemon()
