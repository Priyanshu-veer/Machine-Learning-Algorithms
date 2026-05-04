import torch
from utils import load_model, load_image
from dataset import load_dataset

model = load_model("model/model.pth")
model.eval()

org_images, _ = load_dataset("signatures")

features = []

with torch.no_grad():
    for img_path in org_images:
        img = load_image(img_path)
        feat, _ = model(img, img)   # use forward_once logically
        features.append((img_path, feat))

torch.save(features, "features.pt")

print("Features saved!")