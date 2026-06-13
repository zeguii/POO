from typing import List, Tuple, Dict
from abc import ABC, abstractmethod

class Pergunta(ABC):
    def __init__(self, texto: str, explicacao_geral: str = None):
        self.texto = texto
        self.explicacao_geral = explicacao_geral

    @abstractmethod
    def validar_resposta(self, resposta) -> bool:
        pass

    def get_explicacao(self) -> str:
        return self.explicacao_geral

    @abstractmethod
    def get_tipo(self) -> str:
        pass