#coding:utf-8
__author__ = 'zhangxd18'
import csv,cv2
import sys
import os
import codecs
import re
import Tkinter
import tkMessageBox
import tkFileDialog
import Canvas
from PIL import Image
from PIL import ImageTk

XML_DATA_DIR = r"D:/Python27/Lib/site-packages/cv2/data"
def select_file_path():
    path = tkFileDialog.askopenfilename()
    
    #path = tkFileDialog.askdirectory()
    dstPath.set(path)
    
def start_analyze():
    print dstPath.get()
    #print dir(canvas_dst)
    
    dstFilePath = dstPath.get()
    
    img = cv2.imread(dstFilePath)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    reverse = cv2.bitwise_not(gray)
    
    face_cascade = cv2.CascadeClassifier( os.path.join(XML_DATA_DIR, "haarcascade_frontalface_default.xml") )
    eye_cascade = cv2.CascadeClassifier( os.path.join(XML_DATA_DIR, "haarcascade_eye_tree_eyeglasses.xml") )

    if face_cascade:
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        print "normal face:", faces
        
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale( roi_gray, 1.1, 1, cv2.CASCADE_SCALE_IMAGE,(2,2) )
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 1)
        """
        reverse_faces = face_cascade.detectMultiScale(reverse, 1.3, 5)
        print "reverse face:", reverse_faces
        for face in reverse_faces:
            x, y, w, h = face
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        """
    cv2.imshow("img", img)
    
    #tkMessageBox.showinfo('tips', '分析结束')


if __name__ == "__main__":
    #print sys.argv[1]

    root = Tkinter.Tk()
    dstPath = Tkinter.StringVar()
    
    #root.withdraw()
    Tkinter.Label(root, text = '目标文件：').grid(row = 0, column = 0)
    Tkinter.Entry(root, textvariable = dstPath).grid(row = 0, column = 1)
    Tkinter.Button(root, text = '文件选择', command = select_file_path).grid(row = 0, column = 2)
    
    Tkinter.Button(root, text = '开始分析', command = start_analyze).grid(row = 1, column = 2)
    
    
    root.mainloop()
    
