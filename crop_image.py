# Import necessary libraries
from PIL import Image
import os
import sys

def crop_image(input_path, output_path, size, section):
    # Open the image
    with Image.open(input_path) as img:
        width, height = img.size

        # Define coordinates based on section
        if section == 'center':
            left = (width - size[0]) // 2
            top = (height - size[1]) // 2
        elif section == 'top-right':
            left = width - size[0]
            top = 0
        elif section == 'bottom-right':
            left = width - size[0]
            top = height - size[1]
        else:
            raise ValueError("Unsupported section. Choose 'center', 'top-right', or 'bottom-right'.")

        right = left + size[0]
        bottom = top + size[1]

        # Crop the image
        img_cropped = img.crop((left, top, right, bottom))

        # Save the cropped image
        img_cropped.save(output_path)
        print(f"Cropped image saved to {output_path}")

def main():
    # Check command line arguments
    if len(sys.argv) != 4:
        print("Usage: python crop_images.py <section> <crop_width> <crop_height>")
        sys.exit(1)

    section = sys.argv[1]
    crop_width = int(sys.argv[2])
    crop_height = int(sys.argv[3])
    size = (crop_width, crop_height)

    input_dir = "./datasets/test_data"
    output_dir = "./crop_images"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            crop_image(input_path, output_path, size, section)

if __name__ == "__main__":
    main()
