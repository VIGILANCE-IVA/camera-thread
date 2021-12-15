from setuptools import find_packages, setup

setup(
    name='camera_threading',
    packages=find_packages(include=['camera_threading']),
    version='0.1.0',
    description='Simply open camera as anew thread',
    author='Paul Jeremiah Mugaya',
    install_requires=['pyee', 'opencv-python==4.1.1.26'],
    license='MIT',
)
