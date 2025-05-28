import clip
import torch
from PIL import Image

# Setup device (GPU kalau ada, CPU kalau nggak)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model dan preprocess dari repo CLIP
model, preprocess = clip.load("ViT-B/32", device=device)

# Buka gambar yang mau diembed
image = preprocess(Image.open("test.jpg")).unsqueeze(0).to(device)

# Buat token text (bisa diganti sesuai kebutuhan)
text = clip.tokenize(["a photo", "an image"]).to(device)

# Dapatkan fitur (embedding) gambar dan teks
with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)

print("Image features shape:", image_features.shape)
print("Text features shape:", text_features.shape)

# Kalau mau simpan embedding ke file atau kirim ke API, tinggal convert ke list atau numpy
image_embedding = image_features.cpu().numpy().tolist()
print("Example embedding vector:", image_embedding[0][:10])  # contoh 10 dimensi pertama
