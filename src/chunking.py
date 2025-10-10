import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.schema.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Define o caminho para a pasta onde os documentos brutos estão.
CAMINHO_DOCUMENTOS_RAW = "data/raw"

def carregar_documentos(caminho_pasta: str) -> List[Document]:
    """
    Carrega todos os documentos .txt e .pdf de um diretório especificado.

    Args:
        caminho_pasta (str): O caminho para a pasta contendo os documentos.

    Returns:
        List[Document]: Uma lista de objetos Document, cada um representando um arquivo.
    """
    documentos_carregados = []
    
    # Lista todos os arquivos no diretório fornecido.
    for arquivo in os.listdir(caminho_pasta):
        # Constrói o caminho completo para o arquivo.
        caminho_completo_arquivo = os.path.join(caminho_pasta, arquivo)
        
        # Escolhe o carregador (Loader) apropriado com base na extensão do arquivo.
        if arquivo.endswith(".pdf"):
            loader = PyPDFLoader(caminho_completo_arquivo)
            print(f"Carregando documento PDF: {arquivo}...")
        elif arquivo.endswith(".txt"):
            # Especifica o encoding como 'utf-8'
            loader = TextLoader(caminho_completo_arquivo, encoding='utf-8')
            print(f"Carregando documento de texto: {arquivo}...")
        else:
            # Pula arquivos com extensões não suportadas.
            print(f"Arquivo '{arquivo}' com formato não suportado. Pulando.")
            continue
            
        # Carrega o documento e o adiciona à nossa lista.
        documentos_carregados.extend(loader.load())
        
    return documentos_carregados

def dividir_documentos_em_chunks(documentos: List[Document]) -> List[Document]:
    """
    Divide os documentos carregados em pedaços menores (chunks) de tamanho fixo.

    Isto é crucial para o RAG, pois permite que o modelo de embedding processe
    o texto em partes manejáveis e encontre trechos mais específicos durante a busca.

    Args:
        documentos (List[Document]): A lista de documentos carregados.

    Returns:
        List[Document]: Uma nova lista de Documentos, onde cada um é um chunk do original.
    """
    print("Dividindo documentos em chunks...")
    
    # RecursiveCharacterTextSplitter é uma estratégia recomendada.
    # Ele tenta manter parágrafos, sentenças e palavras juntos o máximo possível.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Define o tamanho máximo de cada chunk (em caracteres).
        chunk_overlap=200, # Define uma sobreposição entre chunks para não perder contexto.
        length_function=len
    )
    
    chunks_de_texto = text_splitter.split_documents(documentos)
    print(f"Total de {len(documentos)} documentos divididos em {len(chunks_de_texto)} chunks.")
    return chunks_de_texto

def processar_documentos() -> List[Document]:
    """
    Função principal que orquestra o carregamento e a divisão dos documentos.
    
    Returns:
        List[Document]: A lista final de chunks de documentos, prontos para serem vetorizados.
    """
    print("Iniciando o processamento dos documentos...")
    documentos = carregar_documentos(CAMINHO_DOCUMENTOS_RAW)
    if not documentos:
        print("Nenhum documento encontrado para processar.")
        return []
    
    chunks = dividir_documentos_em_chunks(documentos)
    return chunks