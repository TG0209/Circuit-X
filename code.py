import numpy as np
import cv2
not_casscade = cv2.CascadeClassifier('casscades/cascadenot.xml')
or_casscade = cv2.CascadeClassifier('casscades/cascadeor.xml')
and_casscade = cv2.CascadeClassifier('casscades/cascadeand.xml')
nor_casscade = cv2.CascadeClassifier('casscades/cascadenor.xml')

xor_casscade = cv2.CascadeClassifier('casscades/cascadexor.xml')
nand_casscade = cv2.CascadeClassifier('casscades/cascadenand.xml')

img = cv2.imread('test2.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
nots = not_casscade.detectMultiScale(gray,1.01,7)
ors = or_casscade.detectMultiScale(gray,2.10,7)
ands = and_casscade.detectMultiScale(gray,2.35,7)
nors = nor_casscade.detectMultiScale(gray,1.05,7)
xors = xor_casscade.detectMultiScale(gray,2.55,32)
nands = nand_casscade.detectMultiScale(gray,1.1,32)
c =0

for (x,y,w,h) in nots:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    c = c+1
for (x,y,w,h) in ors:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    c = c+1
for (x,y,w,h) in ands:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    c = c+1
  
for (x,y,w,h) in nors:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(52,248,248),2)
    c = c+1

for (x,y,w,h) in xors:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
    c = c+1
for (x,y,w,h) in nands:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(240,13,255),2)
    c = c+1
    
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'blue = not gate',(0,50), font, 1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(img,'red = and gate',(0,100), font, 1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(img,'green = or gate',(0,150), font, 1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(img,'yellow = nor gate',(0,200), font, 1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(img,'black = xor gate',(0,250), font, 1,(0,0,0),2,cv2.LINE_AA)
cv2.putText(img,'Total logic gates =' + str(c),(400,50), font, 2,(23,42,255),2,cv2.LINE_AA)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()