from typing import List, Tuple, Dict
from abc import ABC, abstractmethod
from src.pergunta import Pergunta

class Resposta(ABC):
    def __init__(self, pergunta: Pergunta):
        self.pergunta = pergunta
        self.esta_correta = False
        self.pontuacao_obtida = 0.0

    @abstractmethod
    def calcular_pontuacao(self) -> float:
        pass