# AsciiTerminalCam
A python 3 script for displaying images, videos and life video in the linux terminal using OpenCV.
It only supports terminals which can display the full RGB color range, but most modern terminals are able to do this.

# Installation
Make sure OpenCV python is installed.
To install it use the following command:
```bash
pip install opencv-python
```

Then just download the .py files and run asciicam.py.

# Usage
The script can display images and videos.
When no parameter is given it tries to use a webcam. This may require root to run and depends on your system. 

Show image:
```bash
python asciicam.py path/to/image.jpg
```
Show video:
```bash
python asciicam.py path/to/video.mp4
```
Notice that the display speed of the video depends on the size of the terminal.
The larger the Terminal the slower the video.
It may get even slower if you are watching the video over a ssh connection.

Show video from Url:
The url has to end with a video file format (like .mp4 or .avi) in order to function.
This can easily be fixed if you want to change the script a little bit.
```bash
python asciicam.py http://www.domain.com/path/to/video.mp4
```
With no parameters OpenCV tries to open your webcam. In order to do this you may need to run the script as root.
```bash
sudo python asciicam.py
```
