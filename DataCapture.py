# To generate img data from video

import cv2
import os
import datetime

id = "Unnati"
video_path = "Data Collection - BE Project\\Unnati 1.mp4"

cap=cv2.VideoCapture(video_path)
# count the number of frames
def videoTime(data):
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = data.get(cv2.CAP_PROP_FPS)

    # calculate duration of the video
    seconds = round(frames / fps)
    video_time = datetime.timedelta(seconds=seconds)
    print(f"No. of frames: {frames}")
    print(f"duration in seconds: {seconds}")
    print(f"video time: {video_time}")

videoTime(cap)

face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def face_croped(img):
    cv2.imshow("Hello",img)
    # convert gray sacle
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    #Scaling factor 1.3
    # Minimum naber 5
    for (x,y,w,h) in faces:
        face_croped=img[y:y+h,x:x+w]
        return face_croped


img_id=750

while True:
    ret,my_frame=cap.read()

    # check if video requires rotation
    # my_frame = cv2.rotate(my_frame, cv2.ROTATE_180)

    if face_croped(my_frame) is not None:
        img_id+=1
        face=cv2.resize(face_croped(my_frame),(450,450))
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        parent= "Preprocessed Data"
        directory = str(id)
        path=os.path.join(parent,directory)
        os.makedirs(path,exist_ok=True)
        file_name_path=f"Preprocessed Data/{str(id)}/user.{str(id)}.{str(img_id)}.jpg"
        cv2.imwrite(file_name_path,face)
        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
        cv2.imshow("Capture Images",face)

    # To get 100 images
    # if cv2.waitKey(1)==13 or int(img_id)==100:
    #     break

    # To get images of full video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


