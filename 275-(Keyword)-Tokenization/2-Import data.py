# Agora, adicionamos objetos à coleção, repetindo objetos de texto como propriedades.

import weaviate

# Instantiate your client (not shown). e.g.:
# client = weaviate.connect_to_weaviate_cloud(...) or
client = weaviate.connect_to_local()

collection = client.collections.use("TokenizationDemo")

# Get property names
property_names = [p.name for p in collection.config.get().properties]

phrases = [
    # string with special characters
    "Lois & Clark: The New Adventures of Superman",

    # strings with stopwords & varying orders
    "computer mouse",
    "Computer Mouse",
    "mouse computer",
    "computer mouse pad",
    "a computer mouse",

    # strings without spaces
    "variable_name",
    "Variable_Name",
    "Variable Name",
    "a_variable_name",
    "the_variable_name",
    "variable_new_name",
]

for phrase in phrases:
    obj_properties = {}
    for property_name in property_names:
        obj_properties[property_name] = phrase
    print(obj_properties)
    collection.data.insert(properties=obj_properties)

client.close()