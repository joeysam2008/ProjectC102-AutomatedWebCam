# Importing the modules.
import cv2 
import dropbox
import time
import random

# creating variable and taking current system time
start_time = time.time()

def take_Snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # ret will return a boolean value
        ret,frame = videoCaptureObject.read()
        # naming the captured image
        img_name = 'img'+str(number)+'.png'
        # saving img name & picture. 
        # cv2.imWrite() is method to save images to any storage device
        cv2.imWrite(img_name, frame)
        start_time = time.time
        result = False

    return img_name
    print('Your snapshot has been taken.')
    # DIsabling the camera
    videoCaptureObject.release()
    # To close all windows
    cv2.destroyAllWindows()

def Upload_Files(img_name):
    access_token = 'sl.BAgvfgczuhGIjBpJ2ujxFr2DYXRk59qFiTA_NUlzoOlDWrltK5J7SljK_jVsu0mVgX2HKoY5USPX4hGQu0CXQGwfxtdH3phdpl8F5SwpNCBf2l09i4fXct6vkfm4E66BVo4KrwYV__Qw'
    file = img_counter
    file_from = file
    file_to = '/ProjectC102/'+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload( f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print('Your file has been uploaded to Dropbox')

def main():
    while(True):
        if((time.time()-start_time)>=120):
            # calling take_snapshot() function
            name = take_Snapshot
            # calling Upload_Files() function
            Upload_Files(name)

main()