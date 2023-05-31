# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# carregue os módulos de sua preferência aqui

"""# Carregamento de dados

Na célula abaixo é realizado o carregamento da base de dados.
Você **não** deve alterar o código apresentado.
"""

df = pd.read_csv('/content/enron.csv')
df.head(5)

"""Verificando se os dados carregaram corretamente:"""

df.head(5)

"""# Análise descritiva de dados

Nesta etapa, você conduzirá uma análise descritiva da base de dados da Enron.

Para a base de dados como um todo, você deve reportar:
- O número de indivíduos (instâncias) na tabela;
- O número de variáveis descritivas (colunas ou atributos) destes indivíduos;
- O número de pessoas de interesse, isto é, fraudadores (POIs) e não-POIs;

Para cada uma das variáveis numéricas, você deve apresentar:
- Média
- Mediana
- Variância
- Desvio padrão
- Quartis

E para cada uma das variáveis categóricas:
- A moda
- Os valores únicos de cada variável

Além de apresentar estatísticas sobre cada variável da base de dados, a análise a ser conduzida nesta etapa requer uma análise crítica. 
Desta forma, você é convidado a extrair *insights* a partir destas estatísticas, verificando se os valores apresentados condizem ou não com a realidade.
**Lembre-se: todas estas estatísticas devem ser calculadas e apresentadas, de forma legível, no relatório fornecido na descrição da ATP.**

"""

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

print('Estatísticas das variáveis categóricas:')
print('MODA:')
moda

print('Estatísticas das variáveis categóricas:')
print('MODA:')
moda
print('--------')
print('Valores Únicos')
valores_unicos

"""##Insights






1. A análise das medidas de Média e Mediana revela que algumas colunas, como "**bonus**" e "**exercised_stock_options**", possuem valores extremamente altos que influenciam a média, resultando em uma média maior que a mediana. Isso sugere a presença de **casos excepcionais ou outliers nessas colunas**, que podem ser de interesse para investigações adicionais.

2. Ao considerar a Variância e o Desvio Padrão, notamos que a coluna "**loan_advances**" apresenta uma dispersão significativamente maior em comparação com outras colunas. Isso indica que os valores nessa coluna variam amplamente em relação à média, sugerindo uma maior variabilidade nos dados. Essa descoberta pode ser relevante para identificar **casos atípicos ou padrões incomuns relacionados a empréstimos**.

# Análise univariada de dados

Nesta seção, você conduzirá uma análise univariada de dados.
Esta análise deve contemplar **todas** as variáveis disponíveis na base de dados, exceto o **nome do indivíduo**.
O objetivo desta etapa é identificar o comportamento das variáveis, verificando curtose e assimetria, assim como extraindo insights sobre cada variável individualmente.
Desta forma, para cada variável, trabalhe com as seguintes etapas:

* Crie um cabeçalho no relatório com o nome da variável;
* Crie visualizações univariadas (histogramas, box-plots, etc), de acordo com o tipo de dado; e
* Apresente as principais conclusões que podemos obter a partir destas visualizações.

## Bonus
"""

describe = df['bonus'].describe()
print(describe)

plt.boxplot(df['bonus'].dropna())
plt.title('Boxplot - Bônus')
plt.xlabel('Bônus')
plt.show()

"""#### Análise crítica
 O desvio padrão é de aproximadamente 10.71 milhões. Isso indica **uma grande variabilidade** nos valores de "bonus" recebidos pelos funcionários da empresa. Alguns funcionários podem ter recebido bônus significativamente maiores ou menores do que a média que foi aproximadamente 2,37M.
 É relevante observar o valor máximo dos bônus recebidos pelos funcionários, que é de aproximadamente 97.343.620. Esse **valor é muito superior aos outros quartis** e indica que existe pelo menos um funcionário na empresa ERON que recebeu um bônus excepcionalmente alto em comparação com os demais.

# Pagamentos diferidos (deferral_payments)
"""

describe = df['deferral_payments'].describe()
print(describe)

plt.boxplot(df['deferral_payments'].dropna())
plt.title('Boxplot - Pagamentos Diferidos')
plt.xlabel('Pagamentos Diferidos')
plt.show()

"""### Análise crítica
O desvio padrão é de aproximadamente 5.16 milhões. Isso indica uma grande variabilidade nos valores de pagamentos postergados recebidos pelos funcionários. Alguns funcionários podem ter valores de postergamento significativamente maiores ou menores do que a média.
O valor mínimo de pagamentos diferidos foi negativo (-102.500)
O valor do primeiro quartil é de aproximadamente 81.573. Isso significa que 25% dos funcionários tiveram um valor de postergamento igual ou inferior a esse valor. Essa informação indica que uma parcela significativa dos funcionários teve valores de postergamento relativamente baixos.
O valor máximo é de aproximadamente 32.083.400. Esse valor é muito maior do que os outros quartis, indicando que pode haver pelo menos um funcionário com um valor de postergamento excepcionalmente alto em comparação com os demais.

## Renda diferida
"""

