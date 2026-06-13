from typing import Dict
from src.perguntadiscursiva import PerguntaDiscursiva
from src.llmservice import LLMService

class Correcao:
    @staticmethod
    def corrigir_discursiva(pergunta: PerguntaDiscursiva, resposta_aluno: str, service: LLMService = None) -> Dict:
        # Se nenhum serviço for passado, instancia o padrão automaticamente
        if service is None:
            service = LLMService()
            
        return service.corrigir_resposta(pergunta, resposta_aluno)

    @staticmethod
    def criar_prompt_correcao(pergunta: PerguntaDiscursiva, resposta_aluno: str) -> str:
        # Método utilitário para isolar a montagem do prompt se necessário
        return f"Pergunta: {pergunta.texto} | Esperado: {pergunta.resposta_esperada} | Aluno: {resposta_aluno}"