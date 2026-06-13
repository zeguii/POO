from typing import List, Tuple, Dict
from src.pergunta import Pergunta
from src.alternativa import Alternativa

class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto: str, alternativas: list[Alternativa], explicacao_geral: str = None):
        super().__init__(texto, explicacao_geral)
        self.alternativas = alternativas

    def validar_resposta(self, indice: int) -> bool:
        if 0 <= indice < len(self.alternativas):
            return self.alternativas[indice].correta
        return False

    def get_alternativa_correta(self) -> Alternativa:
        for alt in self.alternativas:
            if alt.correta:
                return alt
        return None

    def get_tipo(self) -> str:
        return "multipla_escolha" 
    
    