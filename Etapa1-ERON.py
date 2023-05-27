import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# carregue os módulos de sua preferência aqui

df = pd.read_csv('/content/enron.csv')
df.head(5)

qntd_individuos = df.shape[0]
num_colunas = df.shape[1]
df_poi = df[df['poi'] == True]
df_no_poi = df[df['poi'] == False]
qntd_poi = df_poi.shape[0]
qntd_no_poi = df_no_poi.shape[0]

#separando os tipos de variaveis
df_numerico = df.drop(['poi', 'email_address','name'], axis=1)
df_categorico = df[['poi', 'email_address','name']]


#gerando estatísticas dos dados numéricos
estatisticas = pd.DataFrame({
    'Média': df_numerico.mean(),
    'Mediana':df_numerico.median(),
    'Variância': df_numerico.var(),
    'Desvio Padrão': df_numerico.std(),
    'Quartil 25%':df_numerico.quantile(0.25),
    'Quartil 50%':df_numerico.quantile(0.5),
    'Quartil 75%': df_numerico.quantile(0.75)
})

#Moda e valores únicos das colunas
moda = df_categorico.mode().iloc[0]
valores_unicos = df_categorico.nunique()

print('APRESENTAÇÃO DE DADOS DESCRITIVOS')
print('Quantidade de indivíduos analisados: ',qntd_individuos)
print('Quantidade de variáveis analisadas: ',num_colunas)
print('Quantidade de indivíduos envolvidos na fraude (POI): ',qntd_poi)
print('Quantidade de indivíduos que NÃO ESTÃO envolvidos na fraude (non-POI): ',qntd_no_poi)
print('-------//-------------------//-----------------//----------------')
print('Estatísticas das variáveis númericas:')
estatisticas




