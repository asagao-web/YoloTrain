import os
import shutil
import random
import sys


def main(project_dir, train_ratio=0.8):
    # Define the source directory and the target directories
    source_dir = os.path.join(project_dir, "images")
    train_images_dir = os.path.join(project_dir, "img/train/images")
    train_labels_dir = os.path.join(project_dir, "img/train/labels")
    valid_images_dir = os.path.join(project_dir, "img/valid/images")
    valid_labels_dir = os.path.join(project_dir, "img/valid/labels")

    # Check if directories exist
    directories = [source_dir, train_images_dir, train_labels_dir, valid_images_dir, valid_labels_dir]
    for directory in directories:
        if not os.path.isdir(directory):
            print(f"Error: Directory {directory} does not exist.")
            return

    # Get a list of all image and label files
    all_files = os.listdir(source_dir)
    image_files = [f for f in all_files if f.endswith('.jpg')]
    label_files = [f for f in all_files if f.endswith('.txt')]

    # Ensure each image file has a corresponding label file
    base_names = [os.path.splitext(f)[0] for f in image_files]
    if not all(name + '.txt' in label_files for name in base_names):
        print("Error: Some image files do not have corresponding label files.")
        return

    # Shuffle the base names
    random.shuffle(base_names)

    # Split the base names into training and validation sets
    num_train = int(len(base_names) * train_ratio)
    train_base_names = base_names[:num_train]
    valid_base_names = base_names[num_train:]

    # Copy the files to the appropriate directories
    for base_name in train_base_names:
        shutil.copy(os.path.join(source_dir, base_name + '.jpg'), train_images_dir)
        shutil.copy(os.path.join(source_dir, base_name + '.txt'), train_labels_dir)
    for base_name in valid_base_names:
        shutil.copy(os.path.join(source_dir, base_name + '.jpg'), valid_images_dir)
        shutil.copy(os.path.join(source_dir, base_name + '.txt'), valid_labels_dir)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <project_dir>")
    else:
        main(sys.argv[1])
