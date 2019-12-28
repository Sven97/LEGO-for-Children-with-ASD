import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def callback(x):
    pass


cv2.namedWindow("TrackBar")
cv2.createTrackbar("LH", "TrackBar", 0, 255, callback)
cv2.createTrackbar("LS", "TrackBar", 0, 255, callback)
cv2.createTrackbar("LV", "TrackBar", 0, 255, callback)
cv2.createTrackbar("UH", "TrackBar", 255, 255, callback)
cv2.createTrackbar("US", "TrackBar", 255, 255, callback)
cv2.createTrackbar("UV", "TrackBar", 255, 255, callback)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("LH", "TrackBar")
    lower_s = cv2.getTrackbarPos("LS", "TrackBar")
    lower_v = cv2.getTrackbarPos("LV", "TrackBar")

    upper_h = cv2.getTrackbarPos("UH", "TrackBar")
    upper_s = cv2.getTrackbarPos("US", "TrackBar")
    upper_v = cv2.getTrackbarPos("UV", "TrackBar")

    lower_hsv = np.array([lower_h, lower_s, lower_v])
    upper_hsv = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Suggested hsv boundary values for different colors

# red
# LH 0
# LS 100
# LV 0
# UH 10
# US 255
# UV 255

# blue
# LH 91
# LS 104
# LV 65
# UH 127
# US 255
# UV 255

# green
# LH 47
# LS 97
# LV 28
# UH 90
# US 255
# UV 255
