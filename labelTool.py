# -*- coding: utf-8 -*-
"""

This is a image labelTool script file.
parameter:  
      labelMap :   a dict like {0:'other',1:'cat',2:'dog',3:'car'}
      path :       image dir
This script will create some dirs in path. Each of those dirs will store pictures of one class in labelMap 
"""
from __future__ import print_function
import cv2
import os
import shutil

def createDir(path,labelMap):
    
    if(not isinstance(labelMap,dict)):
        print("labelMap must be a dict.....like {0:'cat',1:'dog'}")
        return False
    if(not os.path.exists(path)):
        print("{} is not exists!!!".format(path))
        return False
    for k,v in zip(labelMap.keys(),labelMap.values()):
        classPath = os.path.join(path,v)
        if(not os.path.exists(classPath)):
            os.mkdir(classPath)
    return True

        
def dealFile(filePath,labelMap):
    home = os.path.dirname(filePath)
    print("0-9 is setelct class , blank is pass,Esc is quit ")
    print(labelMap)
    while(1):
        key = cv2.waitKey(0)
        key = key - 0x30
        if(key >= 0 and key < len(labelMap)) or key== -21 or key==-16 : break
        print(key)
    

    print(labelMap,key)
    if(key==-16): return
    dst = os.path.join(home,labelMap[key])
    shutil.copy(filePath,dst)
    return

def select(path,labelMap):
    
    if(not createDir(path,labelMap)):
        return
    postfix = ('.jpg','png','.bmp')
    fileNames = os.listdir(path)
    for filename in fileNames:
        if(not filename.endswith(postfix)):
            continue
        filePath = os.path.join(path,filename)
        img = cv2.imread(filePath)
        cv2.imshow(str(filename),img)
        dealFile(filePath,labelMap)
        cv2.destroyAllWindows()
       
if __name__ == "__main__":
    labelMap = {0:'other',1:'cat',2:'dog',3:'car'}
    path = "C:\\workspace\\testSelect"
    select(path,labelMap)
        