import cv2
import numpy as np
import requests
import urllib.request

def bincount_app(a): # It returnes the most commom color in the image 'a'
    a2D = a.reshape(-1,a.shape[-1])
    col_range = (256, 256, 256) # generically : a2D.max(0)+1
    a1D = np.ravel_multi_index(a2D.T, col_range)
    return np.unravel_index(np.bincount(a1D).argmax(), col_range)

def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


#==========================================SETTINGS===================================================

def look_thumb_img(image):
    # image = requests.get(image_link)
    # image = cv2.imread(image)
    a2D = image.reshape(-1,image.shape[-1])
    col_range = (256, 256, 256) # generically : a2D.max(0)+1
    a1D = np.ravel_multi_index(a2D.T, col_range)
    return np.unravel_index(np.bincount(a1D).argmax(), col_range)

def look_for_faces(image):
    carregaAlgoritmo = cv2.CascadeClassifier(r'C:\Users\marqu\Documents\Coding\Youtube\Files\haarcascade_frontalface_default.xml')

    # image = cv2.imread(img)
    # image = np.array(image, dtype=np.uint8)
    imageGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = carregaAlgoritmo.detectMultiScale(imageGrey, scaleFactor=1.05, minNeighbors=4, minSize=(25,25))

    for(x, y, l, a) in faces:
        cv2.rectangle(image, (x,y), (x+l, y+a), (255,0,255), 2)
    
    cv2.namedWindow("Faces", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Faces",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty("Faces",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_NORMAL)
    cv2.imshow("Faces", image)

    cv2.destroyWindow("Faces")

    if len(faces) > 0:
        faces = True
    else:
        faces = False

    return faces

#teste
test_image =(r"C:\Users\marqu\Documents\Coding\OpenCVScript\fotos\imagem1.jpg")

