from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run_interpreter(text):
    # Passo 1: Análise Léxica
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    print("Tokens gerados:")
    print(tokens)
    print("-" * 20)

    # Passo 2: Análise Sintática
    parser = Parser(tokens)
    ast_root = parser.parse()
    print("Árvore de Sintaxe Abstrata (AST) gerada:")
    print(ast_root)
    print("-" * 20)

    # Passo 3: Interpretação
    interpreter = Interpreter()
    result = interpreter.visit(ast_root)
    print("Resultado da expressão:")
    print(result)

if __name__ == '__main__':
    with open('examples/E04.txt', 'r') as file:
        expression = file.read()
    
    run_interpreter(expression)


# Podemos adicionar também mais exemplos aqui para testar

# if __name__ == '__main__':
#     # Exemplo de uso com uma expressão
#     expression = "10 + (2 * 5) - 3 / 1"
#     run_interpreter(expression)
