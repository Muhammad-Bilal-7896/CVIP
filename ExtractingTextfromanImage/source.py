import cv2
import pytesseract
import os

def save_to_directory(p,d):
    img = cv2.imread(p) 
    os.chdir(d) 
    print("Before saving")   
    print(os.listdir(d))   
    filename = 'textDetected.png'
    cv2.imwrite(filename, img) 
    print("After saving")  
    print(os.listdir(d))

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
path = r'D:\SIXTHSEMESTERMATERIAL\CVIP\Assignments\ExtractingTextfromanImage\Input\textImage.png'
directory = r'D:\SIXTHSEMESTERMATERIAL\CVIP\Assignments\ExtractingTextfromanImage\Output'

img = cv2.imread(path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#we will print first
#print(pytesseract.image_to_string(img))

### Detecting Characters
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    cv2.putText(img,b[0],(x,hImg-y+20),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)

save_to_directory(path,directory)


cv2.imshow('Result',img)
cv2.waitKey(0)

# Saving to an output directory
save_to_directory(path,directory)

