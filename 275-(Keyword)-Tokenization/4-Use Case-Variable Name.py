# Agora que adicionamos um conjunto de objetos ao Weaviate, vamos ver como diferentes métodos de tokenização impactam a recuperação filtrada.
# Cada consulta filtrada terá uma aparência semelhante a esta, na qual filtramos os objetos para um conjunto de strings de consulta.
# Configuraremos uma função reutilizável para filtrar objetos com base em um conjunto de strings de consulta. Lembre-se de que um filtro é binário: ou ele corresponde ou não.
# A função retornará uma lista de objetos correspondentes e os imprimirá para que possamos ver.


import weaviate
from weaviate.classes.query import Filter
from weaviate.collections import Collection
from typing import List

# Instantiate your client (not shown). e.g.:
# client = weaviate.connect_to_weaviate_cloud(...) or
client = weaviate.connect_to_local()

collection = client.collections.use("TokenizationDemo")

# Get property names
property_names = list()
for p in collection.config.get().properties:
    property_names.append(p.name)

query_strings = ["<YOUR_QUERY_STRING>"]


def filter_demo(collection: Collection, property_names: List[str], query_strings: List[str]):
    from weaviate.classes.query import Filter

    for query_string in query_strings:
        print("\n" + "=" * 40 + f"\nHits for: '{query_string}'" + "\n" + "=" * 40)
        for property_name in property_names:
            response = collection.query.fetch_objects(
                filters=Filter.by_property(property_name).equal(query_string),
            )
            if len(response.objects) > 0:
                print(f">> '{property_name}' matches")
                for obj in response.objects:
                    print(obj.properties[property_name])


filter_demo(collection, property_names, ["variable_name"])