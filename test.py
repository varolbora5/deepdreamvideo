import cv2
from PIL import Image
import os

cap = cv2.VideoCapture("video.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)

im = Image.open('./deep_image/deepframe0.jpg')

print(im.size)
print(type(im.size))
w, h = im.size

fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (w, h))
for root, dirs, files in os.walk("./deep_image"):
    for file in files:
        image = cv2.imread(file)
        frame = cv2.resize(image, (w, h))
        out.write(frame)
out.release()
cv2.destroyAllWindows()
