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
 <img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Screen/screen_putty_accesso.png"/><br>
 
   * Inserite l'IP del Raspberry e premete invio
   * Vi chiederà di inserire le credenziali:
     * Username:ip
     * Password:raspberry
   * Siete dentro Raspberry!   
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Screen/screen_putty_raspberry.png"/><br>

    * Adesso potete passare alla configurazione
  
 * Metodo 3(Metodo [VNC](https://it.wikipedia.org/wiki/Virtual_Network_Computing)):
   * Scaricate [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)
   * Collegate Raspberry al router tramite cavo ethernet(siete obblogati alla prima partenza)
   * Accedete al router o tramite ip scanner trovate l'IP di Raspberry
   * Una volta trovato l'indirizzo IP di Raspberry, aprite VNC Viewer
   <img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Screen/screen_vnc.png"/><br>
     * Inserite l'IP di Raspberry
     * Vi chiederà Username e Password:
       * Username:pi
       * Password:raspberry<br>
       <img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Screen/screen_vnc_accesso.png"/><br>
     * Siete dentro Raspberry
     * Potete passare alla configurazione
     <img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Screen/screen_raspberry_home.png"/><br>
  
Per il porogetto si è utilizzato sia il Metodo 2 che il Metodo 3.
Il Metrodo 2 lo abbiamo utilizzato per accedere a Raspberry e acceder alla configurazione per accedere alla rete Wi-Fi.
Fatto l'accesso siamo passati al Metodo 3.<br>

## 3. Configurazione Ambiente Raspberry
Appena effettuate l'accesso a Raspberry, accedete alla configurazione attraverso il comando: 'raspi-config'<br>
* Accedete al terminale
* Digitate 'sudo raspi-config'
* Si aprirà la configurazione di Raspberry<br>
<img src="https://github.com/FliesFree/FliesFree/blob/master/Foto/Screen/screen_raspberry_config.png"/><br>
* Accedete a NetworkOptions
* Inserite l'SSID della rete al quale volete connettervi e la password
* Abilitate la camera per poterla utilizzare in un secondo momento
* Se non effettua il reboot fatelo voi con il comando 'sudo reboot'
* La vostra Raspberry si collegherà sempre a quella rete Wi-Fi, quindi potete disconnettere il cavo LAN da router
