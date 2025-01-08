from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk
import os

# Initialize the main window
root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of image file names in the same project folder
image_paths = [
    "images1.jpg",
    "images2.jpg",
    "images3.jpg",
    "images4.jpg",
    "images5.jpg"
]

# Check which files exist
existing_files = [path for path in image_paths if os.path.exists(path)]
if not existing_files:
    print("No valid image files found. Please check the folder contents.")
    root.destroy()  # Exit if no images are available
    exit()

# Resize the images to 1080x1080
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in existing_files]
photo_images = [ImageTk.PhotoImage(image) for image in images]

# Create a cycle iterator for the images
slideshow = cycle(photo_images)

# Create a label to display the images
label = tk.Label(root)
label.pack()

def update_image():
    """Update the label with the next image in the slideshow."""
    next_image = next(slideshow)
    label.config(image=next_image)
    # Schedule the next image update after 3000ms (3 seconds)
    root.after(3000, update_image)

def start_slideshow():
    """Start the slideshow by calling update_image."""
    update_image()

# Add a button to start the slideshow
play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

# Run the Tkinter main loop
root.mainloop()
