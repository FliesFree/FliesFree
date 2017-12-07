# Inizializzazione Raspberry Pi 3

## 1. Installazione Raspian
 * Per installare raspian, scarichiamo l'ultima versione dal sito ufficiale Raspberry: [Link Ufficiale](https://www.raspberrypi.org/downloads/)
 * Estraiamo i file dal file compresso
 * Prendiamo una Scheda SD da 8GB minimo(perchè diventerà la memoria del Raspberry e ci andremo a salvare tutte le foto per l'image processing)
 * Formattiamo la scheda SD con [SD Card Formatter](https://www.sdcard.org/downloads/formatter_4/)
 * Installiamo il file ISO estratto dall'archivio scaricato precedentemente
 * Utilizziamo, per installare l'ISO, [Win 32 Diskimager](https://sourceforge.net/projects/win32diskimager/)
 * Una volta installato l'ISO siamo pronti per inserire la scheda nel nostro Rasp e farlo partire
 
## 2. Prima partenza Raspberry
Per far partire la prima volta Raspberry, ci sono vari modi, vi elenco quelli più utilizzati e soprattuto quello che si è utilizzato per questo progetto.
<br>
 * Metodo 1(Metodo Diretto):
   * Collegare schermo attraverso l'apposito connettore e mouse e tastiera attraverso gli ingressi USB
   * Una volta collegati alimentate Raspberry e la partenza sarà automatica
   * Raspberry ha un Username e una Password di default: 
     * Username: pi
     * Password: raspberry
   * Siete pronti per operare!
  
 * Metodo 2(Metodo [SSH](https://it.wikipedia.org/wiki/Secure_Shell)):
   * Installate [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) sul vostro PC, sia se avete una macchin a linux sia windows
   * Una volta installato collegate Raspberry al vostro router di casa tramite il cavo ethernet(come primo accesso si è obbligati! Poi si può collegare Raspberry alla rete Wi-Fi)
   * Collegate anche il vostro PC alla rete domestica e accedete, tramite browser, al router(es: 192.168.0.1) e vedete tutti i dispositivi connessi, dovreste trovare anche Raspberry
   * Se non sapete come accedere al router o vedere gli indirizzi IP dei dispositivi connessi, si può utilizzare un programma chiamato [IP Scanner](https://www.advanced-ip-scanner.com/it/)
   * Dovrete inserire un rang di indirizzi IP per cercare tutti gli IP dei dispositivi connessi(es: 192.168.0.1 - 192.168.0.255)
   * Se non sapete quali range di IP inserire andate sul terminale e digitate ipconfig, troverete il Gatewey di rete che sarà il vostro indirizzo di partenza
   * Una volta trovato l'indirizzo IP di Raspberry possiamo accedervi attraverso Putty
  
