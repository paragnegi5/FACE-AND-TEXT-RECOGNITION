import pytesseract
import PIL
import cv2 as cv
from PIL import Image, ImageDraw
face_cascade=cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade=cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_input=input("Enter the path of the image: ")
im=Image.open(image_input)
cv_img=cv.imread(image_input)
nom=input("Please choose what you want to extract:- \n1.)Text \n2.)Faces\n")
