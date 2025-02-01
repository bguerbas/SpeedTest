import speedtest
from datetime import datetime
import pandas as pd
from threading import Timer
from twilio.rest import Client

# Configuração do Twilio
TWILIO_SID = "SEU_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "SEU_AUTH_TOKEN"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Número do Twilio para WhatsApp
SEU_NUMERO_WHATSAPP = "whatsapp:+55SEUNUMERO"  # Substitua pelo seu número com código do país

def enviar_alerta_whatsapp(mensagem):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=mensagem,
        to=SEU_NUMERO_WHATSAPP
    )

# Função para gravar dados da velocidade da internet
def internet():
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    s = speedtest.Speedtest()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    velocidade = s.download(threads=None) * (10 ** -6)  # Convertendo para Mbps

    # Adiciona os dados ao arquivo Excel
    df.loc[len(df)] = [data_atual, hora_atual, round(velocidade)]
    df.to_excel('dados.xlsx', sheet_name='base', index=False)

    # Se a velocidade for menor que 200 Mbps, envia alerta via WhatsApp
    if velocidade < 200:
        mensagem = f"⚠️ Alerta de Internet Lenta!\nVelocidade registrada: {round(velocidade)} Mbps\nData: {data_atual} - Hora: {hora_atual}"
        enviar_alerta_whatsapp(mensagem)

    # Reexecuta a função a cada 5 minutos (300 segundos)
    Timer(120, internet).start()

internet()
