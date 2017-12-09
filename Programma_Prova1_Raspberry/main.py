import cattura_immagine
import elabora_immagine


#Cattura immagine tramite scatto con la PiCamera
cattura_immagine.get_img()

#Elaora l'immagine con un algoritmo OpenCV
elabora_immagine.trova_mosche()