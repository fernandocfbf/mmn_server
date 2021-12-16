import cv2
import matplotlib.pyplot as plt

def image_show(img):
    '''
    input: image to show (array)
    output: empty
    description: show the image using open cv
    '''
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(25,7.5)), plt.imshow(img), plt.axis('off')