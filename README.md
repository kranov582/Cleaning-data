# Projeto de limpeza de dados
Este projeto tem o objetivo de ilustrar a capacidade do autor de limpar e organizar os dados da maneira correta. O banco de dados utilizado foi o dataset de casos de covid no brasil, no ano de 2022, disponivel aqui: https://covid.saude.gov.br/


Neste projeto foi utilizado a IDE PyCharm Community Edition 2021.3.3, com a versão 3.9 do Python. O arquivo do dataset foi salvo em formato .csv, e foi utilizado o excel para fazer manipulações. Para manipular o dataset no Python, foi utilizado a biblioteca Pandas.

Inicialmente, o banco de dados estava com algums problemas que impediram o carregamento do mesmo para a IDE do PyCharm. O problema era que algumas linhas estavam com uma virgula a mais, decorrente da separação de regioes dentro da coluna referente a "estado".

![image](https://user-images.githubusercontent.com/97236661/167714912-7c350aae-01a4-4d4e-a65f-adcf37c4c975.png)

A solução foi abrir o arquivo pelo excel e alterar manualmente as virgulas desta coluna por pontos.

