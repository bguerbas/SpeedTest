import speedtest
from datetime import datetime
import pandas as pd
from threading import Timer
from ping3 import ping

minutos = 3
# Criando classe para facilitar o armazenamento do resultado do ping
class PingRes:
    def __init__(self, host, mensagem, resultado):
        self.host = host
        self.mensagem = mensagem
        self.resultado = resultado

# função para gravar dados da velocidade da internet
def internet():
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')

    try:
        s = speedtest.Speedtest()
        velocidade = s.download(threads=None)*(10**-6)
        upload = s.upload(threads=None)*(10**-6)
        pingtest = pingPong()

        for i in pingtest:
            if i.host == "Google:":
                pingGoogle = i
            elif i.host == "AWS_Brasil:":
                pingAWS = i
            elif i.host == "Youtube:":
                pingYoutube = i
            elif i.host == "Facebook:":
                pingFacebook = i
            elif i.host == "Instagram:":
                pingInstagram = i

        df.loc[len(df)] = [data_atual, hora_atual, round(velocidade), round(upload), pingGoogle.resultado, pingGoogle.mensagem, pingAWS.resultado, pingAWS.mensagem, pingYoutube.resultado, pingYoutube.mensagem, pingFacebook.resultado, pingFacebook.mensagem, pingInstagram.resultado, pingInstagram.mensagem]
        df.to_excel('dados.xlsx', sheet_name='base', index=False)
    except:
        print("Erro, internet sem conexão")
        velocidade = 0
        upload = 0
        res = PingRes(0, "Erro, internet sem conexão", 0)
        pingGoogle = res
        pingAWS = res
        pingYoutube = res
        pingFacebook = res
        pingInstagram = res

        df.loc[len(df)] = [data_atual, hora_atual, round(velocidade), round(upload), pingGoogle.resultado, pingGoogle.mensagem, pingAWS.resultado, pingAWS.mensagem, pingYoutube.resultado, pingYoutube.mensagem, pingFacebook.resultado, pingFacebook.mensagem, pingInstagram.resultado, pingInstagram.mensagem]
        df.to_excel('dados.xlsx', sheet_name='base', index=False)
    
    print("Registro feito na planilha. " + hora_atual + " | Velocidade download: " + str(round(velocidade)) + " | Velocidade upload: " + str(round(upload))+ " | Ping Google: " + str(round(pingGoogle.resultado)))

    
    Timer((60*minutos), internet).start()

# função para realizar o ping na lista de hosts fornecida
def pingPong():
    # Abre e lê o arquivo contendo os hosts e IPs
    with open("D:\Dev\Python\lista_ips.txt") as file:
        lista = file.read()
        lista = lista.splitlines()
    resposta = []

    # Percorre a lista de hosts e executa o ping em cada um
    for i in lista:
        ip = i.split()[1]
        host = i.split()[0]
        res = round(ping(ip, unit='ms'))
        if res == False:
            resposta.append(PingRes(host, "Host desconhecido", 0))

        elif res == 0:
            resposta.append(PingRes(host, "Sem resposta do host", 0))

        else:
            resposta.append(PingRes(host, "Resposta recebida", res))
    
    return resposta


print("Timer iniciado, executar a cada " + str((60*minutos)/60) + " minutos")
internet()

