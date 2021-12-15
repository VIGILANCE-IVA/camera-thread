### prerequisites

> https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f
> Install opencv-python
> Install pyee

### SAMPLE

```python
import cv2 as cv
import time
from camera_threading.streamer import Capture

def on_stream(frame):
    cv.imshow('Frame', frame)

camera = Capture('0', 0)

camera.on("frame", on_stream)

camera.start()

time.sleep(5)
camera.pause()

time.sleep(10)

camera.resume()
time.sleep(50)

camera.pause()
time.sleep(5)

camera.stop()
```
