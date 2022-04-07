import cv2
import pytesseract
import os

def save_to_directory(p,d):
    img = cv2.imread(p) 
    os.chdir(d) 
    print("Before saving")   
    print(os.listdir(d))   
    filename = 'newFile.png'
    cv2.imwrite(filename, img) 
    print("After saving")  
    print(os.listdir(d))

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
path = r'D:\SIXTHSEMESTERMATERIAL\CVIP\Assignments\ExtractingTextfromanImage\Input\textImage2.png'
directory = r'D:\SIXTHSEMESTERMATERIAL\CVIP\Assignments\ExtractingTextfromanImage\Output'

img = cv2.imread(path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('Result',img)
cv2.waitKey(0)

# Saving to an output directory
save_to_directory(path,directory)

