<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Logo/flies_free_logo.png"/>

Questo progetto vede la realizzazione di un prototipo(tutto automatizzato) per prevenerire tempestivamente l'attacco delle mosche in un uliveto.

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

### <a name="ancora-comunicazione_nodi"></a> 5. Comunicazione Nodi

