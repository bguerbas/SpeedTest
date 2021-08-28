import speedtest
from datetime import datetime
import pandas as pd
from threading import Timer

minutos = 3

# função para gravar dados da velocidade da internet
def internet():
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')

    try:
        s = speedtest.Speedtest()
        velocidade = s.download(threads=None)*(10**-6)
        upload = s.upload(threads=None)*(10**-6)
        df.loc[len(df)] = [data_atual, hora_atual, round(velocidade), round(upload)]
        df.to_excel('dados.xlsx', sheet_name='base', index=False)
    except:
        print("Erro, internet sem conexão")
        velocidade = 0
        upload = 0
        df.loc[len(df)] = [data_atual, hora_atual, velocidade, upload]
        df.to_excel('dados.xlsx', sheet_name='base', index=False)
    
    print("Registro feito na planilha. " + hora_atual + " | Velocidade download: " + str(round(velocidade)) + " | Velocidade upload: " + str(round(upload)))

    
    Timer((60*minutos), internet).start()

print("Timer iniciado, executar a cada " + str((60*minutos)/60) + " minutos")
internet()


