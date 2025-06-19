# VarroaScan

Aplicativo móvel para identificação do ácaro *Varroa destructor* em colônias de abelhas, utilizando redes neurais convolucionais e o conjunto de dados VarroaDataset.

## Estrutura de Diretórios

- **api/**  
  Contém o código-fonte da API de visão computacional utilizada para realizar as predições.

- **app/**  
  Contém o código-fonte da aplicação móvel desenvolvida para Android.

- **dataset/**  
  Conjunto de dados original, sem modificações.

- **dataset-sm/**  
  Versão reduzida e adaptada do dataset original, com menor quantidade de imagens e coordenadas de *bounding boxes* normalizadas.

- **yolo/**  
  Contém o código utilizado para o treinamento do modelo YOLOv8, incluindo o notebook do Google Colab e o script de normalização das *bounding boxes*.

- **varroa-scan.apk**  
  Arquivo APK da aplicação, disponível para instalação direta em dispositivos Android.

## Conjunto de Dados

Este projeto utiliza o [VarroaDataset](https://github.com/schurist/VarroaDataset), um conjunto de imagens anotadas para a detecção do ácaro *Varroa destructor* em abelhas, publicado por Schurischuster et al.

O dataset original está disponível no repositório oficial:  
🔗 [github.com/schurist/VarroaDataset](https://github.com/schurist/VarroaDataset)

Créditos ao autor original:
> **Schurischuster, H. et al.**  
> *VarroaDataset – A public image dataset for detection of the Varroa destructor mite on honey bees*  
> Disponível em: https://github.com/schurist/VarroaDataset
