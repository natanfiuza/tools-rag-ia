from typing import List
from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma

# Define o caminho onde o banco de dados vetorial será salvo.
CAMINHO_DB = "chroma_db"

def criar_e_armazenar_vetores(chunks: List[Document], modelo_embedding):
    """
    Cria os embeddings para cada chunk e os armazena no ChromaDB.

    Este processo pode demorar um pouco na primeira vez, dependendo do
    número de documentos e da potência do seu computador.

    Args:
        chunks (List[Document]): A lista de chunks de texto.
        modelo_embedding: A instância do modelo de embedding a ser usado.
    """
    print("Criando e armazenando embeddings no ChromaDB...")
    
    # O Chroma.from_documents faz todo o trabalho pesado:
    # 1. Pega cada chunk.
    # 2. Usa o `modelo_embedding` para criar o vetor.
    # 3. Salva o chunk e seu vetor correspondente no banco de dados.
    # `persist_directory` garante que os dados sejam salvos em disco.
    vector_store = Chroma.from_documents(
        documents=chunks, 
        embedding=modelo_embedding, 
        persist_directory=CAMINHO_DB
    )
    
    print(f"Embeddings salvos com sucesso no diretório: {CAMINHO_DB}")

def realizar_busca_por_similaridade(pergunta: str, modelo_embedding) -> List[Document]:
    """
    Carrega o banco de dados vetorial existente e busca os chunks mais
    relevantes para uma determinada pergunta.

    Args:
        pergunta (str): A pergunta do usuário.
        modelo_embedding: A instância do modelo de embedding.

    Returns:
        List[Document]: Uma lista dos chunks mais similares à pergunta.
    """
    print("Carregando banco de dados vetorial existente...")
    
    # Carrega o banco de dados que foi salvo anteriormente.
    vector_store = Chroma(
        persist_directory=CAMINHO_DB, 
        embedding_function=modelo_embedding
    )
    
    print(f"Realizando busca por similaridade para a pergunta: '{pergunta}'")
    
    # Usa a função `similarity_search` para:
    # 1. Converter a `pergunta` em um vetor usando o mesmo `modelo_embedding`.
    # 2. Comparar este vetor com todos os vetores armazenados no banco.
    # 3. Retornar os 'k' chunks mais próximos (mais similares semanticamente).
    # k=3 significa que queremos os 3 resultados mais relevantes.
    documentos_encontrados = vector_store.similarity_search(query=pergunta, k=3)
    
    return documentos_encontrados