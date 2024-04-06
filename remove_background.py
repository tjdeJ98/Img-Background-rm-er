from rembg import remove
from PIL import Image, ImageTk
from tkinter import Tk, Label


# input_path = r'941f9626-aed4-4592-8ec5-6fed1d340654.jpeg'
# output_path = 'output.png'

# input_image = Image.open(input_path)  # Use a descriptive variable name
# output = remove(input_image)
# output.save(output_path)
root = Tk()
root.title("Image Background Remover")
root.minsize(800, 400)

text = Label(root, text="Image background remover")
text.pack()
text2 = Label(root, text=" - By Timo de Jong")
text2.pack()

image = Image.open("TimoRome.jpeg")
image_resized = image.resize(
    (int(image.width/2), int(image.height/2)), Image.Resampling.BOX)
image = ImageTk.PhotoImage(image_resized)
img = Label(root, image=image)
img.pack()


root.mainloop()
