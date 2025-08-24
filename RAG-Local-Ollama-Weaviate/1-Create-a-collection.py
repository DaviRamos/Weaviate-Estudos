import weaviate

import weaviate.classes.config as wc
import os


documents = [
  "Llamas are members of the camelid family meaning they're pretty closely related to vicuñas and camels",
  "Llamas were first domesticated and used as pack animals 4,000 to 5,000 years ago in the Peruvian highlands",
  "Llamas can grow as much as 6 feet tall though the average llama between 5 feet 6 inches and 5 feet 9 inches tall",
  "Llamas weigh between 280 and 450 pounds and can carry 25 to 30 percent of their body weight",
  "Llamas are vegetarians and have very efficient digestive systems",
  "Llamas live to be about 20 years old, though some only live for 15 years and others live to be 30 years old",
]

client = weaviate.connect_to_local()

# Create a new data collection
client.collections.create(
    name="docs", # Name of the data collection
    properties=[
        wc.Property(name="docs", data_type=wc.DataType.TEXT) # Name and data type of the property
    ],
    # Define the vectorizer module
    vector_config=wc.Configure.Vectors.text2vec_ollama(  # Configure the Ollama embedding integration
        api_endpoint="http://host.docker.internal:11434",  # If using Docker you might need: http://host.docker.internal:11434
        model="nomic-embed-text",  # The model to use
    ),
    # Define the generative module
    generative_config=wc.Configure.Generative.ollama(  # Configure the Ollama generative integration
        api_endpoint="http://host.docker.internal:11434",  # If using Docker you might need: http://host.docker.internal:11434
        model="llama3.2",  # The model to use
    )

)
client.close()  # Close the connection & release resources