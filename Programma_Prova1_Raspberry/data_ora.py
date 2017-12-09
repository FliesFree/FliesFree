import datetime

i = datetime.datetime.now()

def data_ora_attuale():    
    data_odierna = "%s_%s_%s_%s"%(i.year,i.month,i.day,i.hour)
    return data_odierna

def ora_attuale():
    return "%s_%s_%s_%s" %(i.hour)

def data_attuale():
    return "%s_%s_%s_%s" %(i.year,i.month,i.day)
