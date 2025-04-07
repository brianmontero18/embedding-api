from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
model = SentenceTransformer('thenlper/gte-base')

@app.route('/')
def home():
    return 'Embeddings service is running!'

@app.route('/embed', methods=['POST'])
def embed():
    data = request.get_json()
    text = data.get('text', '')
    embedding = model.encode(text).tolist()
    return jsonify({'embedding': embedding})
