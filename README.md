# varroa-scan
A mobile application capable of identifying the Varroa destructor mite in bee colonies using convolutional neural networks and VarroaDataset

## SEMANA 1

- 1 - Com a ajuda da ferramenta labelImg, rotular 1 imagem da base de dados para ver o formato que ele gera para o YOLO
- 2 - Comparar o label gerado para o YOLO com o original da base de dados
- 3 - Criar algoritmo que converte o formato das labels originais para o formato do YOLO para evitar rotulamento manual
- 4 - Pegar a base original e normalizar as coordenadas de bounding boxes no formato do YOLO
- 5 - Criar uma versão menor da base de dados para testar no treinamento
    - para o conjunto de
        - treinamento: 200 exemplos de 8225 (2,4%)
        - teste: 100 de 3408 (2,93%)
        - validação: 70 de 1876 (3,73%)
- 6 - Testar com imagens aleatórias do google o modelo treinado com a base pequena

------------------------------------------------------------------------------------------------------------------
## SEMANA 2

- 1 - Testar ajustar hiperparâmetros na base pequena para ver se existe uma melhora
- 2 - Dobrar o tamanho da base pequena e ver como o modelo se sai
- 3 - Repetir o passo 1
- 4 - Repetir o passo 2

