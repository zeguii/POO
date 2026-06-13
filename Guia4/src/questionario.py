from typing import List, Tuple, Dict
from src.pergunta import Pergunta

class Questionario:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.perguntas = []

    def adicionar_pergunta(self, p: Pergunta):
        self.perguntas.append(p)

    def criar_attempt(self, usuario: str):
        from src.tentativaquestionario import TentativaQuestionario
        return TentativaQuestionario(self, usuario)