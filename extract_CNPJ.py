
import pandas as pd

exemplo = pd.read_csv('/Users/joaogoncalves/Documents/SinteseData/Projeto-CNPJ/Primeira_Entrega/Datasets/file_01.csv')

print(exemplo.shape)
exemplo.head(10)

import os

def pegar_lista_csv_na_pasta(pasta):
  directory = pasta
  files = []
  for filename in os.listdir(directory):
    # print(filename)
    # print('separa')
    # print(directory)
    f = os.path.join(directory, filename)
    # print(f)

    if (os.path.isfile(f)) and ('.csv' in f) and ('file_' in f):
      files.append(f)
  return files

lista_csv = pegar_lista_csv_na_pasta('/Users/joaogoncalves/Documents/SinteseData/Projeto-CNPJ/Primeira_Entrega/Datasets')

#mostra apenas os 6 primeiros arquivos
print(lista_csv[0:5])

lista_csv[0][9:]
#resultado deve ser file_01.csv (varia o tamanho da string do diretório que o arquivo está)

def criando_arquivos_apenas_cnpj(lista_csv):
  for caminho_csv in lista_csv:
    arquivo_df = pd.read_csv(caminho_csv)

    #mudar de acordo com o resultado do codigo acima, referente ao nome do arquivo
    nome_arquivo = caminho_csv[9:]
    #crio um novo dataframe com uma coluna cnpj
    cnpj_df = pd.DataFrame(columns=['cnpj'])
    
    cnpj_df['cnpj'] = arquivo_df['cnpj']
    
    #deve existir a pasta 'apenas_cnpj'
    cnpj_df.to_csv('/Users/joaogoncalves/Documents/SinteseData/Projeto-CNPJ/Primeira_Entrega/Datasets/apenas_cnpj/' + nome_arquivo)
    print(nome_arquivo + ' criado.')

criando_arquivos_apenas_cnpj(lista_csv)

#teste de arquivos criados
lista_cnpj_csv = pegar_lista_csv_na_pasta('/Users/joaogoncalves/Documents/SinteseData/Projeto-CNPJ/Primeira_Entrega/Datasets/apenas_cnpj')
lista_cnpj_csv

cnpj_1 = pd.read_csv(lista_cnpj_csv[0])

cnpj_1.head(6)

#excluir indice da tabela originaria
# cnpj_1_drop = cnpj_1.drop(columns = ['Unnamed: 0'])

# cnpj_1_drop.to_csv('caminho + nome_arquivo')