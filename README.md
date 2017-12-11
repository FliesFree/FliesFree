<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/flies_free_logo.png"/>

Questo progetto vede la realizzazione di un prototipo(tutto automatizzato) per prevenerire tempestivamente l'attacco delle mosche in un uliveto.<br><br>
Nel [link seguente](http://www.pithecusa.com/hobby/ortofrutteo/Nemici/le_tre_mosche.htm) troverete una piccola spiegazione sui tre tipi di mosche più diffuse nel nostro territorio e tra queste la mosca dell'olivo.
<br>
Il progetto verrà diviso in due parti:
* Realizzazione hardware e software del prototipo
* Realizzazione della parte di front-end e back-end del software per la gestione dei dati e comunicazione con l'utente

<br>

D'ora in poi chiameremo il nostro prototipo, per semplicità FFS(FliesFreeShield).

__________________________________________________________________

# <a name="ancora-indice"></a> Indice
* <a href="#ancora-componenti">Componentistica</a>
* <a href="#ancora-struttura">Struttura</a>
  * <a href="#ancora-nodomaster">Struttura Nodo Master</a>
  * <a href="#ancora-nodoslave">Struttura Nodo Slave</a>
  * <a href="#ancora-alimentazione">Alimentazione Nodi</a>
  * <a href="#ancora-comunicazione_nodi">Comunicazione Nodi</a>
* <a href="#ancora-esempio_lavoro">Esempio</a>
* <a href="#ancora-moddilavoro">Modalità di lavoro</a>
  * <a href="#ancora-fase1">Fase 1 - Divisione della mappa</a>
  * <a href="#ancora-fase2">Fase 2 - Inserimento di ripetitori di segnale</a>
  * <a href="#ancora-fase3">Fase 3 - Alloggio trappole per zona</a>
  * <a href="#ancora-fase4">Fase 4 - Alloggio FFS</a>
  * <a href="#ancora-fase5">Fase 5 - Elaborazione immagini</a>
  * <a href="#ancora-fase6">Fase 6 - Acquisizione dati</a>
  * <a href="#ancora-fase7">Fase 7 - Comunicazione con l'utente</a>
* <a href="#ancora-progettazione">Progettazione</a>
  * <a href="#ancora-prog_1">Progettazione Raspberry-Image Processing-Acquisizioni Dati-Porting</a>
    * <a href="#ancora-prova1">Prova1:Acquisizione foto e Image Processing</a>
    * <a href="#ancora-prova2">Prova2:Invio dati sul DB</a>
  * <a href="#ancora-prog_2">Progettazione Web-Database-Sicurezza</a>
 
__________________________________________________________________________________

## <a name="ancora-componenti"/></a> Componentistica
 * [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/);
 * [Camera Raspberry](https://www.raspberrypi.org/products/camera-module-v2/);
 * [Apio DONGLE](https://www.apio.cc/component/virtuemart/store_ita/prodotti/apio-dongle-1-4-detail?Itemid=0);
 * Saponetta Wi-Fi;
 * [Modulo TP4056](http://www.hotmcu.com/tp4056-micro-usb-5v-1a-lithium-battery-charger-with-protection-p-176.html);
 * Pile al litio;
 * Alzatore di tensione da 3.3v a 5v;
 * Pannello solare.
 
*N.B: Per tutte le componenti, ad esclusione della saponetta Wi-Fi, bisogna prenderne di un numero uguale a quello dei nodi.
Esempio: 3 Nodi -> 3 Raspberry, 3 Camera, 3 Apio DONGLE, 3 Moduli TP4056, 3 pile e 3 pannelli.*
 
____________________________________________________________________________________

## <a name="ancora-struttura"></a> Struttura
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Struttura/struttura_generale.jpg"/>
Come possiamo vedere da questa struttura generale, i nodi della rete comunicano attraverso una rete senza fili, inviando dati in entrambe le direzioni.
Adesso vediamo nel dettaglio come sono strutturati i vari nodi, le comunicazioni e le loro alimentazioni.

### <a name="ancora-nodomaster"></a> 1. Struttura Nodo Master
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Struttura/schema_nodo_master.png"/>
Come possiamo vedere dallo schema, il nodo master è formato da:

 * Raspberry Pi 3 
 * Camera per Raspberry
 * Apio DONGLE
 * Saponetta 3G/4G

La Raspberry è il cuore pulsante del nodo: cattura le immagini attraverso la telecamera, le elabora e le manda sul Cloud attraverso la saponetta Wi-Fi.
La APIO DONGLE serve per comunicare con gli altri nodi in entrambe le direzioni.

### <a name="ancora-nodoslave"></a>  2. Struttura Nodo Slave
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Struttura/schema_nodo_slave.png"/>

Per il nodo master le cose sono più semplici:

 * Raspberry Pi 3
 * Camera
 * Apio DONGLE
 
In questo caso, a differenza del nodo master, non abbiamo la saponetta Wi-Fi, perchè, una volta elaborata l'immagine, i dati vengono inoltrati al nodo master che provvederà a piazzarli sul Cloud.

### <a name="ancora-alimentazione"></a> 3. Alimentazione Nodi
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Struttura/alimentazione.png"/>

 * Pannello solare
 * Cavetti
 * Modulo TP4056
 * Pila al litio
 * Alzatore di tensione
 
In questo caso è la pila al litio che fornisce energia al sistema e il pannello solare fornisce energia alla batteria.
Grazie all'ausilio del modulo TP4056 è possibile ricaricare la pila tramite il pannello solare.
Un alzatore di tensione collaga il circuito di alimentazione alla Raspberry fornedoli esattamente 5v(tensione di lavoro della scheda).

<br>
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Struttura/asd.jpg"/>
Come possiamo vedere dall'immagine, il pannello solare ricarica la pila al litio, la pila al litio alimenta il nodo attraverso un'alzatore di tensione(voltage booster): portando la tensione da 3.7V a 5V.<br>
Questo fa si che ogni nodo abbiamo una propria alimentazione e che sia autonomo.<br>
Bisogna stare attenti sui voltaggi e gli amperaggi forniti dal pannello solare e dalla pila.
Una Raspberry Pi 3 assorbe, in norma, 800mAh, quindi preleverà dalla pila al litio 800mA ogni ora.
Una pila, in media(considerando quelle degli smartphone), ha una durata di 1-2 giorni, considerando questi tipi di consumi.
Il pannello solare deve fornire una giusta dose di energia per far si che la pila non si scarichi mai del tutto e possa sempre alimentare, in modo costante, il nodo.
Può capitare che in un giorno non ci sia sole a sufficienza da produrre la giusta dose di energia per la pila, ma questo non fermerà il nodo perchè ha una propria autonomia grazie alla pila che regge almeno 1-2 giorni.
Il problema si viene a creare quando i giorni di assenza di sole sono molti di più... ma vedremo di risolvere tale problema con una pila più grande.
Parleremo di questa problematica più in la...

### <a name="ancora-comunicazione_nodi"></a> 5. Comunicazione Nodi
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Struttura/comunicazione.png"/>
In questo schema possiamo vedere come avviene la comunicazione fra i vari nodi.
Le Apio DONGLE comunicano in entrambi i sensi e permettono ai nodi di passarsi le informazioni e dati.
Tutti i dati convoglieranno sul nodo master che provvederà a mettersi sul Cloud.
Ogni nodo della rete elabora le immagini direttamente sul posto... al nodo master verranno passate solamente le informazioni inerenti a tali immagini.

_____________________________________________________________________________

## <a name="ancora-esempio_lavoro"></a> Esempio
 * Hardware:
   * Ogni nodo avrà a disposizione una trappola a feromone e la fotocamera di raspberry punterà su quest'ultima<br>
   * La raspberry per la maggiorparte del tempo sarà in "sleep" e si sveglierà solamente per scattare una foto alla trappola ed elaborare l'immagine<br>
   * Una volta elaborata l'immagine, con degli algoritmi specifici, verranno mandati i dati relativi a quest'ultima sul cloud(nel caso del nodo master) oppure al nodo master(nel caso di nodo slave)<br>
   * La raspberry tornerà in fase di "sleep"<br>
   
 * Software:
   * Il cloud riceve i dati inviati dal master e gli andrà ad archiviare in un database
   * Tramite un algoritmo verranno verificati i dati mandati dal nodo master:
     * Se l'algoritmo prevede un problema su un nodo manda un segnale(SMS e/o notifica app) con il relativo problema
     * Se l'algoritmo non prevede nessun problema non viene mandato nessun riscontro
   * Tramite un'app è possibile monitorare quello che sta accadendo nell'uliveto
_____________________________________________________________________________

## <a name="ancora-moddilavoro"></a> Modalità di lavoro
Come si è detto all'inizio, il progetto consiste nell'evitare l'attacco della mosca in un uliveto, in modo da agire nel momento giusto all'eliminazione.
Questo fa si che si produca un olio di maggiore qualità.<br>

*Ma come inseriamo il nostro prototipo in un uliveto?*<br>
Per prima cosa, non avendo a disposizione prese di corrente o altro, si è pensato ad autoalimentare l'intero sistema con una pila e un pannelletto solare per ogni nodo.
Per inserire il prototipo nell'uliveto ci occorre una piantina o planimetria dell'area da proteggere e inserire tanti nodi in base alla grandezza.
Più grande è il terreno e di più nodi abbiamo bisogno, ma solamente uno e uno solo sarà il nodo master.
Sapendo il range, entro il quale agisce la comunicazione di ogni nodo, possiamo dividere l'uliveto in zone e piazzare i nodi in ogni zona.
Se dovessero esserci problemi di comunicazione, ad esempio: una zona è troppo lontana per comunicare con il nodo master, si utilizza un ripetitore di segnale, in modo da aumetare il range di comunicazione di ogni nodo.
La comunicazione fra i vari nodi avviene in modo diretto:<br>
*Nodo Master -> Nodo Slave*<br>
*Nodo Slave -> Nodo Master*<br>
Non abbiamo una comunicazione P2P, ma una semplice comunicazione diretta.<br>
Procediamo per gradi:
<br>
<br>

### <a name="ancora-fase1"></a> Fase 1 - Divisione della mappa
Per questa prima fase si deve dividere il terreno di lavoro in rettangoli o quadrati di dimensioni uguali.
Definiamo N zone che faranno parte della nostra rete e dove andremo ad inserire i nostri N nodi.
Prendiamo una mappa di un uliveto:
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Mappe/mappa_uliveto.png"/>
<br>
Adesso dividiamola in parti uguali:
<br>
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Mappe/mappa_uliveto_divisa.png"/>
Le divisioni devono avvenire in base al range di comunicazione, se ad esempio i due nodi possono comunicare ad un massimo di 120 metri, si deve dividere la mappa in blocchi di dimensione 100x100.
Si può prevedere di dividere in blocchi più grandi inserendo tra ogni blocco un ripetitore di segnale, in modo da estendere il range di comunicazione.

### <a name="ancora-fase2"></a> Fase 2 - Inserimento di ripetitori
Si è obbligati ad inserire qualche ripetitore perchè la comunicazione deve essere diretta e quindi un nodo slave, per quanto lontano possa essere, deve comunicare direttamente con il master.
Inseriamo i ripetitori in punti in cui si possa ripetere al meglio il segnale di un nodo.

### <a name="ancora-fase3"></a> Fase 3 - Inserimento trappole
Bisogna inserire una trappola a feromone per mosche in ogni punto in cui andremo a piazzare un nodo.
Questa trappola creerà una comunicazione su quello che sta accadendo:
le trappole cattureranno una certa quantità di mosche, le fotocamere delle raspberry puntano su tali trappole e scatteranno delle foto che verranno successivamente elaborate per garantire un'azione tempestiva da parte dell'agricoltore(qual'ora ci fosse bisogno).
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Mappe/mappa_uliveto_divisa_contrappole.png"/>

### <a name="ancora-fase4"></a> Fase 4 - Alloggio FFS
Una volta disposta la trappola, possiamo disporre il nostro prototipo FFS di fronte la trappola, per monitorare quello che succederà in ogni zona.

### <a name="ancora-fase5"></a> Fase 5 - Elaborazione Immagini
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Componenti/raspberry_con_camera.jpg"/>
La fotocamera posta su Raspberry catturerà le immagini nell'arco della giornata e le elaborerà attraverso la librearia OpenCV.
<a href="https://opencv.org/"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/opencv_logo.png"/></a>

### <a name="ancora-fase6"></a> Fase 6 - Acquisizione dati
Una volta acquisiti i dati, inerenti all'elaborazione dell'immagini, questi verranno inviati sul cloud attraverso un collegamento Wi-Fi con una saponetta 3G/4G.
Prima di questo, se l'immagine elaborata è presente su un nodo slave, i dati verranno mandati sul nodo master, sarà quest'ultimo ad inoltrarli sul cloud.
Le comunicazioni fra i nodi slave e master avviene in modalità wirless con le Apio DONGLE.

### <a name="ancora-fase7"></a> Fase 7 - Comunicazione con l'utente
I dati mandati sul cloud saranno presentati all'utente attraverso una Web App e/o un'App per smartphone

__________________________________________________________________________

## <a name="ancora-progettazione"></a> Progettazione
In questa fase descriveremo passo passo tutte le fasi di progettazione sia hardware che software.<br>

_____________________________________________________________________________
### <a name="ancora-prog_1"></a> *1) Progettazione Raspberry-Image Processing-Acquisizioni Dati-Porting*
#### *A cura di Pietro Rignanese*
Prima di passare alla progettazione, ricordiamo le fasi per inizailizzare Raspberry. Trovate tutto su questo [Link](https://github.com/FliesFree/FliesFree/blob/master/Inizializzazione_Raspberry_Pi_3.md)
<br>
Una volta inizializzato Raspberry e collegato alla rete, si può partire a progettare...<br>
Dividiamo questa fase di progettazione in *Prove*, dove andremo a descrivere passo passo come realizzzare un prototipo in grado di scattare foto, elaborare l'immagine e inviarle sul server.
Tutte queste fasi verranno parcellizzate, in modo da facilitare la realizzazione del prototipo.
<br>
##### <a name="ancora-prova1"></a> *Prova 1: Acquisizione immagine e image processing*
Partiamo con la prima prova, in cui effettuaiamo una foto e un'elaborazione dell'immagine, in modo da trovare in essa una o più figure cercate(nel nostro cado mosche, ma per il test ci limitiamo a delle forme disegnate a penna su un semplice cartoncino).<br>
<br>
*Acquisizione Immagine:*<br>
Per poter acquisire un'immagine si deve verificare prima il funzionamento della PiCamera connessa a Raspberry.
Seguiamo questi semplici passi:
* Collegare la PiCamera nell'apposito slot facendo attenzione di collegarlo nel modo giusto e nel giusto verso
* Se avete seguito la guida prima di partire con la progettazione, allora avete abilitato anche la camera, altrimenti dovete abilitarla digitando da riga di comando 'sudo raspi-config' e andare nella sezione 'camera'
* Testiamo il funzionamento della PiCamera digitando 'sudo raspistill -v -o acquisizione.jpg'
* Se tutto è a posto la Raspberry scatterà una foto e vi mostrerà una preview della foto
* Se si verificano dei problemi tipo "No data received from sensor. Check all connections, including the Sunny one on the camera board" potrebbe dipendere da diversi fattori:
  * Sottoalimentazione della scheda
  * Slot di collegamento PiCamera non chiuso<br>
 Soluzione:
  * La sottoalimentazione si risolve collegando Raspberry con l'alimentatore di almeno 2A
  * Lo slot dove avete collegato la PiCamera dovete farlo scattare una volta inserita la camera<br>
  
Una volta fatto tutto e testata la camera, possiamo passare a programmare in Python.<br>
Nella reposity è presente una cartella 'Programma_Prova1_Raspberry' dove all'interno sono presenti i codici da eseguire in python per scattare foto ed elaborare immagini... ma andiamo per gradi...<br>
Scaricate la reposity di GitHub e copiate all'interno della vostra Raspberry la cartella enunciata poco fa, anche sulla home va bene, l'importante è eseguire lo script di codice "main.py".
Come potete vedere nella cartella sono presenti diversi file, ognuno di questi ha al suo interno una o più funzioni che vengono richiamate dal main.
Il file "cattura_immagine.py" ha al suo intreno una fnzione che acquisisce una foto attraverso la camera.
<br>
"data_ora.py" ha diverse funzione che gestiscono la data e l'ora attuale: queste funzioni saranno dispensabili per poter salvare le foto scattate e archiviarle per data e ora.<br>
"elabora_immagine.py" è il file che contiene al suo interno due funzioni: la prima visualizza l'immagine  aschermo e la seconda è quella riservata all'image processing e sarà quella che spiegheremo nel maggior dettaglio.<br>
"main.py" è una file che richiama gli altri file e le loro funzioni, in modo da avere un codice più pulito e più facile da modificare in futuro.<br>

*Image Processing:*<br>
Per poter effettuare l'image processing di un'immagine si utilizzano le librerie di OpenCV.<br>
Per poterle utilizzare dovete installarle sul vostro Raspberry da riga di comando: 'sudo apt-get install python-picamera python3-picamera python-rpi.gpio' e 'sudo apt-get install python-opencv'.<br>
<br>
*In che modo avviene il ritrovamento di una forma o figura all'interno di una foto scattata?*<br>
Avviene in 3 Fasi:
  * *Fase di Detection*:si individuano i punti in cui sono presenti dei tratti caratteristici dell'immagine da trovare
  * *Fase di Extraction*:estraggo dei vettori n-dimensionali che descrivano ogni punto trovato
  * *Fase di Matching*:si confrontano gli spazi di n-dimensioni trovati tra l'immagine scattata ed una campione, in modo da vedere la corrispondenza.
  <br>
Queste 3 fasi sono consecutive e fanno si che dall'immagine scattata si possa evidenziare una forma o un oggetto da trovare.
Nel nostro caso, vogliamo trovare un particolare tipo di mosca e quindi li diamo come immagine campione(che verranno confrontate con l'immagine scattata) la mosca da trocare in tutte le possibili posizioni e angolazioni... l'algoritmo prevederà al resto...<br>
Questa tecnica è chiamata *Machine Learning*, ovvero alleno l'algoritmo a riconoscere un'oggetto dandogli un'oggetto di riferimento.
Più oggetti di riferimento li diamo, più preciso sarà il ritrovamento.<br>
Nel nostro caso, abbiamo testato l'algoritmo cercando su un cartoncino una serie di cerchi e ovali colorati...
L'algoritmo funziona! Perchè scarta le forme più grandi e quelle non piene.<br>
A questo [Link](https://docs.opencv.org/master/d2/d96/tutorial_py_table_of_contents_imgproc.html) di OpenCV sono presenti tutti i tipi di algoritmo di ricerca, saturazione, esposizione e altro... in base al tipo di lavoro da fare sull'immagine, verrà scelto un algoritmo al posto di un altro.<br>
Nel nostro caso abbiamo 2 cartelle che vengono usate per elaborare l'algoritmo:
  * Directory 'Mosche': Contiene le immagini di mosche che verranno usate come campione per il confronto
  * Directory 'Trappole': Contiene le immagine delle trappole scatate volta per volta e catalogate per data e ora
 <br>
 


##### <a name="ancora-prova2"></a> *Prova 2: Invio dati dul DB*



________________________________________________________________________________________________________________________

### <a name="ancora-prog_2"></a> *2) Progettazione Web-Database-Sicurezza*
#### *A cura di Andrea Polenta*
__________________________________________________________________________

## <a name="ancora-indice"></a> Torna all'indice

<a href="https://www.raspberrypi.org/"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/logo_rasp.png"/></a> <a href="https://www.apio.cc/"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/Apio_Logo.png"/></a> <a href="https://github.com/FliesFree"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/flies_free_logo(2).png"/></a> <a href="https://opencv.org/"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/opencv_logo.png"/></a><a href="www.angular.io"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/angular_logo.png"/></a><a href="https://nodejs.org/it/"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/node_logo.png"/></a><a href="https://www.realvnc.com/en/connect/download/viewer/"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/vcn_logo.png"/></a><a href="https://auth0.com/press"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/auth0_logo.png"/></a><a href=""><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/npm_logo.png"/></a><a href=""><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/php_logo.png"/></a><a href=""><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/postgis_logo.png"/></a><a href=""><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/postgresql_logo.png"/></a><a href=""><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/python_logo.png"/></a><a href=""><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/slim_logo.png"/></a><a href=""><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/type_logo.png"/></a>
          
