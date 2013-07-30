Proposta de projetinho para avaliação
-------------------------------------


### Idéia Básica

Visualização dos microdados do INEP.


### Contexto

Há alguns anos, o INEP fornece, ao público, acesso aos microdados de
diversos dos levantamentos feitos pelo instituto. Esses dados, ainda que
anonimizados, fornecem incrível nível de detalhe sobre o que acontece em
cada um dos componentes do sistema de educação básica brasileiro. O
formato disponibilizado, porém, é espartano e praticamente inacessível a
pessoas que não têm conhecimento tecnológico para seu manuseio: os
maiores arquivos chegam a 6 GB de dados puros.

            +---------------------+
            |                     |
            |                     |           +----------+
            |         BIG         |           | oh noes! |
            |                     |           +----------+
            |                     |          /                    
            |         DATA        |     /O\                   
            |                     |     \|/                   
            |                     |      |                   
            +---------------------+     / \

Neste projeto, sua tarefa é construir uma aplicação web que
disponibilize as informações presentes nesses microdados em um formato
que pessoas mortais possam consumir.


### A aplicação

Uma maneira bacana de visualizar esses dados, provavelmente, consiste em
construir uma aplicação web que forneça agregações dos microdados.

Um dos problemas dos microdados é o de que o nível de detalhe é extremo
(e.g.: notas de alunos) enquanto a informação só passa a ser útil em
níveis mais agregados, como escola (e.g.: distribuição das notas em uma
escola) ou cidade (e.g.: porcentagem de escolas em um município com
média abaixo de determinado limiar). O que queremos aqui é agregar dados
para produzir informação/métricas de qualidade.

Para este projeto, qualquer ideia que resolva de uma maneira
interessante o problema do parágrafo acima é válida. No entanto, fazemos
também uma sugestão de caminho a seguir que pode ser seguida ou ignorada
à vontade.


### A sugestão

Uma das visualizações clássicas do desempenho agregado de um grupo é o
histograma. Média e desvio padrão ajudam até certo ponto, mas o
histograma oferece uma fotografia muito mais detalhada do que
efetivamente acontece.


                ^
                |              *
                |              | * *
                |            * |     *
                |          *   |     |
                |    * * *     |     | *
                |  *     |     |     |   *
                |*       |     |     |     *
                +----------------------------->
                        µ-σ    µ    µ+σ


Mais precisamente, a ideia seria permitir a visualização, por exemplo,
do desempenho de uma escola *versus* o desempenho da cidade ou estado em
que se encontra a escola através da sobreposição dos dois histogramas. A
seguir, um exemplo de sobreposição de dois histogramas para fins de
comparação.


![exemplo carteado da internet com dois histogramas sobrepostos para
comparação][img1]


A interface pode ser bem simples; não estamos avaliando com muita
atenção o webdesign da aplicação uma vez que o foco é a engenharia. Para
o caso mais simples em que apenas damos a opção de comparar a escola com
a cidade em que se encontra, pode-se pensar em algo como uma página
única em que o usuário escolhe a escola através de uma busca textual e
já pode ver o histograma da escola escolhida versus a cidade em que a
escola se insere:


        +-----------------------------------------+--------+
        | montessori                              | Buscar |
        +-----------------------------------------+--------+
          |   MARIA MONTESSORI                           |
          |   MONTESSORI SANTA TEREZINHA COLEGIO         |
          | > PRIMA ESCOLA MONTESSORI DE SAO PAULO       |
          |   AGUAI ESCOLA MONTESSORIANA                 |
          +----------------------------------------------+

        Escola: PRIMA ESCOLA MONTESSORI DE SAO PAULO

        Histograma comparando com a cidade:

        << insira aqui o histograma >>    


Logicamente, é possível tornar esse sistema tão sofisticado quanto se
queira. Mas acreditamos que o modelo atual é um bom ponto de partida. A
partir deste ponto, é fácil imaginar introduzir features como o
histograma versus o estado, versus o país, comparação entre escolas,
comparação entre áreas diferentes do conhecimento, comparação entre
regiões do país...


### Os dados

Os dados necessários para esta aplicação estão amplamente disponíveis. O
INEP disponibiliza os microdados de seus levantamentos em seu site
http://portal.inep.gov.br/basica-levantamentos-microdados. Os
levantamentos que provavelmente são interessantes no nosso caso são o
**Censo Escolar** para obtenção do catálogo de escolas e o **ENEM** para
a distribuição de notas. Os dois levantamentos compartilham uma chave
comum, então não deve haver problemas com cruzamento de dados.

O tamanho dos dados é particularmente difícil de lidar: os microdados do
ENEM, por exemplo, abordam informações detalhadas de mais de 5 milhões
de alunos. Para nós da Geekie, é importante saber lidar com tal
quantidade de dados, mas ao mesmo tempo entendemos as limitações de
tempo para um projeto como o que está sendo proposto.

Propomos então **que apenas os dados de escolas referentes ao município
de São Paulo - SP sejam considerados.** Isso diminui a carga de alunos
para aproximadamente 80 mil alunos, um número bem mais administrável.

Também propomos que apenas uma das quatro áreas de conhecimento (entre
Ciências da Natureza, Ciências Humanas, Linguagens e Matemática) seja
considerada, a fim de evitar código tedioso.


### As regras do jogo

A proposta é que a pessoa esteja livre para escolher como arquitetar sua
solução no nível de aplicação. Para o stack/framework, sugerimos
fortemente um dos stacks atualmente utilizados pela engenharia da
Geekie:

 - Linguagem: Python
 - Hosting: Google AppEngine, Heroku (provavelmente o mais fácil)
 - Framework: webapp2, Flask (provavelmente o mais fácil), Pyramid
 - DB: Google AppEngine datastore, MongoDB (provavelmente o mais fácil), ZODB,
   possivelmente MySQL/PostgreSQL

Queremos ver a aplicação rodando hospedada já em algum lugar, por isso
já propomos também o stack de hosting preferencial.

Valorizamos simplicidade e soluções espertas, bem como **saber utilizar
o que já existe a seu favor.** Se já existir magicamente uma library que
cria uma página com exatamente esses requisitos, está valendo. Serviços
third-party são fair game, em particular addons como os que o Heroku
disponibiliza.

A ideia do desafio é que possa ser completado em 3 dias. Programadores
rápidos devem ser capazes de terminar o desafio em 1 dia.

Em caso de dúvidas, contactar sherman@geekie.com.br e tentaremos responder
ASAP.

---

[img1]: http://openi.nlm.nih.gov/imgs/rescaled512/3056740_1752-0509-5-31-3.png 
"Exemplo aleatório da internet com dois histogramas sobrepostos para comparação"
