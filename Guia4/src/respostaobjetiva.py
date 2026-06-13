from typing import List, Tuple, Dict
from src.resposta import Resposta
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha

class RespostaObjetiva(Resposta):
    def __init__(self, pergunta: PerguntaMultiplaEscolha, indice_escolhido: int):
        super().__init__(pergunta)
        self.indice_escolhido = indice_escolhido
        
        if 0 <= indice_escolhido < len(pergunta.alternativas):
            self.alternativa_selecionada = pergunta.alternativas[indice_escolhido]
        else:
            self.alternativa_selecionada = None
            
        self.calcular_pontuacao()

    def calcular_pontuacao(self) -> float:
        self.esta_correta = self.pergunta.validar_resposta(self.indice_escolhido)
        self.pontuacao_obtida = 1.0 if self.esta_correta else 0.0
        return self.pontuacao_obtida