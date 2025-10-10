from langchain_community.embeddings import HuggingFaceEmbeddings

# Define o nome do modelo de embedding que vamos usar.
# 'all-MiniLM-L6-v2' é um modelo popular, eficiente e de alta qualidade.
# Ele roda localmente na sua máquina (não precisa de API).

NOME_MODELO_EMBEDDING = 'all-MiniLM-L6-v2'

def obter_modelo_embedding():
    """
    Inicializa e retorna o modelo de embedding.

    O embedding é a representação numérica de um texto. Modelos de IA usam
    esses vetores para entender a "distância" e a similaridade semântica
    entre diferentes pedaços de texto.

    Returns:
        HuggingFaceEmbeddings: Uma instância do modelo de embedding pronto para uso.
    """
    print(f"Carregando o modelo de embedding '{NOME_MODELO_EMBEDDING}'...")
    
    # Usamos o HuggingFaceEmbeddings do LangChain que facilita o uso de modelos
    # da popular plataforma Hugging Face.
    # 'device': 'cpu' garante que o modelo rode na CPU. Se você tiver uma GPU
    # compatível (NVIDIA com CUDA), pode mudar para 'cuda'.
    modelo_embedding = HuggingFaceEmbeddings(
        model_name=NOME_MODELO_EMBEDDING,
        model_kwargs={'device': 'cpu'} 
    )
    
    print("Modelo de embedding carregado com sucesso.")
    return modelo_embedding