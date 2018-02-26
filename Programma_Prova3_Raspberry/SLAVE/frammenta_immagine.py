import base64
import data_ora
import invio
import time

def frammenta():
	invio.invio_dongle("codice",1)
	image = 'Risultati/result_%s.jpg'%data_ora.data_ora_attuale()
	#image = 'Risultati/result_2018_2_25_13.jpg'
#-------------Converte immagine in base64 e conta i caratteri che la compongono----
	image_64 = base64.encodestring(open(image,"rb").read())
	print(image_64)
	print(len(image_64))


	num = len(image_64) #Numero caratteri composti dall'immagine
	#num = 1000
	dec = 0 #Contatore per pacchettidi stringhe
	nuova_stringa = ""
#---Ciclo per creazione pacchetti di stringhe e rimozione dei caratteri che non vengono letti dalle dongle----
	for n in range(0,num):
		print(n)
		time.sleep(0.2)
		if n > 0:
			dec = dec+90
			n = dec
			if n > num:
				break
			else:	
				print(n)
				m = n+90
				if m > num:
					m = num
					nuova_stringa = image_64[n:m].replace("/","_")
					nuova_stringa = nuova_stringa.replace("\n","")
					nuova_stringa = nuova_stringa.replace("=",".")
					print(nuova_stringa)
					invio.invio_dongle("image",nuova_stringa)
					#time.sleep(0.05)
				else:
					#print(m)
					nuova_stringa = image_64[n:m].replace("/","_")
					nuova_stringa = nuova_stringa.replace("\n","")
					nuova_stringa = nuova_stringa.replace("=",".")
					print(nuova_stringa)
					invio.invio_dongle("image",nuova_stringa)
					#time.sleep(0.05)
		else:
			print(n)
			m = n+90
			#print(m)
			nuova_stringa = image_64[n:m].replace("/","_")
			nuova_stringa = nuova_stringa.replace("\n","")
			nuova_stringa = nuova_stringa.replace("=",".")
			print(nuova_stringa)
			invio.invio_dongle("image",nuova_stringa)
			#time.sleep(0.05)


	print("----Frammentazione conclusa---")
	invio.invio_dongle("onoff","1")
