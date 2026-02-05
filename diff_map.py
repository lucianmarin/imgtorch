import torch
import torchvision.transforms as T
from PIL import Image
import argparse
import os

def extract_diff_map(img1_path, img2_path, output_path):
    # Load images
    img1 = Image.open(img1_path).convert('RGB')
    img2 = Image.open(img2_path).convert('RGB')

    # Define transforms
    transform = T.Compose([
        T.ToTensor(),
    ])

    # Convert to tensors
    tensor1 = transform(img1)
    tensor2 = transform(img2)

    # Ensure same size
    if tensor1.shape != tensor2.shape:
        print(f"Resizing image 2 from {tensor2.shape[1:]} to {tensor1.shape[1:]}")
        resize_transform = T.Resize(tensor1.shape[1:])
        tensor2 = transform(resize_transform(img2))

    # Calculate absolute difference
    diff = torch.abs(tensor1 - tensor2)

    # Convert back to image and save
    diff_img = T.ToPILImage()(diff)
    diff_img.save(output_path)
    print(f"Difference map saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract difference map between two images using PyTorch.")
    parser.add_argument("img1", help="Path to the first image")
    parser.add_argument("img2", help="Path to the second image")
    parser.add_argument("--output", default="diff_map.jpg", help="Path to save the output difference map")

    args = parser.parse_args()

    if not os.path.exists(args.img1) or not os.path.exists(args.img2):
        print("Error: One or both input images do not exist.")
    else:
        extract_diff_map(args.img1, args.img2, args.output)
