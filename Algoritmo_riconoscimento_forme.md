# Algoritmo riconoscimento forme con Raspberry

## Segmentazione
Partizionamento di un'immagine in zone omogenee sulla base di un certo criterio di appartenenza dei pixel ad una regione.<br>

Obiettivo: Riconoscere oggetti(mosche) su una trappola a fermoni per mosche.<br>

Tipi di segmentazione:
#### Edge Detection
#### Tresholding
#### Region Based

## Problematiche
A volte l'immagine può essere affetta da "rumore" ossia un qualcosa che sfuma i toni dell'immagine.
Per ridurre questi disturbi si utilizzano delle *tecniche di filtraggio*<br>
* Filtri passa-basso: attenuano le alte frequenze dell'immagine lasciando inalterate le basse
* Filtri passa-alto: esalta i contorni rendendoli più grossi e meglio individuabili.


## Libreria OpenCV
Algoritmi di elaborazione d'immagine sono tutte all'interno della libreria di OpenCV.
Abbiamo circa 500 funzioni da poter sfruttare per l'elaborazione dell'immagine e dei video.
