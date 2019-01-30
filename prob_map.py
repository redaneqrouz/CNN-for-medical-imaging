# testing the model importation 
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

# for testing the model in big image 760*400 by window sliding and color notation 
from PIL import Image
import sys
import copy

# for rune time execution 
import time
start = time.time()


    
def pixel_predicte(picture,prob):
    p = float(prob)
    #picture = cv2.imread(picture, cv2.IMREAD_GRAYSCALE)
    #picture = cv2.applyColorMap(picture, cv2.COLORMAP_JET)
    if p > 0.3 and p < 0.5:
        picture = cv2.applyColorMap(picture, cv2.COLORMAP_WINTER)
    elif p > 0.5 and p < 0.8:
        picture = cv2.applyColorMap(picture, cv2.COLORMAP_SUMMER)
    elif p > 0.8:
        picture = cv2.applyColorMap(picture, cv2.COLORMAP_AUTUMN)
    picture = cv2.resize(picture, (28,28))
    return picture


# import argument 
    # first argument is the model
modele_= sys.argv[1]
    #  second the image
img  = sys.argv[2]

image = cv2.imread(img)

stepSize = 28
x_offset=y_offset=28
i = 0

def sliding_window(image, stepSize, windowSize):
    # slide a window across the image
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
        # yield the current window
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])
            
winW = winH = 28

    # loop over the sliding window for each layer of the pyramid
model = load_model(modele_)
for (x, y, window) in sliding_window(image, stepSize=28, windowSize=(winW, winH)):
        # if the window does not meet our desired window size, ignore it
    if window.shape[0] != winH or window.shape[1] != winW:
        continue
    wino = window.copy()
    window = window.astype("float") / 255.0
    window = img_to_array(window)
    window = np.expand_dims(window, axis=0)
    print("[INFO] loading network...",i)
    i+=1
    # classify the input image
    (benign, malign) = model.predict(window)[0]
    label = "benign" if benign > malign else "malign"
    proba = benign if benign > malign else malign
    if label is "benign":
        i_mg = wino
    elif label is "malign":
        i_mg = pixel_predicte(wino,proba)
    image[y:y+winH, x:x+winH] = i_mg
    #if(i%100 == 0):
     #   cv2.imwrite('outputa.png',image)



# end time execution 
end = time.time()
print(end - start)
 
# draw the label on the image
#output = imutils.resize(orig, width=400)
#cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,	0.7, (0, 255, 0), 2)
 
# show the output image
#cv2.imshow("output image", image)
#cv2.imshow("input image", img)
cv2.imwrite('output.png',image)
#cv2.imwrite('input.png',img)
cv2.waitKey(0)
exit(0)
