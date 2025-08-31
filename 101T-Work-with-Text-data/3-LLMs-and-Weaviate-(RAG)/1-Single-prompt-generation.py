import os
import weaviate
from weaviate.config import AdditionalConfig, Timeout

# Instantiate your client (not shown). e.g.:
# headers = {"X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")}  # Replace with your OpenAI API key
# client = weaviate.connect_to_weaviate_cloud(..., headers=headers) or
# client = weaviate.connect_to_local(..., headers=headers)

#client = weaviate.connect_to_local()
client = weaviate.connect_to_local(
            additional_config=AdditionalConfig(
                timeout=Timeout(init=30, query=60, insert=120)  # Values in seconds
            )
        )

# Get the collection
movies = client.collections.get("Movie")

# Perform query
response = movies.generate.near_text(
    query="dystopian future",
    limit=5,
    single_prompt="Translate this into French: {title}"
)

# Inspect the response
for o in response.objects:
    print(o.properties["title"])  # Print the title
    print(o.generated)  # Print the generated text (the title, in French)

client.close()