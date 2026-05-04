import streamlit as st
import torch
import torch.nn.functional as F
from utils import load_model, load_image
import os

st.set_page_config(
    page_title="Cheque Signature Verification",
    layout="centered"
)

# Load model
@st.cache_resource
def get_model():
    return load_model("model/model.pth")

model = get_model()


# Load precomputed features
features = torch.load("features.pt")


# UI

st.title("✍️ Fast Signature Verification")

uploaded_file = st.file_uploader("Upload Signature", type=["png", "jpg", "jpeg"])

threshold = st.slider("Threshold", 0.0, 3.0, 1.0)

# VERIFY BUTTON
verify = st.button("VERIFY SIGNATURE")


# Prediction only on button click
if uploaded_file and verify:

    test_img = load_image(uploaded_file)

    with torch.no_grad():
        test_feat, _ = model(test_img, test_img)

        best_match_path = None
        min_dist = float("inf")

        for img_path, ref_feat in features:
            dist = F.pairwise_distance(test_feat, ref_feat).item()

            if dist < min_dist:
                min_dist = dist
                best_match_path = img_path

    
    # Extract label
    label = os.path.basename(best_match_path)

    # Output
    st.subheader(f"Best Match Distance: {round(min_dist, 4)}")

    if min_dist < threshold:
        st.success(f"✔ Verified with: {label}")
    else:
        st.error("❌ Forged Signature")