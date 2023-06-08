<h1 align="center"> Roteiro para tratamento Dataset-CNPJ</h1>

> Status do Projeto: ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Deploy da Aplicação](#deploy-da-aplicação-dash)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

## Descrição do projeto 

<p align="justify">
  O tratamento foi necessário devido ao seu tamanho. Um arquivo .csv de
 45milhões de linhas (2,27GB)
 A estratégia usada foi após o download e decompressão do arquivo não 
 abrir ou carregar os dados. Antes de qualquer coisa o arquivo foi 
 dividido em varios outros arquivos. Cada novo arquivo tem 1milhão de 
 linhas, totalizando 45 novos arquivos.
</p>

## Funcionalidades

:heavy_check_mark: Tratar uma base de dados massiva

:heavy_check_mark: Descartar dados impropios, incompletos ou nulos

:heavy_check_mark: Divisão e organização padrão de dados para ser processado posteriomente

:heavy_check_mark: Tamanho do arquivo compatível e acessivél por um computador doméstico


## Pré-requisitos

:warning: Um sistema operacional baseado em Unix/Linux

...

:warning: [Git]

...

Ferramenta para controle de versão

## Como rodar a aplicação:

No terminal, clone o projeto: 

```
git clone https://github.com/joaolfgoncalves/script-CNPJ
```
... 
Após clonar o repositório, dentro do mesmo diretorio, baixe o  Dataset com todos os CNPJ pelo link:

```
ttps://drive.google.com/drive/folders/10Gs6lMbIJ_JB1q55DHSoWBkDPSsnqMSc?usp=share_link
```

## Após o download execute o seguinte script:

```
` split -l 1000000 -d empresas.csv file_ `
```

## Etapa 2: 
Loop para renomear e adicionar a estensão .csv em todos os arquivos gerados

`for i in $(find file_*); do mv $i "$i.csv"; done `

## Etapa 3:
Adicionando o cabeçalho CSV (o cabeçalho ficou no primeiro arquivo file_00.csv ), aos arquivos gerados  

`for i in $(find . -type f -name "file_*.csv" -not -name "file_00.csv");
    do echo "$(head -1 empresas.csv)\n$(cat $i)" > $i; done`

## Etapa 4: Após dividir o arquivo em vários arquivos menores, vamos usar Python limpar os dados e tirar informações que não são interessantes no momento, organizar e padronizar todos.

:warning: Mesmo dividindo em arquivo menores, o processamento continua dificil. A solução encontrada foi usar o Google Colab pela sua disponibilidade de processamento e memória RAM. Abaixo segui o link para o notebook com o script em python:

```
https://colab.research.google.com/drive/1yb5SvXbW_YHouyYs8yLFo8UHft4JcAFa?usp=sharing#scrollTo=H-i5_Siw-WEx
```

:warning: Para execução e processamento dos dasdos, os dados devem ser colocados em um GoogleDrive para ter acesso pelo Colab.

:warning: * Tentei deixar os dados localmente mas o resultado não foi como esperado. Para garantir uma boa execução suba os arquivos para um pasta no
GoogleDrive e linke ela no script que será exeecutado no Google Colab. Ao abri o Colab, observe as orientações para inserir o diretorio correto com a base de dados

## Conclusão: 
Após a execusão vamos obteer 43 arquivos, cada um com 1milhão de CNPJ, tabelados e enumerados.
Os dados foram normalizados da melhor forma para ser usado em uma aplicação já existente. Mas o script pode ser facilmente alterado para outras preferências e finalidades.
## Desenvolvedores/Contribuintes :octocat:
 
 (https://github.com/joaolfgoncalves)
