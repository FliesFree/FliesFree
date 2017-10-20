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
* <a href="#ancora-esempiodilavoro">Esempio di lavoro</a>
 
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

## <a name="ancora-esempiodilavoro"></a> Esempio di lavoro
Come si è detto all'inizio, il progetto consiste nell'evitare l'attacco della mosca in un uliveto, in modo da agire nel momento giusto all'eliminazione.
Questo fa si che si produca un olio di maggiore qualità.

*Ma come inseriamo il nostro prototipo in un uliveto?*
Per prima cosa, non avendo a disposizione prese di corrente o altro, si è pensato ad autoalimentare l'intero sistema con una pila e un pannelletto solare per ogni nodo.
Per inserire il prototipo nell'uliveto ci occorre una piantina o planimetria dell'area da proteggere e inserire tanti nodi in base alla grandezza.
Più grande è il terreno e di più nodi abbiamo bisogno, ma solamente uno e uno solo sarà il nodo master.
Sapendo il range, entro il quale agisce la comunicazione di ogni nodo, possiamo dividere l'uliveto in zone e piazzare i nodi in ogni zona.
Se dovessero esserci problemi di comunicazione, ad esempio: una zona è troppo lontana per comunicare con il nodo master, si utilizza un ripetitore di segnale, in modo da aumetare il range di comunicazione di ogni nodo.
La comunicazione fra i vari nodi avviene in modo diretto:<br>
*Nodo Master -> Nodo Slave*<br>
*Nodo Slave -> Nodo Master*<br>
Non abbiamo una comunicazione P2P, ma una semplice comunicazione diretta.<br>
