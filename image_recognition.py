import cv2
import numpy as np
import requests

def bincount_app(a): # It returnes the most commom color in the image 'a'
    a2D = a.reshape(-1,a.shape[-1])
    col_range = (256, 256, 256) # generically : a2D.max(0)+1
    a1D = np.ravel_multi_index(a2D.T, col_range)
    return np.unravel_index(np.bincount(a1D).argmax(), col_range)
#==========================================SETTINGS===================================================

def look_thumb_img(image_link):
    image = requests.get(image_link)
    image = cv2.imread(image)
    a2D = image.reshape(-1,image.shape[-1])
    col_range = (256, 256, 256) # generically : a2D.max(0)+1
    a1D = np.ravel_multi_index(a2D.T, col_range)

    return np.unravel_index(np.bincount(a1D).argmax(), col_range)

def look_for_faces(image_link):
    image = requests.get(image_link)
    carregaAlgoritmo = cv2.CascadeClassifier(r'C:\Users\marqu\Documents\Coding\Youtube\Files\haarcascade_frontalface_default.xml')
    
    image = cv2.imread(image)
    
    imageGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = carregaAlgoritmo.detectMultiScale(imageGrey, scaleFactor=1.05, minNeighbors=4, minSize=(25,25))
    
    print(type(faces))
    
    for(x, y, l, a) in faces:
        cv2.rectangle(image, (x,y), (x+l, y+a), (255,0,255), 2)
    
    
    cv2.namedWindow("Faces", cv2.WINDOW_NORMAL)
    
    cv2.setWindowProperty("Faces",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty("Faces",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_NORMAL)
    cv2.imshow("Faces", image)
    # cv2.waitKey()
    cv2.destroyWindow("Faces")

    if len(faces) > 0:
        faces = True
    else:
        faces = False

    return faces

#teste
test_image =(r"C:\Users\marqu\Documents\Coding\OpenCVScript\fotos\imagem1.jpg")

print(look_thumb_img(test_image))
print(look_for_faces(test_image))
