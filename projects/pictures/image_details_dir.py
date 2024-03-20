from tkinter import Tk, filedialog
from os import listdir
from os.path import join
from PIL import Image


def get_image_resolution(image_path):
  """
  Opens the image and returns its width and height as a tuple.

  Args:
      image_path: The path to the image file.

  Returns:
      A tuple containing the image width and height.
  """
  try:
    with Image.open(image_path) as image:
      return image.width, image.height
  except OSError:
    # Handle potential errors like corrupted images
    print(f"Error opening image: {image_path}")
    return None


def list_images_with_resolution(directory):
  """
  Lists all image files in a directory and prints their resolution.

  Args:
      directory: The path to the directory containing images.
  """
  num_files = 0
  for filename in listdir(directory):
    num_files += 1  # Count all files in the directory
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
      image_path = join(directory, filename)
      width, height = get_image_resolution(image_path)
      if width and height:
        print(f"{filename}: {width}x{height}")

  # Print the total number of files after iterating through all entries
  print(f"\nTotal files in the directory: {num_files}")


def select_folder():
  """
  Opens a file dialog to select a directory and calls list_images_with_resolution.
  """
  root = Tk()
  root.withdraw()  # Hide the main window
  directory = filedialog.askdirectory(title="Select Image Folder")
  if directory:
    list_images_with_resolution(directory)


if __name__ == "__main__":
  select_folder()
