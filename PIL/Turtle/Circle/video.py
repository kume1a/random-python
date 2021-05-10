import cv2
import os

mult = 2
fps = 30
image_folder = '..\\Mult{}'.format(mult)
video_name = '{}fps{}.avi'.format(fps, mult)

images = ["image{}.jpg".format(i) for i in range(1,200)]

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, fps, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()