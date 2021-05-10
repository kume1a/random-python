# with open(r"C:\Users\Administrator\Desktop\Python\Gui\bote\binr.txt", "wb") as f:
#     with open(r"C:\Users\Administrator\Desktop\yvelaferi\gio.mp4", "rb") as file:
#         f.write(file.read())


with open(r"C:\Users\Administrator\Desktop\Python\Gui\bote\binr.txt", "rb") as f:
    binary = f.read()


with open("bote.mp4", "wb") as file:
    file.write(binary)
