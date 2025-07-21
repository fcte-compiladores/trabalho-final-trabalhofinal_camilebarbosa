# A classe Token representa uma unidade léxica (um token)

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f"Token({self.type}, {self.value})"
        return f"Token({self.type})"

# --- Tipos de tokens (constantes) ---
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'


# A classe Lexer é o coração do analisador léxico
class Lexer:
    def __init__(self, text):
        # O texto de entrada (a expressão)
        self.text = text
        # Posição atual do leitor no texto
        self.pos = 0
        # Caractere atual que está sendo lido
        self.current_char = self.text[self.pos]

    def _advance(self):
        # Move o leitor para o próximo caractere
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            # Símbolo especial para indicar o fim do texto
            self.current_char = None

    def _skip_whitespace(self):
        # Pula qualquer espaço em branco, nova linha, etc.
        while self.current_char is not None and self.current_char.isspace():
            self._advance()

    def _get_integer(self):
        # Lê um número de múltiplos dígitos
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self._advance()
        return int(result)

    def generate_tokens(self):
        # O método principal que gera a lista de tokens
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self._skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                tokens.append(Token(INTEGER, self._get_integer()))
                continue

            if self.current_char == '+':
                tokens.append(Token(PLUS))
                self._advance()
                continue

            if self.current_char == '-':
                tokens.append(Token(MINUS))
                self._advance()
                continue

            if self.current_char == '*':
                tokens.append(Token(MULTIPLY))
                self._advance()
                continue

            if self.current_char == '/':
                tokens.append(Token(DIVIDE))
                self._advance()
                continue

            if self.current_char == '(':
                tokens.append(Token(LPAREN))
                self._advance()
                continue

            if self.current_char == ')':
                tokens.append(Token(RPAREN))
                self._advance()
                continue

            # Se chegamos aqui, é um caractere desconhecido
            raise Exception(f'Caractere inválido: {self.current_char}')

        return tokens


# --- Exemplo para testar o código ---
if __name__ == '__main__':
    text = "10 + (2 * 5) - 3 / 1"
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    print("Tokens gerados:")
    print(tokens)