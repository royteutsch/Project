from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

drawing = svg2rlg("C:/Users/teuts/PycharmProjects/Project/svg-svgrepo-com.svg")
renderPM.drawToFile(drawing, "temp.png", fmt="PNG")


from tkinter import *

tk = Tk()


from PIL import Image, ImageTk

img = Image.open('temp.png')
pimg = ImageTk.PhotoImage(img)
size = img.size


frame = Canvas(tk, width=size[0], height=size[1])
frame.pack()
frame.create_image(0,0,anchor='nw',image=pimg)

tk.mainloop()
