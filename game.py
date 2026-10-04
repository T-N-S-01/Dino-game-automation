import cv2
import mss
import numpy as np
import pyautogui
import time

game_window = {"top": 150, "left": 100, "width": 740, "height": 195}
jump_ready = False

def preprocess(img):

    roi = img[130:305, 225:280]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    count = cv2.countNonZero(thresh)
    cv2.imshow("Thresh", roi)

    if count > 50:
        return True

    return False


with mss.MSS() as sct:
    while True:
        if jump_ready and (time.time() - t > 0.18):
            pyautogui.press('space')
            jump_ready = False

        img = np.array(sct.grab(game_window))
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        has_detected = preprocess(frame)

        if has_detected and not jump_ready:
            jump_ready = True
            t = time.time()

        cv2.imshow("Full Screen", img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cv2.destroyAllWindows()