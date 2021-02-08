import cv2 as cv

#img = cv.imread('photos/IMG_9750.JPG')

capture = cv.VideoCapture('Videos/pertama.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

#cv.imshow('Human', img)

cv.waitKey(0)