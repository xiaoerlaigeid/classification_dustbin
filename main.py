import time
import cv2
import recognize_picture
import os
import speech_recognition_baidu
import re 
def tell_cannot_classify():
    os.system("cannot_classify.wav")
def record_send_audio_and_return_result():
    file_name = 'audio.wav'
    os.system("arecord -d 10 -f cd -t wav -D copy foobar.wav")
    result = speech_recognition_baidu.speech_recognition_baidu(file_name)
    if result.find('其他') != -1:
        
    elif result.find('罐') != -1 or result.find('瓶罐') != -1 and result.find('桶') != -1:
        
    elif 
    
    else :
def get_image(file_name):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(file_name,frame)
    cap.release()
def convert_class_to_siginal(result):
    
def main():
    file_name = str(time.asctime( time.localtime(time.time()) ))+'.jpg'
    get_image(file_name)
    result = recognize_picture.recognize_picture(file_name)
    if result != 0 or result != 1 or result != 2:
        convert_class_to_siginal(result)
    else:
        tell_cannot_classify()
        audio_result = record_send_audio_and_return_result()
        convert_class_to_siginal(result,image=False)