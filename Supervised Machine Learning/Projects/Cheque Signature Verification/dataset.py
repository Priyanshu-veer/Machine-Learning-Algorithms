import os


def load_dataset(root_path):
    """
    Returns:
        org_images: list of genuine image paths
        forg_images: list of forged image paths
    """

    org_path = os.path.join(root_path, "full_org")
    forg_path = os.path.join(root_path, "full_forg")

    if not os.path.exists(org_path):
        raise FileNotFoundError(f"Missing folder: {org_path}")
    if not os.path.exists(forg_path):
        raise FileNotFoundError(f"Missing folder: {forg_path}")

    org_images = []
    forg_images = []

    # Load genuine images
    for filename in os.listdir(org_path):
        if filename.lower().endswith(".png"):
            org_images.append(os.path.join(org_path, filename))

    # Load forged images
    for filename in os.listdir(forg_path):
        if filename.lower().endswith(".png"):
            forg_images.append(os.path.join(forg_path, filename))

    return org_images, forg_images


# Test
if __name__ == "__main__":
    org, forg = load_dataset("C:/Users/lanovo/Desktop/ML Algorithms/Machine Learning/Supervised Machince Learning/Projects/Cheque verification/signatures")

    print("Total Genuine:", len(org))
    print("Total Forged:", len(forg))

