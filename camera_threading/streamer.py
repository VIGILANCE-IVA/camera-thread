import threading
import time

import cv2 as cv
from pyee import EventEmitter


class Capture(threading.Thread):

    def __init__(self, source=0, delay=0):
        super(Capture, self).__init__()
        self.__flag = threading.Event()  # The flag used to pause the thread
        self.__flag.set()  # Set to True
        self.__running = threading.Event()  # Used to stop the thread identification
        self.__running.set()  # Set running to True
        self.emitter = EventEmitter()
        self.delay = delay
        self.source = source
        self.resolution = {
            '3': 640,
            '4': 480
        }

    def on(self, event, f):
        # run all events
        self.emitter.on(event, f)

    def emit(self, event, *args, **kwargs):
        self.emitter.emit(event, *args, **kwargs)

    def set(self, key, value):
        self.resolution[str(key)] = value

    def make_1080p(cap):
        cap.set(3, 1920)
        cap.set(4, 1080)
        return cap

    def make_720p(cap):
        cap.set(3, 1280)
        cap.set(4, 720)
        return cap

    def make_480p(cap):
        cap.set(3, 640)
        cap.set(4, 480)
        return cap

    def change_res(cap, width, height):
        cap.set(3, width)
        cap.set(4, height)
        return cap

    def run(self):
        if str(self.source).isdigit():
            self.source = int(self.source)

        # capture stream
        capture = cv.VideoCapture(self.source)

        # resolution
        capture.set(3, self.resolution['3'])
        capture.set(4, self.resolution['4'])

        while self.__running.isSet():
            self.__flag.wait()  # return immediately when it is True, block until the internal flag is True when it is False
            ret, frame = capture.read()
            if self.source == 0:
                frame = cv.flip(frame, 1)  # flip if webcam

            # In case the image is not read properly
            if not ret:
                continue

            self.emit("frame", frame)

            if cv.waitKey(1) and 0xff == ord('q'):
                exit = True
                break

            time.sleep(int(self.delay))  # By time.sleep(1) you repeat the loop every 1 sec.

        capture.release()
        cv.destroyAllWindows()

    def pause(self):
        self.__flag.clear()  # Set to False to block the thread

    def resume(self):
        self.__flag.set()  # Set to True, let the thread stop blocking

    def stop(self):
        self.__flag.set()  # Resume the thread from the suspended state, if it is already suspended
        self.__running.clear()  # Set to False
