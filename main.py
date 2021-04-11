from speedtest import Speedtest
from datetime import datetime
import csv
import time
# função para gravar dados da velocidade da internet
def main():
    while True:
        agora = datetime.now()
        data_atual = agora.strftime('%d/%m/%Y')
        hora_atual = agora.strftime('%H:%M')
        velocidade = Speedtest().download(threads=None)*(10**-6)
        try:
            with open('dados.csv', 'wt', newline ='') as csvfile:
                fieldnames = ['Data', 'Hora', 'Velocidade']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                csvWriter = csv.writer(csvfile, delimiter=',')
                csvWriter.writerow([data_atual, hora_atual, round(velocidade)])
                writer.writerow({'Data': data_atual, 'Hora': hora_atual, 'Velocidade': f'{round(velocidade, 2)}MB'})
                print(data_atual, hora_atual, round(velocidade))
        except PermissionError:
            print("Feche o arquivo CSV para prosseguir...")
        time.sleep(1800)

main()
