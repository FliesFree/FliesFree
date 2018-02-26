import cattura_immagine
import elabora_immagine
import invio_web_server as invio
import data_ora as d
import invio as dongle
import frammenta_immagine

#Cattura immagine tramite scatto con la PiCamera
cattura_immagine.get_img()

#Elaora l'immagine con un algoritmo OpenCV
elabora_immagine.trova_mosche()

#Invia il risultato della foto alla master
frammenta_immagine.frammenta()


print("Spegnimento...")
