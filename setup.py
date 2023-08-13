from setuptools import setup, find_packages
import os
import torch
import datasets
from InstructorEmbedding import INSTRUCTOR
import json

def initialize_koko():
    torch.set_grad_enabled(False)

    # Check if config.json exists, if not, create it
    if not os.path.exists('config.json'):
        default_config = {
            "column": "embedding",
            "prompt": "Represent the Stackoverflow question for retrieving corresponding codes: ",
            "model_path": "bin/model.bin",
            "dataset_path": "bin/dataset.bin",
            "faiss_path": "bin/faiss.bin"
        }

        with open('config.json', 'w') as f:
            json.dump(default_config, f)

    # Load the config file
    with open('config.json', 'r') as f:
        CONFIG = json.load(f)

    # PROMPT = CONFIG['prompt']
    COLUMN = CONFIG['column']
    MODEL_PATH = CONFIG['model_path']
    DATASET_PATH = CONFIG['dataset_path']
    FAISS_PATH = CONFIG['faiss_path']

    # Check if setup has already been done
    if not (os.path.exists(MODEL_PATH) and os.path.exists(DATASET_PATH) and os.path.exists(FAISS_PATH)):
        os.makedirs("bin", exist_ok=True)
        # Initialize the sentence transformer model
        model = INSTRUCTOR('hkunlp/instructor-large')
        torch.save(model, MODEL_PATH)

        # Load the huggingface dataset with the API descriptions and embeddings
        ds = datasets.load_dataset('Maurus/APIBench')['train']
        ds.save_to_disk(DATASET_PATH)

        # Create FAISS index
        ds.add_faiss_index(COLUMN)
        ds.save_faiss_index(COLUMN, file=FAISS_PATH)

# Call the initialization function
initialize_koko()

setup(
    name='koko-gorilla',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'faiss-cpu',
        'datasets',
        'transformers',
        'sentence_transformers',
        'InstructorEmbedding',
        'questionary'
    ],
    entry_points={
        'console_scripts': [
            'koko=koko:main',
        ],
    },
)