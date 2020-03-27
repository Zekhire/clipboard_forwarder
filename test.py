import pyautogui
import cv2
import numpy as np
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\krzys\AppData\Local\Tesseract-OCR\tesseract.exe'
myScreenshot = pyautogui.screenshot()                           # get screenshot
cv2.imshow("test", np.array(myScreenshot))
cv2.waitKey(0)
# print(pytesseract.image_to_string(Image.open("kawaii.jpg"), lang="jpn"))
#
# i = 0
# while True:
#     print(i)
#     myScreenshot = pyautogui.screenshot()
#     cv2.imshow("y", np.array(myScreenshot))
#     cv2.waitKey(0)
#
#     myScreenshot.save('dupa.jpg')
#     i+=1