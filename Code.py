import cv2
import random
import time
import dropbox

start_time=time.time()


def main():
    while(True):
        if((time.time()-start_time)>=0):
            name=TakeingPic()
            UploadingImage(name)


        

def TakeingPic():
    cam=cv2.VideoCapture(0)
    result=True
    number=random.randrange(0,100)

    while(result):
       # global start_time
        ret,frame=cam.read()
        image_name="Image"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time()
        result=False
   
    cam.release()
    cv2.destroyAllWindows()
    return image_name

def UploadingImage(image_name):
    access_token = 'rf3dY05Dd4QAAAAAAAAAAQt3rRbE3__H-Wg_425XMfIlXFZ4Im4-FjCMY2BFhvkV'
    file=image_name
    file_from = file
    file_to = '/SecuritySystem/'+file  # The full path to upload the file to, including the file name

    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("uploaded")


#UploadingImage()

main()  

        
