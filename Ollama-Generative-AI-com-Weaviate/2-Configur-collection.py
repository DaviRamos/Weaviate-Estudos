import weaviate
from weaviate.classes.config import Configure
import os

client = weaviate.connect_to_local()

print(client.is_ready())

client.collections.create(  
    "DemoCollection3",
     vector_config=Configure.Vectors.text2vec_ollama(  # Configure the Ollama embedding integration
        api_endpoint="http://host.docker.internal:11434",  # If using Docker you might need: http://host.docker.internal:11434
        model="nomic-embed-text",  # The model to use
    ),
    # Define the generative module
    generative_config=Configure.Generative.ollama(  # Configure the Ollama generative integration
        api_endpoint="http://host.docker.internal:11434",  # If using Docker you might need: http://host.docker.internal:11434
        model="llama3.2",  # The model to use
    )
    # Additional parameters not shown
)
client.close()  # Close the connection & release resources
