import cattura_immagine
import elabora_immagine
import invio_web_server as invio
import data_ora as d
import dati_db


#Cattura immagine tramite scatto con la PiCamera
cattura_immagine.get_img()

#Elaora l'immagine con un algoritmo OpenCV
elabora_immagine.trova_mosche()

#Invia il risultato della foto sul server
url_foto = 'Risultati/result_%s.png' %d.data_ora_attuale()
invio.invio_foto(url_foto)

#Preleva dati dal db per comporre l'immagine
dati_db.preleva_lista()
dati_db.svuota_lista()