import sys
import cv2
from asciitools import *


def isImage(filename):
 endings = [".jpg", ".png", ".bmp"]
 for i in endings:
  if filename.endswith(i):
   return True
 return False

def isVideo(filename):
 endings = [".avi", ".webm", ".mp4", ".mkv"]
 for i in endings:
  if filename.endswith(i):
   return True
 return False

def showAsciiImage(img):
 img_height = len(img)
 img_width = len(img[0])

 (term_width, term_height) = getTerminalSize()

 offset_x = int(img_width / term_width)
 offset_y = int(img_height / (term_height * 2))

 for y in range(term_height):
  for x in range(term_width):
   setCursorPos(x, y)

   img_pos_x = x * offset_x
   img_pos_y = y * 2 * offset_y

   bb = img[img_pos_y][img_pos_x][0]
   bg = img[img_pos_y][img_pos_x][1]
   br = img[img_pos_y][img_pos_x][2]
   setBackgroundColor(br, bg, bb)

   img_pos_y += 1

   fb = img[img_pos_y][img_pos_x][0]
   fg = img[img_pos_y][img_pos_x][1]
   fr = img[img_pos_y][img_pos_x][2]
   setForegroundColor(fr, fg, fb)

   sys.stdout.write("▄")

def showAsciiVideo(captureObject):
 while True:
  ret, img = captureObject.read()
  if not ret:
   return
  showAsciiImage(img)

if len(sys.argv) > 1:
 filename = sys.argv[1]

 if isImage(filename):
  img = cv2.imread(filename)
  showAsciiImage(img)

 if isVideo(filename):
  cap = cv2.VideoCapture(filename)
  showAsciiVideo(cap)

else:
 cam = cv2.VideoCapture(0)
 showAsciiVideo(cam)
