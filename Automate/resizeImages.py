import os
from PIL import Image

size = (50,50)

dstDirectory = os.path.join(r"C:\Users\PC\Desktop\Java\AndroidDevelopment\TicTacToe\app\src\main\res\drawable")
srcDirectory = os.path.join("C:\\", "Users", "PC", "Downloads")

images = ["o"+str(i)+".png" for i in range(1,5)]
images.extend(["x"+str(i)+".png" for i in range(1,5)])
print(images)


for image in [os.path.join(dstDirectory,image) for image in images]:
    # imageName = image.split("\\")[-1]
    os.remove(image)
    # try:
    #     img = Image.open(image)
    #     img.thumbnail(size, Image.ANTIALIAS)

    #     name = "{}_{}x{}.{}".format(imageName.split(".")[0], size[0], size[1], imageName.split(".")[-1])

    #     print("saving {}".format(name))
    #     img.save(os.path.join(dstDirectory, name))
    # except IOError as error:
    #     print("IOError: {}".format(error))


# for image in [os.path.join(srcDirectory,image) for image in images]:
#     imageName = image.split("\\")[-1]
#     try:
#         img = Image.open(image)
#         img.thumbnail(size, Image.ANTIALIAS)

#         name = "{}_{}x{}.{}".format(imageName.split(".")[0], size[0], size[1], imageName.split(".")[-1])

#         print("saving {}".format(name))
#         img.save(os.path.join(dstDirectory, name))
#     except IOError as error:
#         print("IOError: {}".format(error))