#Funzioni per elaorazioni immagini.
#Pietro Rignanese 2017
#--------------------------------FliesFree-----------------------------

import cv2 as cv
import data_ora
import numpy as np
from matplotlib import pyplot as plt

  #Funzione per visualizzare lo scatto su schermo
def visual_scatto():
    print("Visualizzazione scatto")
    img = cv.imread('/home/pi/FliesFree/Prove/Prove_Python/Flies_Free_Prova1/Trappola/%s.jpg' %data_ora.data_ora_attuale())
    cv.imshow('Scatto', img)
    cv.waitKey(0)
  
  #Funzione per cercare mosche nella foto scattata
def trova_mosche():
    print("Ricerca mosche in corso...")
    img_rgb = cv.imread('/home/pi/FliesFree/Prove/Prove_Python/Flies_Free_Prova1/Trappola/%s.jpg' %data_ora.data_ora_attuale())
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template1 = cv.imread('/home/pi/FliesFree/Prove/Prove_Python/Flies_Free_Prova1/Mosche/mosca1.jpg',0)
    template2 = cv.imread('/home/pi/FliesFree/Prove/Prove_Python/Flies_Free_Prova1/Mosche/mosca2.jpg',0)
    w, h = template1.shape[::-1]
    w2, h2 = template2.shape[::-1]
    #----------Il confronto avviene su due immagini campioni----------
    res1 = cv.matchTemplate(img_gray,template1,cv.TM_CCOEFF_NORMED)
    res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res1 >= threshold)#Matrice di immagine
    loc2 = np.where( res2 >= threshold)#Matrice di immagine
    
    num_mosche = 0 #numero delle mosche trovate
    num_cicli = 0 #numero di cicli
    conf = 0 #Variabile di confronto per poter contare i numero di rettangoli
    
    #Vengono evidenziate le zone dove sono state riscontrate delle mosche
    for pt in zip(*loc[::-1]):
   #------Algortitmo conteggio mosche-------     
        if num_cicli == 0:
            conf = pt[0]
            num_cicli = num_cicli + 1
            num_mosche = num_mosche + 1
        else:
            num_cicli = num_cicli + 1
            if (conf-30)<pt[0] and (conf+30)>pt[0]:
                conf = pt[0]
            else:
                num_mosche = num_mosche + 1
                conf = pt[0]
                
   #-----------------------------------------
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
        
    num_cicli = 0 #Riposto a zero i numero di cicli per ricominciare la conta
    
    for pt2 in zip(*loc2[::-1]):
    #------Algortitmo conteggio mosche-------     
        if num_cicli == 0:
            conf = pt2[0]
            num_cicli = num_cicli + 1
            num_mosche = num_mosche + 1
        else:
            num_cicli = num_cicli + 1
            if (conf-30)<pt2[0] and (conf+30)>pt2[0]:
                conf = pt2[0]
            else:
                num_mosche = num_mosche + 1
                conf = pt2[0]
                
   #-----------------------------------------
        cv.rectangle(img_rgb, pt2, (pt2[0] + w2, pt2[1] + h2), (0,0,255), 1)
        
    #Viene salvata l'immagine con le relative mosche evidenziate    
    cv.imwrite('Risultati/result_%s.png'%data_ora.data_ora_attuale(),img_rgb)
    print("Ricerca mosche coompletata...")
    print("Mosche trovate:")
    print(num_mosche)
    num_mosche = 0 #Riposrto a zero il numero delle mosche per una conta futura
