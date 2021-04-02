import speedtest
from datetime import datetime
import pandas as pd
from threading import Timer

# função para gravar dados da velocidade da internet


class internet_speed_data:
    def __init__(self):
        date = None
        time = None
        speed = None


class internet_speed(internet_speed_data):
    def determine:
        date = datetime.now().strftime('%d/%m/%Y')
        time = datetime.now().strftime('%H:%M')
        speed = s.download(threads=None)*(10**-6)


def internet():
    print("starting")
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    s = speedtest.Speedtest()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    velocidade = s.download(threads=None)*(10**-6)
    print(velocidade)
    df.loc[len(df)] = [data_atual, hora_atual, round(velocidade)]
    df.to_excel('dados.xlsx', sheet_name='base', index=False)
    Timer(1, internet).start()


internet()
