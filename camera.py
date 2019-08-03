import cv2 as cv

class VideoCamera(object):
    def __init__(self):
        self.video = cv.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv.imencode('.jpg', image)
        return jpeg.tobytes()
