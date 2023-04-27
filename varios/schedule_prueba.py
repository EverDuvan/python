import pandas as pd
import schedule
import time

def job():
    datos = {'Nombre': ['Juan', 'María', 'Pedro', 'Luisa'],
            'Edad': [25, 30, 35, 28],
            'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}
    df = pd.DataFrame(datos)
    print(df)
    print ('end')
#schedule.every().day.at("01:00").do(job)
#schedule.every(0.05).minutes.do(job)
schedule.every(5.95).seconds.do(job)

while True:
    schedule.run_pending()
    #time.sleep(1) # wait one minute
