from typing import List, Tuple, Dict
from src.resposta import Resposta
from src.perguntadiscursiva import PerguntaDiscursiva

class RespostaDiscursiva(Resposta):
    def __init__(self, pergunta: PerguntaDiscursiva, texto_resposta: str):
        super().__init__(pergunta)
        self.texto_resposta = texto_resposta
        self.calcular_pontuacao()

    def calcular_pontuacao(self) -> float:
        self.esta_correta = self.pergunta.validar_resposta(self.texto_resposta)
        self.pontuacao_obtida = 1.0 if self.esta_correta else 0.0
        return self.pontuacao_obtida
