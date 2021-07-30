from PIL import Image,ImageDraw
import pandas as pd
import glob
import os
import tkinter
from tkinter import filedialog
import face_recognition
import glob
import cv2
import sys
import concurrent.futures


# fields = ["Path"]



def remover(img):  
        cv_img = []
        print(img)

        n= cv2.imread(img)
        cv_img.append(n)
        g = img.split('/')[-1]
        print(g)
        image = face_recognition.load_image_file(img)
        face_locations = face_recognition.face_locations(image)
        number_of_faces = len(face_locations)
        print("I found {} face(s) in this photograph.".format(number_of_faces))

        if number_of_faces>=1:

           #cv2.imwrite(os.path.join(output , g), n)
           os.remove(img)
           print("yes")



def main(path):
    print("========gh=================")
    Names_Num(path)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        
        print(path)
        
        for sub_path in glob.glob(path+"/*"):
#             print("hhhhh--------",sub_path)
            for img in glob.glob(sub_path+"/*.png"):
#                 print("gggggg--------", img)
                executor.submit(remover, img)
                
                
                
def Names_Num(path):
    print("=============")

    n = 0
    b = []
    a = []
 #   print(path)

    for path, subdirs, files in os.walk(path):
  #      print(path)
    #     print(files)

        if n > 0:
            N_c = len(files)
            b.append(N_c)
        n+=1
        for filename in subdirs:
            f = os.path.join( filename)
            a.append(str(f))




    # print(len(b))
    # print(len(a))
    # print(a)
    # print(b)
    final = dict()
    final["folder_name"] = a
    final["image_len"] = b
    df = pd.DataFrame(final)
    print("===================================================aliiiiiiiiiiii")
    np=path.split('/')
    xpath=""
    for i in range(0,len(np)-1):
        xpath+=np[i]+"/"
    print(xpath) 
    df.to_excel(xpath+"Name_and_Images.xlsx")

                
def tk_page():
    

    root = tkinter.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

    return folder_selected



if __name__ =='__main__':
#     root=tk.Tk()
    path = tk_page()
    main(path)
    print("=================",path)
    
#     root.mainloop()
    
    
    
