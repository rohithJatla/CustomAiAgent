from sentence_transformers import SentenceTransformer
import yaml

with open("configs/config.yaml") as f:
    config = yaml.safe_load(f)

model = SentenceTransformer(config['embedding']['model_name'])

def embed_text(texts):
    return model.encode(texts)
