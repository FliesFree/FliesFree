#Funzioni per elaorazioni immagini.
#Pietro Rignanese 2017
#--------------------------------FliesFree-----------------------------

import cv2 as cv
import data_ora
import numpy as np
from matplotlib import pyplot as plt

  #Funzione per visualizzare lo scatto su schermo
def visual_scatto():
    img = cv.imread('/home/pi/FliesFree/Prove/Prove_Python/Flies_Free_Prova1/Trappola/%s.jpg' %data_ora.data_ora_attuale())
    cv.imshow('Scatto', img)
    cv.waitKey(0)
  
  #Funzione per cercare mosche nella foto scattata
def trova_mosche():
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
    loc = np.where( res1 >= threshold)
    loc2 = np.where( res2 >= threshold)
    
    #Vengono evidenziate le zone dove sono state riscontrate delle mosche
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
    for pt2 in zip(*loc2[::-1]):
        cv.rectangle(img_rgb, pt2, (pt2[0] + w2, pt2[1] + h2), (0,0,255), 1)
        
    #Viene salvata l'immagine con le relative mosche evidenziate    
    cv.imwrite('Risultati/result_%s.png'%data_ora.data_ora_attuale(),img_rgb)
