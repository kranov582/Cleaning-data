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

O comando covide_db.describe() mostrou uma série de informações uteis, como a média, contagem de valores, valor minimo e maximo, de cada uma das colunas:

![image](https://user-images.githubusercontent.com/97236661/167717359-7a328a9c-72fe-44f1-879b-16c48af092f8.png)

Analizando a imagem acima, e tambem aquela gerada após o comando .head(), é possivel afirmar que existem valores faltantes em algumas colunas. Por isso, o proximo passo foi verificar quais colunas estavam com dados faltantes, e quantos eram. Isso foi possivel com o comando covid_db.isnull().sum(), que retornou essas informações:
![image](https://user-images.githubusercontent.com/97236661/167717959-ca64b964-61bd-4239-971d-ec13ce7d5943.png)

Ao se deparar com valores faltantes em um banco de dados, existem algumas soluções que se pode chegar para tentar resolver o problema, e cada solução depende da quantidade de dados que estão faltantes.

Nas 6 primeiras colunas com valores faltantes e tambem na ultima coluna mostrada na imagem, é possivel notar que o valor encontrado é muito pequeno quando considerado o valor total da amostra (Mesmo com o valor mais alto encontrado, 6323, ainda é muito menor que os 724853 valores do banco de dados). Dado essa consideração, a solução escolhida foi apenas remover estas linhas faltantes, pois essa pequena quantidade não iria atrapalhar o aprendizado de um possivel algoritimo de Machine Learning. Para fazer essa remoção, foi escrito essa linha de codigo:
covid_db = covid_db.dropna(subset=['estado', 'municipio'])

Por outro lado, nas colunas de nome 'RecuperadosNovos' e 'emAcompanhamentoNovos', a quantidade de valores ausentes é de 724722, que é praticamente 100% dos valores do banco de dados. Nesse caso, a melhor solução é excluir a coluna inteira do banco de dados. Para fazer essa remoção, foi escrito essa linha de codigo:

covid_db = covid_db.drop(['Recuperadosnovos', 'emAcompanhamentoNovos'], axis=1)
