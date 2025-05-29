from flask import Flask, request, jsonify
import clip
import torch
from PIL import Image
import io

app = Flask(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

@app.route('/embed-image', methods=['POST'])
def embed_image():
    if 'image' not in request.files:
        print("❌ No image in request.files")
        return jsonify({'error': 'No image uploaded'}), 400

    try:
        file = request.files['image']
        print("📥 Flask received image:", file.filename)
        image = Image.open(file.stream).convert("RGB")
        image = preprocess(image).unsqueeze(0).to(device)

        with torch.no_grad():
            image_features = model.encode_image(image)

        embedding = image_features.cpu().numpy()[0].tolist()
        print("✅ Flask generated embedding of length:", len(embedding))
        return jsonify({'embedding': embedding})
    except Exception as e:
        print("❌ Flask embedding failed:", str(e))
        return jsonify({'error': 'Embedding failed', 'message': str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
