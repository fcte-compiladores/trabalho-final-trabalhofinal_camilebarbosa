from parser import NumberNode, BinaryOpNode
from lexer import PLUS, MINUS, MULTIPLY, DIVIDE

class Interpreter:
    def visit(self, node):
        # O método visit decide qual método chamar com base no tipo do nó.
        method_name = f'_visit_{type(node).__name__}'
        method = getattr(self, method_name, self._no_visit_method)
        return method(node)

    def _visit_NumberNode(self, node):
        # Visita um nó de número e retorna seu valor.
        return node.value

    def _visit_BinaryOpNode(self, node):
        # Visita um nó de operação binária.
        # Primeiro, visita os nós filhos (esquerda e direita) para obter seus valores.
        left_value = self.visit(node.left_node)
        right_value = self.visit(node.right_node)

        # Em seguida, realiza a operação com base no tipo do token.
        op_type = node.op_token.type
        if op_type == PLUS:
            return left_value + right_value
        elif op_type == MINUS:
            return left_value - right_value
        elif op_type == MULTIPLY:
            return left_value * right_value
        elif op_type == DIVIDE:
            # Adiciona uma verificação para evitar divisão por zero.
            if right_value == 0:
                raise Exception("Erro: Divisão por zero.")
            return left_value / right_value

    def _no_visit_method(self, node):
        # Método de fallback 
        raise Exception(f'Nenhum método visit para o tipo de nó {type(node).__name__}')