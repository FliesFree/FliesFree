<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/flies_free_logo.png"/>

Questo progetto vede la realizzazione di un prototipo(tutto automatizzato) per prevenerire tempestivamente l'attacco delle mosche in un uliveto.

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
  * <a href="#ancora-fase4">Fase 4 - Alimentazione</a>
  * <a href="#ancora-fase5">Fase 5 - Elaborazione immagini</a>
  * <a href="#ancora-fase6">Fase 6 - Acquisizione dati</a>
  * <a href="#ancora-fase7">Fase 7 - Transumanza dei dati sul Cloud</a>
* <a href="#ancora-progettazione">Progettazione</a>
 
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

### <a name="ancora-fase4"></a> Fase 4 - Alimentazione
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

### <a name="ancora-fase5"></a> Fase 5 - Elaborazione Immagini
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Componenti/raspberry_con_camera.jpg"/>
La fotocamera posta su Raspberry catturerà le immagini nell'arco della giornata e le elaborerà attraverso la librearia OpenCV.
<a href="https://opencv.org/"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/opencv_logo.png"/></a>

### <a name="ancora-fase6"></a> Fase 6 - Acquisizione dati
Una volta acquisiti i dati, inerenti all'elaborazione dell'immagini, questi verranno inviati sul cloud attraverso un collegamento Wi-Fi con una saponetta 3G/4G.
Prima di questo, se l'immagine elaborata è presente su un nodo slave, i dati verranno mandati sul nodo master, sarà quest'ultimo ad inoltrarli sul cloud.
Le comunicazioni fra i nodi slave e master avviene in modalità wirless con le Apio DONGLE.

### <a name="ancora-fase7"></a> Fase 7 - Transumanza dati sul cloud
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/cloud.png"/>
I dati verranno mandati al cloud dal nodo master attarverso una comunicazione senza fili.

__________________________________________________________________________

## <a name="ancora-progettazione"></a> Progettazione
In questa fase descriveremo passo passo tutte le fasi di progettazione sia hardware che software.
__________________________________________________________________________

## <a name="ancora-indice"></a> Torna all'indice

<a href="https://www.raspberrypi.org/"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/logo_rasp.png"/></a> <a href="https://www.apio.cc/"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/Apio_Logo.png"/></a> <a href="https://github.com/FliesFree"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/flies_free_logo(2).png"/></a> <a href="https://opencv.org/"><img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/opencv_logo.png"/></a>
          
