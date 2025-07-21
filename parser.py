from lexer import Token, INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, LPAREN, RPAREN, Lexer

# --- Classes para os nós da Árvore de Sintaxe Abstrata (AST) ---
class NumberNode:
    def __init__(self, token):
        self.token = token
        self.value = token.value
        
    def __repr__(self):
        return f"NumberNode({self.value})"

class BinaryOpNode:
    def __init__(self, left_node, op_token, right_node):
        self.left_node = left_node
        self.op_token = op_token
        self.right_node = right_node
        
    def __repr__(self):
        return f"({self.left_node} {self.op_token.type} {self.right_node})"

# --- A classe Parser ---
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = 0
        self.current_token = self.tokens[self.token_idx]
        
    def _advance(self):
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_token = self.tokens[self.token_idx]

    def _factor(self):
        token = self.current_token
        
        if token.type == LPAREN:
            self._advance()
            node = self._parse_expression()
            if self.current_token.type != RPAREN:
                raise Exception("Parêntese fechando ')' esperado")
            self._advance()
            return node
        elif token.type == INTEGER:
            self._advance()
            return NumberNode(token)
        else:
            raise Exception("Erro de sintaxe: Esperado um número ou '('")

    def _term(self):
        node = self._factor()
        
        while self.current_token and self.current_token.type in (MULTIPLY, DIVIDE):
            op_token = self.current_token
            self._advance()
            right_node = self._factor()
            node = BinaryOpNode(node, op_token, right_node)
            
        return node
        
    def _parse_expression(self):
        node = self._term()
        
        while self.current_token and self.current_token.type in (PLUS, MINUS):
            op_token = self.current_token
            self._advance()
            right_node = self._term()
            node = BinaryOpNode(node, op_token, right_node)
            
        return node
    
    def parse(self):
        if not self.tokens:
            return None
        return self._parse_expression()


if __name__ == '__main__':
    text = "10 + (2 * 5) - 3 / 1"
    
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