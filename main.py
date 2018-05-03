import time
import cv2
import recognize_picture

    
def main():
    file_name = str(time.asctime( time.localtime(time.time()) ))+'.jpg'
    get_image(file_name)
    result = recognize_picture.recognize_picture(file_name)
    if check_result(result):
        convert_class_to_siginal(result)
    else:
        tell_cannot_classify()
        audio_result = record_send_audio_and_return_result()
        convert_class_to_siginal(result,image=False)