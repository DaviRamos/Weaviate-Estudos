# Criaremos uma coleção de objetos simples, com cada objeto contendo diversas propriedades. 
# Cada propriedade conterá o mesmo texto, mas com diferentes métodos de tokenização aplicados.

import weaviate
from weaviate.classes.config import Property, DataType, Tokenization, Configure

# Instantiate your client (not shown). e.g.:
# client = weaviate.connect_to_weaviate_cloud(...) or
client = weaviate.connect_to_local()

tkn_options = [
    Tokenization.WORD,
    Tokenization.LOWERCASE,
    Tokenization.WHITESPACE,
    Tokenization.FIELD,
]

# Create a property for each tokenization option
properties = []
for tokenization in tkn_options:
    prop = Property(
        name=f"text_{tokenization.replace('.', '_')}",
        data_type=DataType.TEXT,
        tokenization=tokenization
    )
    properties.append(prop)


client.collections.create(
    name="TokenizationDemo",
    properties=properties,
    vector_config=Configure.Vectors.self_provided()
)

client.close()