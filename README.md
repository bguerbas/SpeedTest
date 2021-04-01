# Monitoramento da Velocidade da internet :signal_strength:

<p align="center">
  <img src="https://img.shields.io/static/v1?label=python&message=3.8&color=blue&style=for-the-badge&logo=python"/>
</p>



> Status do Projeto: :heavy_check_mark: (pronto)

### Tópicos :writing_hand:

- [Descrição do projeto](#descrição-do-projeto-file_folder)

- [Funcionalidades](#funcionalidades-gear)

- [Deploy da Aplicação](#deploy-da-aplicação-dash)

- [Pré-requisitos](#pré-requisitos-pushpin)

- [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)
- [Observações](#observações-eyes)
- [Bibliotecas utilizadas](#bibliotecas-utilizadas-books) 
- [Melhorias](#melhorias-rocket)
- [Desenvolvedores/Contribuintes](#desenvolvedores/contribuintes-computer)
- [Licença](#licença-grey_exclamation)



## Descrição do projeto :file_folder:

<p align="justify">
  Gerenciar e armazenar a velocidade da internet a cada meia hora.
</p>




## Funcionalidades :gear:

:heavy_check_mark: Armazenamento automático no Excel

:heavy_check_mark: Roda background, não afetando outras tarefas (exceto se estiver instalando pacotes do python)

:heavy_check_mark: O intervalo de tempo é ajustável



## Deploy da Aplicação :dash:

![ezgif.com-gif-maker](C:\Users\bague\Downloads\ezgif.com-gif-maker.gif)



## Pré-requisitos :pushpin:

No Python (salvar o script como TestSpeed.py) :

```
pip install pandas
```

```
pip install threaded
```

```
pip install speedtest-cli
```

No Excel:

- Criar uma planilha nomeada como 'base';

- Nomear três colunas, por exemplo, 'Data', 'Hora'  e 'Velocidade';

- Salvar como dados.xlsx.

  ![1](D:\VelocidadeInternet\1.png)

  

  ![2](D:\VelocidadeInternet\2.png)

  

## Como rodar a aplicação :arrow_forward:

No terminal navegar até o diretório onde se encontram os arquivos [Excel](https://github.com/bguerbas/SpeedTest/blob/main/dados.xlsx) e o [TestSpeed.py](https://github.com/bguerbas/SpeedTest/blob/main/TestSpeed.py), e digitar:

```
python TestSeep.py
```



## Observações :eyes:

A ideia do projeto surgiu em um momento de estresse por perceber a internet travando e resolvi postar no LinkedIn para outras pessoas fazerem o mesmo e poderem contestar com a operadora (tendo provas em mão).

Pesquisei anteriormente a fidedignidade do site Speedtest e se era válido, como prova, os dados gerados. Para quem quiser dar uma olhada, há dois sites bem interessantes que abordam esses assuntos:

- [Comparação de sites que testam a velocida da internet](https://melhorescolha.com/blog/teste-de-velocidade-resultados-diferentes/)
- [Provas para contestar com a operadora de banda larga](https://blog.intnet.com.br/entenda-como-fazer-o-teste-de-velocidade-da-sua-internet/)

A diferença dos megabytes testados é muito mínima, pela facilidade e disponibilidade eu escolhi o speedtest.

O ideal é rodar o programa com o cabo ethernet conectado no computador, porém com o Wifi você já pode ter ideia se a qualidade da internet está muito inferior da contratada.

Como eu fiz no momento de "desespero" o código, com o tempo, irei fazer melhorias (como listadas abaixo).



## Bibliotecas utilizadas :books:

- [SpeedTest](https://pypi.org/project/speedtest-cli/)
- [Threading](https://pypi.org/project/threaded/)
- [Pandas](https://pypi.org/project/pandas/)



## Melhorias :rocket:

:memo: Incluir o nPerf, ping, upload, hora de início e término para rodar o programa;

:memo: Armazenar os dados em uma banco de dados relacional;

:memo: Fazer input permitindo que o usuário entre com dados da sua velocidade contratada e o custo dela;

:memo: Fazer uma análise de estatística básica de velocidade por dia/mês, o quanto está sendo descontado e o quanto deveria ser cobrado/dia pela velocidade que chega.



## Desenvolvedores/Contribuintes :computer:

- Bárbara Guerbas de Figueiredo - [LinkedIn]( https://www.linkedin.com/in/barbaragfigueiredostatistics/) - [Email](baguerbassita@gmail.com)



## Licença :grey_exclamation:

The [MIT License]() (MIT)

Copyright :copyright: 2021 - TestSpeed
