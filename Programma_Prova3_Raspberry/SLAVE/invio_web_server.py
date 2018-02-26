import pycurl


#Funzione per l'invio della foto sul web server
def invio_foto(url_foto):
    print("Invio foto sul web server...")
    c = pycurl.Curl()
    c.setopt(c.URL, '192.168.43.233/test/SlimApp/public/index.php')

    c.setopt(c.HTTPPOST, [
        ('fileupload', (
            # upload the contents of this file
            c.FORM_FILE, url_foto,
        )),
    ])

    c.perform()
    c.close()
    print("Foto inviata!")
