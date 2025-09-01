import weaviate
import weaviate.classes.config as wc
import os

# Instantiate your client (not shown). e.g.:
# headers = {"X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")}  # Replace with your OpenAI API key

client = weaviate.connect_to_local()

client.collections.delete("MovieMM")

client.collections.create(
    name="MovieMM",  # The name of the collection ('MM' for multimodal)
    properties=[
        wc.Property(name="title", data_type=wc.DataType.TEXT),
        wc.Property(name="overview", data_type=wc.DataType.TEXT),
        wc.Property(name="vote_average", data_type=wc.DataType.NUMBER),
        wc.Property(name="genre_ids", data_type=wc.DataType.INT_ARRAY),
        wc.Property(name="release_date", data_type=wc.DataType.DATE),
        wc.Property(name="tmdb_id", data_type=wc.DataType.INT),
        wc.Property(name="poster", data_type=wc.DataType.BLOB),
    ],
    # Define & configure the vectorizer module
    vector_config=wc.Configure.Vectors.multi2vec_clip(
        image_fields=[wc.Multi2VecField(name="poster", weight=0.9)],    # 90% of the vector is from the poster
        text_fields=[wc.Multi2VecField(name="title", weight=0.1)],      # 10% of the vector is from the title
    ),
    # Define the generative module
        # Define the generative module
    generative_config=wc.Configure.Generative.ollama(  # Configure the Ollama generative integration
        api_endpoint="http://host.docker.internal:11434",  # If using Docker you might need: http://host.docker.internal:11434
        model="llama3.2",  # The model to use
    )
)

client.close()