describe = df['deferred_income'].describe()
print(describe)

plt.boxplot(df['deferred_income'].dropna())
plt.title('Boxplot - Renda Diferidas')
plt.xlabel('Renda Diferidas')
plt.show()

"""### Análise Crítica

O valor máximo é de aproximadamente -833. Esse valor negativo indica que pelo menos um funcionário possui uma renda diferida muito baixa em comparação com os demais.

## Honorários do diretor (director_fees)
"""

describe = df['director_fees'].describe()
print(describe)

plt.boxplot(df['director_fees'].dropna())
plt.title('Boxplot - Honorários do Diretor')
plt.xlabel('Honorários do diretor')
plt.show()

"""### Análise Crítica

O desvio padrão mais uma vez indica uma variabilidade nos valores ou seja funcionários podem ter taxas de diretor significativamente maiores ou menores do que a média.
Apenas comparando o valor mínimo de 3.285 e o máximo de 1.398.517 percebemos a diferença.

# Opções de ações exercidas (exercised_stock_options)
"""

describe = df['exercised_stock_options'].describe()
print(describe)

plt.boxplot(df['exercised_stock_options'].dropna())
plt.title('Boxplot - exercised_stock_options')
plt.xlabel('exercised_stock_options')
plt.show()

"""### Análise Crítica

Seguindo o padrão das variáveis anteriores, desvio padrão muito maior do que a média e max e min comprovando a variabiliade dos valores.
Achei interessante o fato de que quase 70% dos indivíduos analisados possuem alguma ação exercida, ao contrário de outras variáveis como bonus e director fees.

## Despesas (expenses)
"""

describe = df['expenses'].describe()
print(describe)

plt.boxplot(df['expenses'].dropna())
plt.title('Boxplot - Despesas')
plt.xlabel('exercised_stock_options')
plt.show()

"""### Análise Crítica
 O valor mínimo de "expenses" é de 148. Isso indica que existem funcionários que tiveram gastos relativamente baixos.
 O valor do primeiro quartil é de aproximadamente 22.614. Isso significa que 25% dos funcionários tiveram gastos iguais ou inferiores a esse valor. Essa informação indica que uma parcela significativa dos funcionários teve gastos relativamente baixos.
 O valor do terceiro quartil é de aproximadamente 79.952. Isso significa que 75% dos funcionários tiveram gastos iguais ou inferiores a esse valor. Essa informação mostra que a maioria dos funcionários teve gastos dentro dessa faixa.
 O valor máximo de despesas é de aproximadamente 5.235.198. Esse valor indica que existe pelo menos um funcionário que teve um gasto excepcionalmente alto em comparação com os demais.

## from_messages
"""

describe = df['from_messages'].describe()
print(describe)

plt.boxplot(df['from_messages'].dropna())
plt.title('Boxplot - from_messages')
plt.xlabel('from_messages')
plt.show()

"""### Análise Crítica

O valor do terceiro quartil é de aproximadamente 145.5. Isso significa que 75% dos funcionários enviaram 145 mensagens ou menos. Essa informação mostra que a maioria dos funcionários enviou uma quantidade relativamente baixa de mensagens.

O valor máximo é de 14368. Esse valor indica que existe pelo menos um funcionário que enviou um número excepcionalmente alto de mensagens em comparação com os demais.

## from_poi_to_this_person
"""

describe = df['from_poi_to_this_person'].describe()
print(describe)

plt.hist(df['from_poi_to_this_person'], bins=10, edgecolor='k')
plt.xlabel('Quantidade de Mensagens Recebidas de Pessoas de Interesse (POI)')
plt.ylabel('Frequência')
plt.title('Histograma - from_poi_to_this_person')
plt.show()

"""### Análise Crítica

Interessante observar que enquanto tiveram funcionarios que NÃO RECEBERAM nenhuma mensagem de um POI, O valor do terceiro quartil é de aproximadamente 72.25. Isso significa que 75% dos funcionários receberam 72 mensagens ou menos dos remetentes de interesse. e teve pelo menos um funcionário que recebeu mais de 500 mensagens de um POI

## from_this_person_to_poi
"""

describe = df['from_this_person_to_poi'].describe()
print(describe)

plt.hist(df['from_this_person_to_poi'], bins=10, edgecolor='k')
plt.xlabel('Quantidade de Mensagens para Pessoas de Interesse (POI)')
plt.ylabel('Frequência')
plt.title('Histograma - from_this_person_to_poi')
plt.show()

