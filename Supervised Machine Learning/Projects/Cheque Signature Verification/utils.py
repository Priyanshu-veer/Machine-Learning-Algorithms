import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
import torchvision.transforms as transforms

# Image Transform
def get_transform():
    return transforms.Compose([
        transforms.Resize((300, 300)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])


# Siamese Network
class SiameseNetwork(nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()

        self.conv_layer = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((4, 4))
        )

        self.fc_layer = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 4 * 4, 256),
            nn.ReLU(),
            nn.Linear(256, 128)
        )

    def forward_once(self, x):
        x = self.conv_layer(x)
        x = self.fc_layer(x)
        return x

    def forward(self, x1, x2):
        out1 = self.forward_once(x1)
        out2 = self.forward_once(x2)
        return out1, out2


# Load Image
def load_image(file):
    if isinstance(file, str):
        img = Image.open(file).convert("L")
    else:
        img = Image.open(file).convert("L")

    transform = get_transform()
    img = transform(img).unsqueeze(0)
    return img


# Load Model
def load_model(model_path="model/model.pth"):
    model = SiameseNetwork()
    model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
    model.eval()
    return model


# Test Two Images
def test_pair(img1_path, img2_path, model, threshold=1.0):

    img1 = load_image(img1_path)
    img2 = load_image(img2_path)

    with torch.no_grad():
        out1, out2 = model(img1, img2)
        distance = F.pairwise_distance(out1, out2).item()

    print("\n--- Result ---")
    print("Image 1:", img1_path)
    print("Image 2:", img2_path)
    print("Distance:", round(distance, 4))

    if distance < threshold:
        print("✔ MATCH (Same Writer)")
    else:
        print("❌ NOT MATCH (Forged/Different Writer)")

    print("-" * 40)

    return distance