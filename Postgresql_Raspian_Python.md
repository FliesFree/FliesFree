# Installazione e configuarazione Postgresql su Raspberry

## Installazione Postgresql
  * Aprire il terminale
  * Aggiornare il firmware '*sudo apt-get update*'
  * Digitare '*sudo apt-get install postgresql postgresql-contrib*'
  * Installiamo le librerie che useremo con il Python: '*sudo apt-get install python-psycopg2*'
  * Digitare '*sudo apt install postgresql libpq-dev postgresql-client postgresql-client-common -y*'
  * Installiamo l'IDE di Postgresql sul Raspberry: '*sudo apt-get install pgadmin3*'

Dovremmo avere tutto per operare con Postgresql sul nostro Raspberry.

## Configurazione Postgresql da terminale
 * '*sudo su postgres*'
 * Creiamo un "User" per il database: '*createuser "nome" -P --interactive*'
 * Impostiamo password e tutte le credenziali che ci chiede
 * Digitate 'exit'
 * Digitate '*psql "nome"*'
 * Si aprirà la modalità DB sul terminale
 * Creiamo una tabella da aggiungere al DB: '*create table nome_tb (name text, surname text,...);*'
 * Mi raccomando al ;(punto e virgola a fine istruzione!!!)
 * Inseriamo qualcosa nella tabella con: '*insert into nome_tb ('valore1','valore2');*'
 * Visualizziamo sul terminale la tabella: '*select * from nome_tb;*' 
 
 
## Configurazione Postgresql da pgAdmin3
 * Creiamo un nuovo collegamento al server e inseriemo i seguenti campi:
   * Name: "nome_db"
   * Port: 5432
   * Username: "nome_user_creato"
 * Cliccate Ok e procediamo!
 
Adesso vedrete su schermo il server creato e il database al suo interno.
All'interno del DB ci sono le tabelle e quello inserito al suo interno.


## Comunicazione con Postgresql da Python

Ecco un piccolo script di codice che si può eseguire da Python:

*import psycopg2*

*conn = psycopg2.connect('dbname=test')*<br>
*cur = conn.cursor()*

*cur.execute('select * from people')*

*results = cur.fetchall()*

*for result in results:*<br>
    *print(result)*
    
    
<br>
Trovate altir esempi di comunicazione a questo [sito](https://pythonspot.com/python-database-postgresql/)

