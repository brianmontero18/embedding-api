import os
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load model once on startup
model_name = os.getenv("EMBEDDING_MODEL", "thenlper/gte-base")
model = SentenceTransformer(model_name)

@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "Embedding service is running."})

@app.route('/embed', methods=['POST'])
def embed():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()

        if not text:
            return jsonify({'error': 'Missing "text" field'}), 400

        embedding = model.encode(text).tolist()
        return jsonify({'embedding': embedding})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
