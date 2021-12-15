### Prerequisites

Go ahead and create a virtual environment by typing:  
`> python3 -m venv venv`

Once it is created, you must now activate the environment by using:  
`> source venv/bin/activate`

In your environment, make sure you have pip installed `wheel`, `setuptools` and `twine`. We will need them for later to build our Python library.

> pip install wheel  
> pip install setuptools  
> pip install twine

## Build your library

Now that all the content is there, we want to build our library. Make sure your present working directory is `/path/to/mypythonlibrary` (so the root folder of your project). In your command prompt, run:  
`>` `python setup.py bdist_wheel`

Your wheel file is stored in the “dist” folder that is now created. You can install your library by using:  
`> pip install /path/to/wheelfile.whl`

### SAMPLE

```python

import cv2 as cv

import time

from camera_threading.streamer import Capture



def  on_stream(frame):

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
