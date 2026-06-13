from typing import List, Tuple, Dict
from datetime import datetime
from src.questionario import Questionario
from src.respostaobjetiva import RespostaObjetiva
from src.respostadiscursiva import RespostaDiscursiva

class TentativaQuestionario:
    def __init__(self, questionario: Questionario, usuario: str):
        self.questionario = questionario
        self.usuario = usuario
        self.data_inicio = datetime.now()
        self.data_fim = None
        self.respostas = []

    def registrar_resposta(self, indice_pergunta: int, valor):
        if self.is_finalizado():
            return
        
        if 0 <= indice_pergunta < len(self.questionario.perguntas):
            pergunta = self.questionario.perguntas[indice_pergunta]
            
            if pergunta.get_tipo() == "multipla_escolha":
                resposta = RespostaObjetiva(pergunta, valor)
            else:
                resposta = RespostaDiscursiva(pergunta, valor)
            
            resposta.calcular_pontuacao()
            self.respostas.append(resposta)

    def is_finalizado(self) -> bool:
        return self.data_fim is not None

    def calcular_pontuacao(self) -> float:
        return sum(r.pontuacao_obtida for r in self.respostas)

    def finalizar(self) -> tuple[float, str]:
        if not self.is_finalizado():
            self.data_fim = datetime.now()
            
        pontuacao_total = self.calcular_pontuacao()
        mensagem = f"Questionário finalizado. Pontuação: {pontuacao_total}"
        return (pontuacao_total, mensagem)