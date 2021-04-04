  #                                          Monitoramento da Velocidade da internet :signal_strength:

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
- [Code linting](#code-linting)
- [Observações](#observações-eyes)
- [Bibliotecas utilizadas](#bibliotecas-utilizadas-books) 
- [Melhorias](#melhorias-rocket)
- [Desenvolvedores e Contribuintes](#desenvolvedores-e-contribuintes-computer)
- [Licença](#licença-grey_exclamation)



## Descrição do projeto :file_folder:

<p align="justify">
  Gerenciar e armazenar a velocidade da internet a cada meia hora.
</p>




## Funcionalidades :gear:

:heavy_check_mark: Armazenamento automático no Excel

:heavy_check_mark: Roda background, não afetando outras tarefas (exceto se estiver instalando pacotes do python)

:heavy_check_mark: O intervalo de tempo é ajustável


## Pré-requisitos :pushpin:

### Instalação de dependências

Após clonar o projeto localmente, instalar as dependências de desenvolvimento e do projeto via algum ambiente
virtual para Python de sua escolha. Aqui foi utilizado o [virtualenv](https://virtualenv.pypa.io/en/latest/) para Python 3.8.

Executar, na raiz do projeto:

```bash
$ virtualenv --python=python3 venv \
&& source venv/bin/activate \
&& pip install --upgrade pip \
&& pip install -r requirements-dev.txt \
&& pip install -r requirements.txt
```


### Armazemamento de resultados no Excel:

- Criar uma planilha nomeada como 'base';

- Nomear três colunas, por exemplo, 'Data', 'Hora'  e 'Velocidade';

- Salvar como dados.xlsx.

  ![1](https://user-images.githubusercontent.com/29557513/113329422-ea448780-92f3-11eb-8111-fda38fa7a05c.png)

  

  ![2](https://user-images.githubusercontent.com/29557513/113329582-20820700-92f4-11eb-80fe-7f555f6278f3.png)

  

## Como rodar a aplicação :arrow_forward:

```bash
$ chmod 777 main.py
$ ./main.py
```

O serviço agora irá periodicamente atualizar a planilha Excel em `test_results/speed-data.xlsx`. A saída do script deverá
ser similar à:

![main-output](https://user-images.githubusercontent.com/35070513/113494643-858a5800-94c0-11eb-8be6-5a21b1de8776.png)

Para encerrar o script, basta pressionar `Ctrl+C`.

## Code linting

O code linting aqui é realizado com o auxílio da biblioteca [prospector](). Para executar a mesma, basta roda na raíz do projeto:

```bash
$ prospector
```

Caso o código esteja seguindo as PEPs e não existam inconsistências nas anotações de tipos, a saída deverá ser similar à:

![prospector-output](https://user-images.githubusercontent.com/35070513/113494802-4ceb7e00-94c2-11eb-86c2-bc71c322d30e.png)

## Observações :eyes:

A ideia do projeto surgiu em um momento de estresse por perceber a internet travando e resolvi postar no LinkedIn para outras pessoas fazerem o mesmo e poderem contestar com a operadora (tendo provas em mão).

Pesquisei anteriormente a fidedignidade do site Speedtest e se era válido, como prova, os dados gerados. Para quem quiser dar uma olhada, há dois sites bem interessantes que abordam esses assuntos:

- [Comparação de sites que testam a velocidade da internet](https://melhorescolha.com/blog/teste-de-velocidade-resultados-diferentes/)
- [Provas para contestar com a operadora de banda larga](https://blog.intnet.com.br/entenda-como-fazer-o-teste-de-velocidade-da-sua-internet/)

A diferença dos megabytes testados é muito mínima, pela facilidade e disponibilidade eu escolhi o speedtest.

O ideal é rodar o programa com o cabo ethernet conectado no computador, porém com o Wifi você já pode ter ideia se a qualidade da internet está muito inferior da contratada.

Como eu fiz no momento de "desespero" o código, com o tempo, irei fazer melhorias (como listadas abaixo).



## Bibliotecas utilizadas :books:

### Produção
- [SpeedTest](https://pypi.org/project/speedtest-cli/)
- [Threading](https://pypi.org/project/threaded/)
- [Pandas](https://pypi.org/project/pandas/)
- [Openxl](https://pypi.org/project/openpyxl/)
### Desenvolvimento
- [Prospector](https://pypi.org/project/prospector/)
- [Mypy](http://mypy-lang.org/)


## Melhorias :rocket:

:memo: Incluir o nPerf, ping, upload, hora de início e término para rodar o programa;

:memo: Armazenar os dados em uma banco de dados relacional, printar na tela em tempos em tempos a média da velocidade até aquele momento;

:memo: Fazer input permitindo que o usuário entre com dados da sua velocidade contratada e o custo dela;

:memo: Fazer uma análise de estatística básica de velocidade por dia/mês/porcentagem, o quanto está sendo descontado e o quanto deveria ser cobrado/dia pela velocidade que chega.



## Desenvolvedores e Contribuintes :computer:

- Bárbara Guerbas de Figueiredo - [LinkedIn]( https://www.linkedin.com/in/barbaragfigueiredostatistics/) - [Email](baguerbassita@gmail.com)
- Guilherme Lima Gonçalves - [LinkedIn]( https://www.linkedin.com/in/guligon90/) - [Email](guligon90@gmail.com)



## Licença :grey_exclamation:

The [MIT License]() (MIT)

Copyright :copyright: 2021 - TestSpeed
