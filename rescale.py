import cv2 as cv

img = cv.imread('photos/IMG_9750.JPG')
cv.imshow('Human', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#Change Resolutin
    '''
def changeRes(width,height):
    #Live Video
    capture.set(3,width)
    capture.set(4,height)
    '''
#Reading videos
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
capture = cv.VideoCapture('Videos/pertama.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = .2) ##add scale = .2 to resize

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) % 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()