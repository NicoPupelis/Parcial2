
from cola import Cola


class BinaryTree:

    class __Node:
        def __init__(self, value, other_values=None, left=None, right=None):
            self.value = value
            self.other_values = other_values
            self.left = left
            self.right = right
            
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

pokemon_data = [
    {"nombre": "Pikachu", "numero": 25, "tipo": "Electrico"},
    {"nombre": "Bulbasaur", "numero": 1, "tipo": "Hierba"},
    {"nombre": "Wartortle", "numero": 31, "tipo": "Agua"},
    {"nombre": "Charmander", "numero": 4, "tipo": "Fuego"},
    {"nombre": "Butterfree", "numero": 86, "tipo": "Hierba"},
    {"nombre": "Blastoise", "numero": 65, "tipo": "Agua"},
    {"nombre": "Magneton", "numero": 87, "tipo": "Electrico"},
    {"nombre": "Ponyta", "numero": 54, "tipo": "Fuego"},
    {"nombre": "Metapod", "numero": 13, "tipo": "Hierba"},
    {"nombre": "Psyduck", "numero": 43, "tipo": "Agua"},
    {"nombre": "Magnemite", "numero": 16, "tipo": "Electrico"},
    {"nombre": "Magmar", "numero": 10, "tipo": "Fuego"},
    {"nombre": "Caterpie", "numero": 65, "tipo": "Hierba"},
    {"nombre": "Golduck", "numero": 41, "tipo": "Agua"},
    {"nombre": "Jolteon", "numero": 44, "tipo": "Electrico"},
    {"nombre": "Lycanroc", "numero": 45, "tipo": "Hierba"},
    {"nombre": "Tyrantrum", "numero": 46, "tipo": "Fuego"},
]

for pokemon in pokemon_data:
    arbol_nombre.insert_node(pokemon["nombre"], {"numero": pokemon["numero"], "tipo": pokemon["tipo"]})
    arbol_numero.insert_node(pokemon["numero"], {"nombre": pokemon["nombre"], "tipo": pokemon["tipo"]})
    arbol_tipo.insert_node(pokemon["tipo"], {"nombre": pokemon["nombre"], "numero": pokemon["numero"]})
    
def search_name_proximity(root, key, results):
    if root is not None:
        if key.lower() in root.value.lower():
            results.append(root.other_values)  
        if key.lower() < root.value.lower():
            search_name_proximity(root.left, key, results)
        if key.lower() > root.value.lower():
            search_name_proximity(root.right, key, results)


search_results = []
search_name_proximity(arbol_nombre.root, "Pik", search_results)   
for pokemon in search_results:
    print(f"Nombre: {pokemon['nombre']}, Número: {pokemon['numero']}, Tipo: {pokemon['tipo']}")

lista_tipo = ['Agua', 'Fuego', 'Hierba', 'Electrico']

for tipo in lista_tipo:
    poke = arbol_tipo.search(tipo)  
    if poke:
        print(f"Tipo: {tipo}") 
        for pokemon in poke.other_values:
            print(pokemon['nombre'])
    else:
        print(f"No se encontraron Pokémon del tipo {tipo}")
        
pokemons_buscados = ["Jolteon", "Lycanroc", "Tyrantrum"]

for pokemon in pokemons_buscados:
    resultado_nombre = arbol_nombre.search(pokemon)

    if resultado_nombre:
        print(f"Nombre: {resultado_nombre.value}, Número: {resultado_nombre.other_values['numero']}, Tipo: {resultado_nombre.other_values['tipo']}")
        
        
def contar_tipo(arbol_tipo, tipo):
    contador = 0
    poke = arbol_tipo.search(tipo)
    if poke:
        for pokemon in poke.other_values:
            contador += 1
    return contador

tipo_electrico = "Electrico"
tipo_acero = "Acero"

cantidad_electricos = contar_tipo(arbol_tipo, tipo_electrico)
cantidad_acero = contar_tipo(arbol_tipo, tipo_acero)

print(f"La cantidad de Pokémon de tipo Eléctrico es: {cantidad_electricos}")
print(f"La cantidad de Pokémon de tipo Acero es: {cantidad_acero}")


print('Por orden ascendente')
arbol_nombre.inorden()
print(' ')
arbol_numero.inorden()
print(' ')
print('Por por nivel')
arbol_nombre.by_level()

