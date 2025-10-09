# Importa a classe necessária para a divisão de texto.
from langchain_text_splitters import RecursiveCharacterTextSplitter

def criar_chunks_de_texto(caminho_do_arquivo: str):
    """
    Lê um arquivo de texto e o divide em chunks semânticos usando uma estratégia recursiva.

    Args:
        caminho_do_arquivo: O caminho para o arquivo .txt contendo o código de ética.

    Returns:
        Uma lista de strings, onde cada string é um chunk de texto.
    """
    try:
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
            texto_completo = arquivo.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_do_arquivo} não foi encontrado.")
        return []

    # 1. Escolha da Estratégia: RecursiveCharacterTextSplitter
    # Esta é a estratégia mais robusta, pois tenta manter os parágrafos e frases juntos.
    meu_splitter = RecursiveCharacterTextSplitter(
        # Lista de separadores que a função tentará usar, em ordem.
        separators=["\n\n", "\n", ". ", " ", ""],
        
        # O tamanho máximo de cada chunk em número de caracteres.
        # Um bom valor inicial fica entre 500 e 1500.
        chunk_size=1000,
        
        # A sobreposição entre chunks. Isso ajuda a manter o contexto entre
        # os pedaços de texto. Se uma frase importante for cortada, ela
        # ainda estará completa no chunk seguinte.
        chunk_overlap=200,
        
        # Função para medir o tamanho do chunk. A padrão é len().
        length_function=len,
        
        # Mantém ou não o separador no final do chunk
        is_separator_regex=False,
    )

    # 2. Execução da Divisão
    # O método split_text aplica a lógica definida acima ao seu texto.
    lista_de_chunks = meu_splitter.split_text(texto_completo)

    return lista_de_chunks

# --- Caso de Uso ---
if __name__ == "__main__":
    # Supondo que seu código de ética está em um arquivo chamado 'codigo_de_etica.txt'
    caminho_arquivo = 'codigo_de_etica.txt'
    
    # Cria um arquivo de exemplo se ele não existir
    try:
        with open(caminho_arquivo, 'x', encoding='utf-8') as f:
            f.write("Artigo 1: Sobre a Integridade.\n\nTodos os colaboradores devem agir com a máxima integridade em todas as suas interações profissionais. Isso inclui honestidade, justiça e transparência. A empresa não tolera suborno, corrupção ou qualquer forma de conduta antiética. É proibido oferecer ou aceitar presentes que possam ser interpretados como uma tentativa de influenciar decisões de negócios.\n\nArtigo 2: Conflito de Interesses.\n\nOs colaboradores devem evitar situações em que seus interesses pessoais possam entrar em conflito com os interesses da empresa. Se um potencial conflito de interesses surgir, ele deve ser imediatamente comunicado ao departamento de Compliance para avaliação e orientação. A transparência é fundamental para resolver tais questões.")
    except FileExistsError:
        pass # O arquivo já existe, tudo bem.

    chunks_resultantes = criar_chunks_de_texto(caminho_arquivo)

    print(f"O documento foi dividido em {len(chunks_resultantes)} chunks.\n")

    # Mostra os primeiros chunks para análise
    for i, chunk in enumerate(chunks_resultantes):
        print(f"--- CHUNK {i + 1} (Tamanho: {len(chunk)} caracteres) ---")
        print(chunk)
        print("\n" + "="*50 + "\n")