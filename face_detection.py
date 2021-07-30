import os
import PIL.Image
import PIL.ImageDraw
import face_recognition
import glob
import cv2
import sys
import time
import concurrent.futures





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

        if number_of_faces!=1:

           #cv2.imwrite(os.path.join(output , g), n)
           os.remove(img)
           print("yes")



def main(path):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for sub_path in glob.glob(path+"/*"):
            print(sub_path)
            for img in glob.glob(sub_path+"/*.jpg"):
                 
            
                executor.submit(remover, img)
                
                


  # block until all the threads finish (i.e. block until all function_x calls finish)    

def ender():
    print("The Done ")
    

if __name__ == "__main__":
   path=sys.argv[1]
   main(path)


      
ender()
