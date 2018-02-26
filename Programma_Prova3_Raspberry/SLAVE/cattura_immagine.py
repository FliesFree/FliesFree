#Cattura Immagine
#Pietro Rignanese 2017
#----------------------FliesFree---------------------------

import picamera  
import time
import data_ora 

def get_img():
    print("Sto scattando una foto...")
    camera = picamera.PiCamera()
    camera.start_preview()
    camera.annotate_text = data_ora.data_ora_attuale()
    time.sleep(5)
    camera.resolution=(500,600)
    camera.capture('/home/pi/FliesFree/Programma_Prova2_Raspberry/Trappola/%s.jpg' % data_ora.data_ora_attuale())
    camera.stop_preview()
    print("Foto scattata.")
