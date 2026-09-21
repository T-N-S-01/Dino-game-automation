import numpy as np
import cv2
from mss import mss

# Define capture area and initialize mss
bbox = {'top': 150, 'left': 0, 'width': 900, 'height': 280}
sct = mss()

while True:
    # Capture screen pixels
    img = sct.grab(bbox)

    # Convert to numpy array and fix color (BGRA to BGR)
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    # Display the screen capture live
    cv2.imshow('Screen Capture', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


