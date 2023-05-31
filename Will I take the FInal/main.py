import operator

import pyautogui as pg
import webbrowser as wb
import time
import pytesseract
import cv2
import numpy as np
import operator as op

# Gets info from aspen

# username = input('Enter your username: ')
# password = input('Enter your password: ')
url = 'https://ri-warwick.myfollett.com/aspen/logon.do'
wb.open(url)
time.sleep(0.6)

# Enter your username and password here

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def find_coordinates_text(text, lang='en'):
    # Take a screenshot of the main screen
    screenshot = pg.screenshot()

    # Convert the screenshot to grayscale
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Find the provided text (text) on the grayscale screenshot
    # using the provided language (lang)
    data = pytesseract.image_to_data(img, lang='eng', output_type='data.frame')

    # Find the coordinates of the provided text (text)
    try:
        x, y = data[data['text'] ==
                    text]['left'].iloc[0], data[data['text'] == text]['top'].iloc[0]

    except IndexError:
        # The text was not found on the screen
        return None

    # Text was found, return the coordinates
    return x, y


login = find_coordinates_text('Login')
y = op.add(int(login[1]),35)
pg.moveTo(login[0], y)
pg.click()
time.sleep(0.4)
pg.typewrite(username)
pg.press('tab')
pg.typewrite(password)
pg.press('enter')

time.sleep(0.5)

text_to_find = 'Academics'
coordinates = find_coordinates_text(text_to_find)

pg.moveTo(coordinates[0], coordinates[1])
pg.click()
