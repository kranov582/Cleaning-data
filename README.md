# Projeto de limpeza de dados
Este projeto tem o objetivo de ilustrar a capacidade do autor de limpar e organizar os dados da maneira correta. O banco de dados utilizado foi o dataset de casos de covid no brasil, no ano de 2022, disponivel aqui: https://covid.saude.gov.br/


Neste projeto foi utilizado a IDE PyCharm Community Edition 2021.3.3, com a versão 3.9 do Python. O arquivo do dataset foi salvo em formato .csv, e foi utilizado o excel para fazer manipulações. Para manipular o dataset no Python, foi utilizado a biblioteca Pandas.

Inicialmente, o banco de dados estava com algums problemas que impediram o carregamento do mesmo para a IDE do PyCharm. O problema era que algumas linhas estavam com uma virgula a mais, decorrente da separação de regioes dentro da coluna referente a "nomeRegiaoSaude".

![image](https://user-images.githubusercontent.com/97236661/167715241-f950f262-d875-4d05-8de6-676e5a37260e.png)


A solução foi abrir o arquivo pelo excel e alterar manualmente as virgulas desta coluna por pontos.
Após essa alteração, o arquivo foi carregado normalmente na IDE do PyCharm, na variavel covid_db.
O proximo passo após isso foi verificar como estavam os primeiros valores do dataset, o tamanho da matriz e tambem a descrição dos dados. Para a melhor visualização, foi configurado para que o Python mostrasse toda o conjunto de dados:

![image](https://user-images.githubusercontent.com/97236661/167716320-57e0c0c2-df06-4fe2-970a-45ca84b15e8f.png)

O comando covid_db.head() mostrou as 5 primeiras linhas de todas as colunas:
![image](https://user-images.githubusercontent.com/97236661/167716691-c0235528-3672-4f56-9b68-9d893fc2c364.png)

O comando covid_db.shape() mostrou o tamanho do dataset, que retornou o valor de (724853, 17), sendo o primeiro o valor de linhas e o segundo o de colunas.

O comando covide_db.describe() mostrou uma série de informações uteis, como a média, contagem de valores, valor minimo e maximo, de cada uma das colunas.
![image](https://user-images.githubusercontent.com/97236661/167717359-7a328a9c-72fe-44f1-879b-16c48af092f8.png)







