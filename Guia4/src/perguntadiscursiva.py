from typing import List, Tuple, Dict
from src.pergunta import Pergunta

class PerguntaDiscursiva(Pergunta):
    def __init__(self, texto: str, resposta_esperada: str = None, explicacao_geral: str = None):
        super().__init__(texto, explicacao_geral)
        self.resposta_esperada = resposta_esperada

    def validar_resposta(self, texto: str) -> bool:
        if self.resposta_esperada is None:
            return True
        return str(texto).strip().lower() == str(self.resposta_esperada).strip().lower()

    def get_tipo(self) -> str:
        return "discursiva"