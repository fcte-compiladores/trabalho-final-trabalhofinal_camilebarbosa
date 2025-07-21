# **Interpretador de Expressões Aritméticas: Uma introdução ao mundo dos Compiladores!**

---

## **Integrantes**
* **Nome:** Camile Barbosa Gonzaga de Oliveira
* **Matrícula:** 251035022
* **Turma:** 16H

---
## **Objetivo**
O objetivo deste repositório é servir como porta entrada a estudantes e curiosos da computação!

## **Introdução**
No coração da computadores, os **compiladores** e **intérpretes** são os programas mágicos que permitem que essas máquinas entendam as instruções que escrevemos. Eles são os tradutores essenciais que convertem o nosso código, que é escrito em linguagens de alto nível, em algo que a máquina pode executar.

Enquanto um **compilador** geralmente traduz um código-fonte completo de uma vez, gerando um arquivo executável, um **interpretador** executa o código linha por linha. Este projeto segue a lógica de um interpretador para demonstrar as etapas fundamentais desse processo de tradução.

O processo de interpretação pode ser dividido em três fases principais, cada uma com um propósito distinto, mas interligado:

1.  **Análise Léxica:** Pense na análise léxica como a primeira leitura do código. Nessa etapa, o interpretador lê o texto da expressão, caractere por caractere, e o quebra em pequenas unidades significativas, chamadas **tokens**. Por exemplo, na expressão `10 + 5`, a análise léxica identificaria o número `10`, o sinal de adição `+` e o número `5` como tokens individuais. É a fase em que o código é transformado de uma simples sequência de caracteres em uma lista de "palavras" que a máquina pode entender.

2.  **Análise Sintática:** Após a análise léxica, a análise sintática entra em ação. Ela é como a gramática de uma língua. Sua função é pegar a lista de tokens e construir uma estrutura hierárquica que representa a lógica da expressão, chamada **Árvore de Sintaxe Abstrata (AST)**. Essa árvore garante que o código faça sentido e respeite as regras da linguagem. Por exemplo, ela reconhece que o sinal `+` opera sobre os números `10` e `5` e que os parênteses alteram a ordem das operações.

3.  **Interpretação ou Avaliação:** A etapa final é onde a mágica acontece. O interpretador percorre a árvore de sintaxe construída e executa as operações. Ele visita cada nó da árvore, avalia os valores e realiza as operações matemáticas na ordem correta, chegando ao resultado final da expressão. É nessa fase que o significado do código se torna realidade.

A linguagem implementada é minimalista, suportando apenas números inteiros e os operadores de adição (`+`), subtração (`-`), multiplicação (`*`), divisão (`/`), além de parênteses para agrupar expressões.

**Exemplos da linguagem:**
* `10 + 5`
* `3 * (2 + 4)`
* `100 / 2 - 5`

---
## ** Ferramentas **

O desenvolvimento deste projeto foi conduzido com o uso de três ferramentas principais, cada uma com um papel específico e fundamental para a sua realização.

Python 3: A linguagem de programação é o principal. A sintaxe clara e a vasta coleção de bibliotecas Python a tornam perfeita para criar nosso projeto. Nós implementamos as diferentes etapas do interpretador em arquivos separados, facilitando a compreensão e a organização do código, tudo isso graças ao Python.

GitHub: O GitHub foi utilizado para o versionamento e a entrega do projeto. A plataforma permitiu gerenciar o código-fonte de forma eficiente e organizar a documentação de acordo com os requisitos do professor.

Markdown: O Markdown utilizado para a criação da documentação no arquivo README.md (Este que você está lendo).


## **Instalação**
Não há dependências externas. Para rodar o interpretador, basta clonar o repositório (git clone __link do repositório__) e executar o arquivo principal (`main.py`) com um interpretador Python 3 no seu terminal ( -- python3 main.py -- ).


## **Estrutura do Código**
A arquitetura do projeto é modular e foi projetada para que cada arquivo represente uma etapa do processo de compilação.

lexer.py: O Analisador Léxico. Este módulo lê a expressão de entrada (uma sequência de caracteres) e a transforma em uma lista de tokens. Ele é a primeira etapa, responsável por quebrar a "frase" em "palavras".

parser.py: O Analisador Sintático. Este módulo recebe a lista de tokens do analisador léxico e a organiza em uma Árvore de Sintaxe Abstrata (AST). Ele garante que a expressão siga as regras gramaticais da linguagem (como a ordem de operações).

interpreter.py: O Interpretador. Este módulo é o avaliador da expressão. Ele percorre a AST e realiza as operações matemáticas de forma recursiva para calcular o resultado final.

main.py: O Ponto de Entrada. Este arquivo orquestra todo o processo, chamando o Lexer, o Parser e o Interpreter em sequência e, mais importante, imprime o resultado de cada etapa, servindo como uma ferramenta pedagógica para visualização.

O programa está configurado para ler e processar automaticamente os exemplos contidos na pasta examples/.

---

## **Exemplos**
A pasta examples/ contém arquivos de texto que demonstram as funcionalidades do interpretador. Cada arquivo serve para testar um aspecto diferente da implementação:

E01.txt: Demonstra o funcionamento básico com uma expressão simples.

E02.txt: Prova que o parser lida corretamente com a ordem de operações (multiplicação antes da adição).

E03.txt: Mostra como o interpretador reage a um erro, reportando a falha de forma adequada.

E04.txt: Também demonstra o funcionamento básico com uma expressão simples, mas com números maiores.

---

## **Bugs e Limitações Conhecidas**

Este projeto é um protótipo pedagógico e, por isso, possui algumas limitações. Melhorias futuras poderiam incluir:

Suporte a números com ponto flutuante (decimais).

Implementação de variáveis e atribuição (x = 10).

Tratamento de erros mais robusto e descritivo.

---

## **Referências**
Pense em Python (Allen B. Downey) - Utilizado como material de referência para a programação do projeto em Python.

---