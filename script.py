import pytesseract
import PIL
import cv2 as cv
from PIL import Image, ImageDraw
face_cascade=cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade=cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




def text_recognization(im):
    text=pytesseract.image_to_string(im)
    if text=="":
        print("No text found in the image")
    else:
        print(text)




def face_recognization(cv_img):
    faces=face_cascade.detectMultiScale(cv_img,1.35)
    if len(faces)==0:
            print("Results found in file:- ")
            print("There were no faces in that file")
            return
    for i in range(len(faces)):
        x,y,w,h=faces[i]
        image=im.crop((x,y,x+w,y+h))
        size=(200,125)
        if(len(faces)<5):
            if i==0:
                image.thumbnail(size, Image.ANTIALIAS)
                background=Image.new('RGBA',(645,125),(0,0,0))
                background.paste(image)
                background.save("output.png")
                #display(Image.open("output.png"))
            else:
                image.thumbnail(size, Image.ANTIALIAS)
                background.paste(image,(i*size[1],0))
                background.save("output.png")
                #display(Image.open("output.png"))
        else:
            if i==0:
                image.thumbnail(size, Image.ANTIALIAS)
                background=Image.new('RGBA',(625,250),(0,0,0))
                background.paste(image)
                background.save("output.png")
                #display(Image.open("output.png"))
            elif i>0 and i<5:
                image.thumbnail(size, Image.ANTIALIAS)
                background.paste(image,(i*size[1],0))
                background.save("output.png")
                #display(Image.open("output.png"))
            else:
                image.thumbnail(size, Image.ANTIALIAS)
                background.paste(image,((i-5)*size[1],125))
                background.save("output.png")
                #display(Image.open("output.png"))
    print("Results found in file:- ")
    display(Image.open("output.png"))



image_input=input("Enter the path of the image: ")
im=Image.open(image_input)
cv_img=cv.imread(image_input)
nom=input("Please choose what you want to extract:- \n1.)Text \n2.)Faces\n")
if int(nom)==1:
    text_recognization(im)
else:
    face_recognization(cv_img)
