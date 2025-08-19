import weaviate
import os

client = weaviate.connect_to_local()



headers = {
    "X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")
}  # Replace with your OpenAI API key

client = weaviate.connect_to_local(headers=headers)

