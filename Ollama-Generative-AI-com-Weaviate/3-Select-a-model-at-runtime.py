import weaviate

from weaviate.classes.config import Configure
from weaviate.classes.generate import GenerativeConfig

client = weaviate.connect_to_local()

collection = client.collections.get("DemoCollection3")
response = collection.generate.near_text(
    query="A holiday film",
    limit=2,
    grouped_task="Write a tweet promoting these two movies",
    generative_provider=GenerativeConfig.ollama(
        api_endpoint="http://host.docker.internal:11434",  # If using Docker, use this to contact your local Ollama instance
        model="llama3"  # The model to use, e.g. "phi3", or "mistral", "command-r-plus", "gemma"
    ),
    # Additional parameters not shown
)

client.close()  # Close the connection & release resources