"""### Análise Crítica

Houveram pessoas que não mandaram mensagens para pessoas envolvidas na fraude enquanto 75% dos dados válidos dessa variável enviaram ate 24 mensagens para POIs
Tendo um ou mais que enviou cerca de 600 mensagens para POIs

## loan_advances
"""

describe = df['loan_advances'].describe()
print(describe)

plt.hist(df['loan_advances'], bins=10)
plt.xlabel('Loan Advances')
plt.ylabel('Frequência')
plt.title('Histograma - Loan Advances')
plt.show()

"""### Análise Crítica

Interessante observar que foram feitos apenas 4 empréstimos onde o valor minimo foi de 400k e o máximo de 83M. Esta variável pode ser muito útil para indicar um POI.

## long_term_incentive
"""

describe = df['long_term_incentive'].describe()
print(describe)

plt.hist(df['long_term_incentive'], bins=10)
plt.xlabel('incentivo de longo prazo')
plt.ylabel('Frequência')
plt.title('Histograma - incentivo de longo prazo')
plt.show()

"""### Análise Crítica
Ao relacionar o valor mínimo e o valor máximo da variável "long_term_incentive" na empresa ERON, podemos observar uma diferença significativa entre esses dois extremos. O valor mínimo é de 69.223, enquanto o valor máximo é de 48.521.930. Essa diferença é bastante expressiva e indica uma disparidade considerável nos incentivos de longo prazo recebidos pelos funcionários.

## Other
"""

describe = df['other'].describe()
print(describe)
plt.boxplot(df['other'].dropna())
plt.title('Boxplot - Other')
plt.xlabel('Other')
plt.show()

"""### Análise
O boxplot gerado para a variável "other" apresenta uma representação gráfica da distribuição dos valores, destacando a mediana, os quartis e os possíveis valores discrepantes. Observa-se que há uma grande dispersão dos dados, com valores variando desde 2 até 42.667.590.
Esses dados sugerem que a variável "other" engloba uma ampla gama de categorias, como benefícios adicionais, compensações não especificadas e outros pagamentos que não se enquadram nas categorias mais comuns. A presença de valores discrepantes indica a existência de funcionários que receberam pagamentos adicionais substanciais.

## restricted_stock
"""

describe = df['restricted_stock'].describe()
print(describe)
plt.boxplot(df['restricted_stock'].dropna())
plt.title('Boxplot - Restricted Stock')
plt.xlabel('Restricted Stock')
plt.show()

"""###Análise
A presença de valores negativos indica a existência de funcionários com saldo de ações restritas inferior ao que foi originalmente concedido.

Esses resultados sugerem que a variável "restricted_stock" representa ações da empresa que foram concedidas a funcionários como parte de seu pacote de remuneração. A ampla dispersão dos valores indica que alguns funcionários possuem quantidades substanciais de ações restritas, enquanto outros possuem quantidades menores.

## restricted_stock_deferred
"""

describe = df['restricted_stock_deferred'].describe()
print(describe)
plt.boxplot(df['restricted_stock_deferred'].dropna())
plt.title('Boxplot - Restricted Stock Deferred')
plt.xlabel('Restricted Stock Deferred')
plt.show()

"""### Análise
É possível observar que a maioria dos valores se concentra em faixas negativas, indicando um saldo de estoque restrito negativo em relação às ações diferidas. Além disso, existem alguns valores extremos positivos que estão distantes da maior parte dos dados.

## salary
"""

describe = df['salary'].describe()
print(describe)
plt.boxplot(df['salary'].dropna())
plt.title('Boxplot - Salary')
plt.xlabel('Salary')
plt.show()

"""### Análise
Ao analisar o boxplot, é possível observar que a maior parte dos salários está concentrada em valores abaixo de $1,000,000, com alguns valores extremos acima desse limite. Esses valores extremos podem indicar salários excepcionalmente altos para alguns indivíduos.

### shared_receipt_with_poi
"""

describe = df['shared_receipt_with_poi'].describe()
print(describe)
plt.boxplot(df['shared_receipt_with_poi'].dropna())
plt.title('Boxplot - shared_receipt_with_poi')
plt.xlabel('shared_receipt_with_poi')
plt.show()

"""### Análise
Ao analisar o boxplot, podemos observar que a maioria dos valores está concentrada entre os quartis 25% e 75%, com a mediana (representada pela linha horizontal dentro da caixa) próxima de 740.5. Existem alguns valores considerados como outliers acima do quartil 75%, indicando uma possível presença de valores extremos nessa variável.

O compartilhamento de r