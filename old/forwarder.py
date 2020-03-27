# from __future__ import print_function
import cv2.cv2 as cv2
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyautogui
import numpy as np
from selenium import webdriver
import time
from desktopmagic.screengrab_win32 import (
getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
getRectAsImage, getDisplaysAsImages)



# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9114 --user-data-dir="D:\SelenTest\Chrome_Test_profile"


def adjustImage(entireScreen, monitor=1):
    entireScreen = np.array(entireScreen)
    h, w, _ = entireScreen.shape
    if w > 1500:
        entireScreen = entireScreen[:, :int(w/2)]

    return entireScreen


def changeValue(edge, epsilon, a1, a2, a3, a4, n1, n2, n3, n4, m, s):
    if edge == n1 or edge == n2:
        return a1, a2, a3, a4
    elif edge == n3:
        if a1 + (m * epsilon) >=0 and a1 + (m * epsilon) <= s:
            a1 += m*epsilon
    elif edge == n4:
        if a2 + (m * epsilon) >= 0 and a2 + (m * epsilon) <= s:
            a2 += m*epsilon
    return a1, a2, a3, a4

def calibration(x1, y1, x2, y2):
    edge = 1
    epsilon = 1
    show = True
    #           2 y1
    #   1 x1      +     3 x2
    #           4 y2

    while True:
        entireScreen = getScreenAsImage()
        entireScreen = adjustImage(entireScreen)
        h, w, _ = entireScreen.shape
        cv2.rectangle(entireScreen, (x1, y1), (x2, y2), (255, 255, 0), 2)
        # cv2.imshow("a", entireScrefen[y1:y2, x1:x2])
        cv2.imshow("a", entireScreen)
        k = cv2.waitKey(30)
        if k == ord("q"):
            break
        #                                                                               +  +  +  +
        elif k == ord("w"): y1, y2, x1, x2 = changeValue(edge, epsilon, y1, y2, x1, x2, 1, 3, 2, 4, -1, h)
        elif k == ord("a"): x1, x2, y1, y2 = changeValue(edge, epsilon, x1, x2, y1, y2, 2, 4, 1, 3, -1, w)
        elif k == ord("s"): y1, y2, x1, x2 = changeValue(edge, epsilon, y1, y2, x1, x2, 1, 3, 2, 4, 1,  h)
        elif k == ord("d"): x1, x2, y1, y2 = changeValue(edge, epsilon, x1, x2, y1, y2, 2, 4, 1, 3, 1,  w)
        elif k == ord("1"): edge = 1
        elif k == ord("2"): edge = 2
        elif k == ord("3"): edge = 3
        elif k == ord("4"): edge = 4
        elif k == ord("+"):
            if epsilon < 19:
                epsilon += 1
        elif k == ord("-"):
            if epsilon > 1:
                epsilon -= 1
        # elif k == ord("e"):
        #     show = not show
        # if show:
        print(edge, epsilon, x1, x2, y1, y2)
    cv2.destroyAllWindows()

    file = open("window.txt", "w")
    file.write(str(x1) + " " + str(x2) + " " + str(y1) + " " + str(y2))

    return x1, y1, x2, y2

def forwarder():
    # setup

    # tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\krzys\AppData\Local\Tesseract-OCR\tesseract.exe'

    # selen
    # options = webdriver.ChromeOptions()
    # options.add_argument("--disable-extensions")

    #============================================
    # chrome_options = webdriver.ChromeOptions()
    # # chrome_options.add_argument(r"C:\Users\krzys\AppData\Local\Google\Chrome\User Data\Default")
    # chrome_options.add_extension(r"C:\Users\krzys\AppData\Local\Google\Chrome\User Data\Default\Extensions\clidkjbfdlffpbbhlalnkifiehenkjaj\4.0.3_0.crx")
    #
    # driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)
    # driver.get("https://translate.google.pl/?hl=pl&tab=TT0")
    # search_input_box = driver.find_element_by_id("source")
    # ============================================
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9114")
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=chrome_options)
    driver.get("https://translate.google.pl/?hl=pl&tab=TT0")  # <---
    search_input_box = driver.find_element_by_id("source")  # <---

    # calibration
    entireScreen = getScreenAsImage()
    entireScreen = adjustImage(entireScreen)
    h, w, _ = entireScreen.shape
    x1, x2, y1, y2 = 0, w, 0, h
    try:
        lines = [line.rstrip('\n') for line in open("window.txt")]
        split = lines[0].split()
        x1, x2, y1, y2 = int(split[0]), int(split[1]), int(split[2]), int(split[3])
    except:
        x1, x2, y1, y2 = 0, w, 0, h
    x1, y1, x2, y2 = calibration(x1, y1, x2, y2)

    dialogOld = None
    # appropriate part of code
    while True:
        time.sleep(2)
        myScreenshot = getScreenAsImage()                           # get screenshot
        myScreenshot = adjustImage(myScreenshot)
        myScreenshot = np.array(myScreenshot)[y1:y2, x1:x2]



        dialog = pytesseract.image_to_string(myScreenshot, lang="jpn")  # get text from screenshot
        print(dialog)

        if dialogOld != dialog:
            search_input_box.clear()
            search_input_box.send_keys(dialog)                              # write string to input box
        cv2.imshow("a", myScreenshot)
        k = cv2.waitKey(30)
        if k == ord("c"):
            x1, y1, x2, y2 = calibration(x1, y1, x2, y2)

        dialogOld = dialog

if __name__ == "__main__":
    # entireScreen = getScreenAsImage()
    # entireScreen = adjustImage(entireScreen)
    # h, w, _ = entireScreen.shape
    # x1, y1, x2, y2 = calibration(0, 0, w, h)
    forwarder()