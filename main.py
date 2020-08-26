import cv2
import os
import requests
cam = cv2.VideoCapture('./video.mp4')
try:
    if not os.path.exists('image_data'):
        os.makedirs('image_data')
except OSError:
    print('Error: Creating directory of image_data')
try:
    if not os.path.exists('deep_image'):
        os.makedirs('deep_image')
except OSError:
    print('Error: Creating directory of deep_image')


currentframe = 0

while True:
    ret, frame = cam.read()
    if ret:
        name = './image_data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        cv2.imwrite(name, frame)

        currentframe += 1
        allframes = currentframe
    else:
        break
cam.release()
cv2.destroyAllWindows()

currentframe = 0
while True:
    if currentframe <= allframes:
        r = requests.post(
            "https://api.deepai.org/api/deepdream",
            files={
                'image': open('./image_data/frame' + str(currentframe) + '.jpg', 'rb'),
            },
            headers={'api-key': '90a0b43f-569f-4cc5-8d11-93b8723005d6'}
        )
        response = r.json()
        print(response)

        imagelink = requests.get(response['output_url'])

        file = open("./deep_image/" + str(currentframe) + '.jpg', "wb")
        file.write(imagelink.content)
        file.close()
        currentframe += 1
    else:
        break
