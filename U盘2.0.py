import os  #系统操作模块
from win32 import *
from win32api import GetLogicalDriveStrings
from win32file import *

num = 1
for root,ds,fs in os.walk("C:\\"):
   print("根目录：",root)
   print("文件夹：",ds)
   print("文件：",fs)
   for video in fs:
      try:
            if video.lower().endwith((".png")) :
             A = root + "\\" + video
             B = "F:\\" + video
             CopyFile(A,B,False)  #遇到相同文件跳过
             print(f"install the {num} file")
             num = num+1
      except:
         exit()