from speedtest import Speedtest
from datetime import datetime
import csv
import time


def retornarInformacoesAnteriores():
    informacoesAnteriores = []
    with open('dados.csv', newline='') as csvfile:
        leitorDeCSV = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for linha in leitorDeCSV:
            elementosDaLinha = linha[0].split(",")
            if 'Data' not in elementosDaLinha[0]:
                informacoesAnteriores.append(elementosDaLinha)

    return informacoesAnteriores


def retornarInformacoesDeAgora():
    agora = datetime.now()
    dataAtual = agora.strftime('%d/%m/%Y')
    horaAtual = agora.strftime('%H:%M')
    velocidade = Speedtest().download(threads=None)*(10**-6)
    return dataAtual, horaAtual, velocidade


def escreverInformacoes(dataAtual, horaAtual, velocidade):
    while True:
        try:
            informacoesAnteriores = retornarInformacoesAnteriores()
            with open('dados.csv', 'wt', newline ='') as csvfile:
                fieldnames = ['Data', 'Hora', 'Velocidade']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for linha in informacoesAnteriores:
                    writer.writerow({'Data': linha[0], 'Hora': linha[1], 'Velocidade': f'{linha[2]} MB'})
    
                writer.writerow({'Data': dataAtual, 'Hora': horaAtual, 'Velocidade': f'{round(velocidade, 2)} MB'})
                print(f'[DATA] {dataAtual} [HORA] {horaAtual} [VELOCIDADE] {round(velocidade, 2)} MB')
                break
        except PermissionError:
            print('Não tenho permissão pra fazer isso... Caso esteja aberto feche o arquivo CSV para prosseguir...')
            time.sleep(5)


def main():
    while True:
        dataAtual, horaAtual, velocidade = retornarInformacoesDeAgora()
        escreverInformacoes(dataAtual, horaAtual, velocidade)
        time.sleep(1800) #Dormir 30 Minutos

main()
