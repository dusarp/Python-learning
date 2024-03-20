from PIL import Image
import tkinter as tk
from tkinter import filedialog

def get_image_details(filepath):
  """
  This function takes an image filepath and returns a dictionary containing image details.
  """
  try:
    with Image.open(filepath) as image:
      width, height = image.size
      format = image.format
      return {
          "Width": width,
          "Height": height,
          "Format": format,
      }
  except FileNotFoundError:
      print(f"Error: File not found - {filepath}")
      return {}

def open_file():
  """
  This function opens a file dialog and retrieves the selected image filepath.
  Then, it calls get_image_details to get properties and prints them to the terminal.
  """
  filepath = filedialog.askopenfilename(
      title="Select Image",
      filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
  )
  if filepath:
    details = get_image_details(filepath)
    if details:
      print("Image Details:")
      for key, value in details.items():
        print(f"{key}: {value}")

def main():
  # Create the main window (hidden)
  window = tk.Tk()
  window.withdraw()  # Hide the main window

  open_file()  # Call the function to open file dialog

  window.mainloop()  # Start the event loop (but window is hidden)

if __name__ == "__main__":
  main()
