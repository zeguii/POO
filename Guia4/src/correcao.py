from typing import Dict
from src.perguntadiscursiva import PerguntaDiscursiva
from src.llmservice import LLMService

class Correcao:
    @staticmethod
    def corrigir_discursiva(pergunta: PerguntaDiscursiva, resposta_aluno: str, service: LLMService = None) -> Dict:
        if service is None:
            service = LLMService()
            
        return service.corrigir_resposta(pergunta, resposta_aluno)

    @staticmethod
    def criar_prompt_correcao(pergunta: PerguntaDiscursiva, resposta_aluno: str) -> str:
        return f"Pergunta: {pergunta.texto} | Esperado: {pergunta.resposta_esperada} | Aluno: {resposta_aluno}"


CorrecaoUtil = Correcao