import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def obter_modelo_embedding_gemini():
    """
    Inicializa e retorna o modelo de embedding do Google Gemini.

    Esta função lê a chave de API do Google a partir das variáveis de ambiente
    e configura o modelo 'embedding-001' para ser usado com o LangChain.

    Returns:
        GoogleGenerativeAIEmbeddings: Uma instância do modelo de embedding do Gemini.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("A variável de ambiente GOOGLE_API_KEY não foi encontrada. Verifique seu arquivo .env.")

    print("Carregando o modelo de embedding 'embedding-001' do Gemini...")
    
    # Inicializa o modelo de embedding do Gemini através do wrapper do LangChain.
    # O modelo "embedding-001" é otimizado para tarefas de Retrieval (RAG).
    gemini_embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )
    
    print("Modelo de embedding do Gemini carregado com sucesso.")
    return gemini_embeddings