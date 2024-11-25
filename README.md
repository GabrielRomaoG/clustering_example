# Teste Localiza

## Preprocessamento

No arquivo preprocessing.py eu escrevi uma função que processa os dois arquivos csv dos datasets. Nele eu faço o carregamento das duas bases, trato NULL values, faço o join dos dois, e mapeio os tipos de dados das colunas.

## Escolha do modelo

Haja visto que Clustering é um tipo de análise mais subjetiva, eu decidi considerar o melhor modelo aquele que melhor segmenta os data points de um plot de PCA realizado no Dataset.

### Processamento

No processamento para inserir no modelo, foi realizado uma transformação para tornar as variáveis categóricas em booleanas (0 e 1) já que modelos não aceitam strings e padronizar as variáveis númericas, haja visto que a escala de uma coluna afeta alguns modelos de clustering.

Todas as variáveis foram utilizadas pois realizei os tratamentos necessários para utilização de todas.

### Sobre o PCA

Principal Component Analysis ou PCA é uma técnica de redução de dimensão aplicada a datasets com muitas features, assim podemos ver todos os data points do nosso dataset em apenas duas dimensões.

### KMeans e Hierarchical Clustering

O KMeans visualmente segmentou melhor os data points portanto eu o escolhi como melhor modelo para este dataset em específico, é possível ver a performance do Hierarchical Clustering logo abaixo da seção do KMeans. 


