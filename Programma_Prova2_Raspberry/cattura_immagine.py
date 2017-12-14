#Cattura Immagine
#Pietro Rignanese 2017
#----------------------FliesFree---------------------------

from picamera import PiCamera 
import time
import data_ora 

def get_img():
    print("Sto scattando una foto...")
    camera = PiCamera()
    camera.start_preview()
    camera.annotate_text = data_ora.data_ora_attuale()
    time.sleep(5)
    camera.capture('/home/pi/FliesFree/Prove/Prove_Python/Flies_Free_Prova1/Trappola/%s.jpg' % data_ora.data_ora_attuale())
    camera.stop_preview()
    print("Foto scattata.")
