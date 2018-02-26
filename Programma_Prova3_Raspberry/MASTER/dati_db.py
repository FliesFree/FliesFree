import MySQLdb
import base64
import data_ora
import time

def preleva_lista():	
	controllo = 0
	cod = 0
	ident = 0
	contr = 0
	for n in range(0,40):
		db = MySQLdb.connect(host="localhost",user="root",passwd="root",db="Logs")
		cur = db.cursor()
		cur.execute("SELECT id,onoff,codice FROM `11` WHERE onoff=1")
		for row in cur.fetchall():
			cod = row[2]
			controllo = row[1]
			ident = row[0]
		print(cod)
		print(controllo)
		print(ident)
		if cod > 0 and controllo == 1 and contr == 0:
			sql = "SELECT * FROM `11` WHERE id>1 and codice="
 			cod = repr(cod)
			sql = sql + cod	
			ident = repr(ident)
			ident = ident.replace("L","")
			sql2 = " and id<"+ident
			sql = sql + sql2
			print(sql)
			cur.execute(sql)
			#cur.execute("DELETE FROM Logs.`11` WHERE `id`>1")
			image_64 = ""

			for row in cur.fetchall():
				if row[5]<>"0":
					image_64 = image_64 + row[5]
			image_64 = image_64.replace("_","/")
			image_64 = image_64.replace(".","=")
			print(image_64)
			base_64_decode = base64.decodestring(image_64)
			immagine = open("Risultati/result_slave_%s.png"%data_ora.data_ora_attuale(),"wb")
			immagine.write(base_64_decode)
			immagine.close()
			#cur.execute("DELETE FROM `11` WHERE id>1")
			contr = 1
			print("Immagine elaborata!")
		
		db.close()
		time.sleep(10)
		
	
	
def svuota_lista():
	db = MySQLdb.connect(host="localhost",user="root",passwd="root",db="Logs")

	cur = db.cursor()	
	sql = "DELETE FROM Logs.`11` WHERE `id`>1"
	try:
		cur.execute(sql)
		db.commit()
	except:
		db.rollback()

	db.close()
